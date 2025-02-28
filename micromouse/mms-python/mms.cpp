// count instead of x in fwd()
// distance instead of val
#include <Wire.h>
#include <MPU6050.h>

// Motor driver and sensor pins
#define PWMA 32
#define AIN1 25
#define AIN2 33
#define PWMB 14
#define BIN1 26
#define BIN2 27
#define C1 18
#define C2 19
#define buttonPin 5
#define trigpinleft 16
#define trigpinright 17
#define trigpinfront 4

#define IR_left 34
#define IR_right 35
#define IR_front 36

MPU6050 mpu;

// Global variables for IMU and motion

float a, gyroX, gyroY;
float yaw = 0.0;
int n = 1, cvalue = 0;
bool rotated = false;
double count = 0;
float orientation = 0.0;
int target_orientation = 0;
int turns = 0;
bool leg=false;
float gyroZ, accelX, accelY, accelZ;
float accelRoll;
unsigned long prevTime = 0;
double val = 17 / (3.141 * 3.2);
int wl, wr, wf;
int yawvalue = 40;
int fwdspeed = 125;
int turnspeedhigh = 120;
int turnspeedlow = 50;
int step=0;
int final_track[400][2];


//------------------------ Motor and Sensor Functions ------------------------//

void fwd() {
 count = 0;
 int x = 0;
 // Drive until the encoder count (scaled by 700) exceeds val.
 while ((count / 700.0) < val) {
 updateIMU();
 x++;
 if (x % 30 == 0) {
 wallStatus(wl, wr, wf);
 if (wf > 1600) {
 applyBrakes();
 // Use return to exit this function if a wall is too close.
 return;
 }
 if (wr > 400 && wl > 1000) {
 yaw += ((wl - wr) / 1000.0) * 1.5;
 orientation = 0.98 * yaw + (1 - 0.98) * accelRoll;
 }
 }
 if (abs(orientation) < 2) {
 moveForward(fwdspeed, fwdspeed);
 } else if (orientation < -2) {
 moveForward(turnspeedlow, turnspeedhigh); // Correcting towards right
 } else if (orientation > 2) {
 moveForward(turnspeedhigh, turnspeedlow); // Correcting towards left
 }
 }
 applyBrakes();
}

void increment() {
 count++;
}

void updateIMU() {
 unsigned long currentTime = millis();
 float dt = (currentTime - prevTime) / 1000.0;
 prevTime = currentTime;
 
 gyroZ = mpu.getRotationZ() / 131.0;
 if (gyroZ < 1 && gyroZ > -1) gyroZ = 0;
 
 accelX = mpu.getAccelerationX() / 16384.0;
 accelY = mpu.getAccelerationY() / 16384.0;
 accelZ = mpu.getAccelerationZ() / 16384.0;
 accelRoll = atan2(-accelX, accelZ) * 180 / PI;
 
 yaw += gyroZ * dt;
 orientation = 0.99 * yaw + (1 - 0.99) * accelRoll;
}

void turnRight() {
 // Turn until orientation nears 75 degrees
 while (abs(orientation) < 75) {
 updateIMU();
 digitalWrite(AIN1, HIGH);
 digitalWrite(AIN2, LOW);
 digitalWrite(BIN1, HIGH);
 digitalWrite(BIN2, LOW);
 analogWrite(PWMA, 70);
 analogWrite(PWMB, 70);
 }
 applyBrakes();
 yaw += 80;
 orientation = 0.99 * yaw + (1 - 0.99) * accelRoll;
 delay(10);
 //fwd();
}

void turnLeft() {
 while (abs(orientation) < 75) {
 updateIMU();
 digitalWrite(AIN1, LOW);
 digitalWrite(AIN2, HIGH);
 digitalWrite(BIN1, LOW);
 digitalWrite(BIN2, HIGH);
 analogWrite(PWMA, 70);
 analogWrite(PWMB, 70);
 }
 applyBrakes();
 yaw -= 90;
 orientation = 0.99 * yaw + (1 - 0.99) * accelRoll;
 delay(10);
 //fwd();
}

void turn180(){
 while (abs(orientation) < 170) {
 updateIMU();
 digitalWrite(AIN1, LOW);
 digitalWrite(AIN2, HIGH);
 digitalWrite(BIN1, LOW);
 digitalWrite(BIN2, HIGH);
 analogWrite(PWMA, 70);
 analogWrite(PWMB, 70);
 }
 applyBrakes();
 yaw -= 170;
 orientation = 0.99 * yaw + (1 - 0.99) * accelRoll;
}

void applyBrakes() {
 // Active braking by short reverse pulse
 analogWrite(PWMA, 100);
 analogWrite(PWMB, 100);
 digitalWrite(AIN1, LOW);
 digitalWrite(AIN2, HIGH);
 digitalWrite(BIN1, HIGH);
 digitalWrite(BIN2, LOW);
 delay(10);
 stopMotors();
}

void moveForward(int leftSpeed, int rightSpeed) {
 digitalWrite(AIN1, HIGH);
 digitalWrite(AIN2, LOW);
 digitalWrite(BIN1, LOW);
 digitalWrite(BIN2, HIGH);
 analogWrite(PWMA, leftSpeed);
 analogWrite(PWMB, rightSpeed);
}

void stopMotors() {
 digitalWrite(AIN1, LOW);
 digitalWrite(AIN2, LOW);
 digitalWrite(BIN1, LOW);
 digitalWrite(BIN2, LOW);
 analogWrite(PWMA, 0);
 analogWrite(PWMB, 0);
 delay(20);
}

void wallStatus(int &sensorLeft, int &sensorRight, int &sensorFront) {
 int r = 0, l = 0, f = 0;
 int readingWithoutTx1, readingWithoutTx2, readingWithoutTx3;
 for (int i = 0; i < 5; i++) {
 digitalWrite(trigpinleft, LOW);
 digitalWrite(trigpinright, LOW);
 digitalWrite(trigpinfront, LOW);
 delayMicroseconds(2000);
 readingWithoutTx1 = analogRead(IR_left);
 readingWithoutTx2 = analogRead(IR_right);
 readingWithoutTx3 = analogRead(IR_front);
 digitalWrite(trigpinright, HIGH);
 digitalWrite(trigpinleft, HIGH);
 digitalWrite(trigpinfront, HIGH);
 delayMicroseconds(2000);
 l += analogRead(IR_left) - readingWithoutTx1;
 r += analogRead(IR_right) - readingWithoutTx2;
 f += analogRead(IR_front) - readingWithoutTx3;
 delay(10);
 }
 sensorLeft = l / 5;
 sensorRight = r / 5;
 sensorFront = f / 5;
 //Serial.print(sensorLeft);
 //Serial.print(". ");
 //Serial.print(sensorRight);
 //Serial.print(". ");
 //Serial.println(sensorFront);
}

//------------------------ Maze Floodfill Code ------------------------//

// Define a cell structure
class cell {
 public:
 int x, y;
 int score;
 int wall[4]; // 0: north, 1: south, 2: east, 3: west
 bool hit;
 int score2;
 cell(int _x = 0, int _y = 0, int _score = 1000,int score2_=-1) {
 x = _x;
 y = _y;
 score = _score;
 hit = false;
 score2=score2_;
 // Initialize walls to 0
 for (int i = 0; i < 4; i++) {
 wall[i] = 0;
 }
 }
};

cell dist[16][16];
cell o[16][16];
int leftwall=900,frontwall=1300,rightwall=1000;
int counter[2] = {0, 15}; // Example starting indices
int arr_size = 4;
cell tobechecked[257] ; // Preinitialize first element
int checkedelements = 0;
int WallNotForward=1300;//,wallNotRight=450,WallNotLeft=700;
int wallNotRight=1000;
int WallNotLeft=900;
int final[400];

void push(){
 for (int i=256;i>0;i--){
 tobechecked[i]=tobechecked[i-1];
 }

}
int bc = 0;

void floodfill() {
 // Initialize the tobechecked array with 4 starting cells
 tobechecked[0] = cell(2,13);
 dist[13][2].score = 0;
 
 dist[13][2].hit = true;
 checkedelements = 0; // Last valid index is 3

 // Mark starting cells in dist
 // tobechecked[0]=dist[8][7];
 // tobechecked[1]=dist[7][7];
 // tobechecked[2]=dist[8][8];
 // tobechecked[3]=dist[7][8];
 // dist[8][7].hit=true;
 // dist[8][7].score=0;
 // dist[7][7].hit=true;
 // dist[7][7].score=0;
 // dist[7][8].hit=true;
 // dist[7][8].score=0;
 // dist[8][8].hit=true;
 // dist[8][8].score=0;

 //Serial.println("floodfill1");

 // Process the floodfill queue
 while (checkedelements >= 0) {
 //Serial.println("floodfill2");

 cell pointer = tobechecked[checkedelements];
 // Shift the tobechecked array left

 tobechecked[checkedelements] = tobechecked[checkedelements+1];
 checkedelements--;
 // //Serial.println(pointer.x);

 // //Serial.println(pointer.y);

 
 if ( pointer.y>0 && !dist[pointer.y - 1][pointer.x].hit && dist[pointer.y][pointer.x].wall[0] == 0) {
 dist[pointer.y - 1][pointer.x].score = dist[pointer.y][pointer.x].score + 1;
 checkedelements++;


 push();
 tobechecked[0]=dist[pointer.y - 1][pointer.x];
 dist[pointer.y - 1][pointer.x].hit = true;
 //Serial.print("UP");

 // //Serial.print(pointer.y);
 // //Serial.print("|");
 // //Serial.print("0");
 // //Serial.print("|");

 // //Serial.println(pointer.x);

 }
 // South
 
 if (pointer.x<15 && !dist[pointer.y ][pointer.x+1].hit && dist[pointer.y][pointer.x].wall[1] == 0) {
 dist[pointer.y ][pointer.x+1].score = dist[pointer.y][pointer.x].score + 1;
 push();

 tobechecked[0]=dist[pointer.y ][pointer.x+1];
 checkedelements++;

 dist[pointer.y ][pointer.x+1].hit = true;
 //Serial.print("RIGHT");

 // //Serial.print(pointer.y);
 // //Serial.print("|");
 // //Serial.print("1");
 // //Serial.print("|");

 // //Serial.println(pointer.x);
 }
 // East
 
 if (pointer.y<15&& !dist[pointer.y+1][pointer.x ].hit && dist[pointer.y][pointer.x].wall[2] == 0) {
 dist[pointer.y+1][pointer.x ].score = dist[pointer.y][pointer.x].score + 1;
 push();
 tobechecked[0]=dist[pointer.y+1][pointer.x ];
 checkedelements++;

 dist[pointer.y+1][pointer.x ].hit = true;
 //Serial.print("down");
 // //Serial.print(pointer.y);
 // //Serial.print("|");
 // //Serial.print("2");
 // //Serial.print("|");

 // //Serial.println(pointer.x);
 }
 // West
 if ( pointer.x>0 && !dist[pointer.y][pointer.x - 1].hit && dist[pointer.y][pointer.x].wall[3] == 0) {
 dist[pointer.y][pointer.x - 1].score = dist[pointer.y][pointer.x].score + 1;
 push();
 checkedelements++;

 tobechecked[0]= dist[pointer.y][pointer.x - 1];
 dist[pointer.y][pointer.x - 1].hit = true;
 //Serial.print("LEFT");

 // //Serial.print(pointer.y);
 // //Serial.print("|");
 // //Serial.print("3");
 // //Serial.print("|");

 // //Serial.println(pointer.x);

 }
 }
 
 // Reset hit flags for future floodfill runs
 for (int i = 0; i < 16; i++) {
 for (int j = 0; j < 16; j++) {
 dist[i][j].hit = false;

 }
 }
}

void finalRun() {
  for (int i=0;i<400;i++){
    
Serial.print(final_track[i][0]);
Serial.print("|");
Serial.println(final_track[i][1]);
  }
  
  turnspeedhigh = 180;
  turnspeedlow = 120;
  fwdspeed = 210;
 for (int i=0;i<10;i++){
 digitalWrite(2,HIGH);
 delay(100);
 digitalWrite(2,LOW);
 delay(100);
 }
 int i = 0;
while(i<=step){
 
 int z = 0;
 if (final[i]==2)break;
//  if (i>step) break;
 while(final[i] == 0){
 z++;
 i++;
 }

 for(int w=0; w < z; w++){
 fwd();
 } 
 if(final[i]==1){
 turnRight();
 fwd();
 }
 if(final[i]==-1){
 turnLeft();
 fwd();
 }
 i++;
 }
}
//------------------------ Setup and Main Loop ------------------------//

void setup() {
 // Setup sensor pins
 pinMode(trigpinleft, OUTPUT);
 pinMode(IR_left, INPUT);
 pinMode(trigpinright, OUTPUT);
 pinMode(IR_right, INPUT);
 pinMode(trigpinfront, OUTPUT);
 pinMode(IR_front, INPUT);
 //Serial.begin(115200);
 pinMode(buttonPin, INPUT_PULLUP);
 // Setup motor pins
 pinMode(AIN1, OUTPUT);
 pinMode(AIN2, OUTPUT);
 pinMode(PWMA, OUTPUT);
 pinMode(BIN1, OUTPUT);
 pinMode(BIN2, OUTPUT);
 pinMode(PWMB, OUTPUT);
 pinMode(C1, INPUT);
 pinMode(2, OUTPUT);

 Wire.begin();
 mpu.initialize();
 Serial.begin(115200);
 attachInterrupt(digitalPinToInterrupt(C1), increment, RISING);
for (int i = 0; i < 16; i++) {
 for (int j = 0; j < 16; j++) {
 dist[i][j].x = j;
 dist[i][j].y = i;

 }
 }

 // Initialize floodfill maze (for example, set walls on the boundary)
 
 floodfill();
 for (int i = 0; i < 16; i++) {
 dist[0][i].wall[0] = 1; // Top row: north wall
 dist[i][0].wall[3] = 1; // Left column: west wall
 }


 



 for (int i=0; i<16;i++){
 for (int j=0; j<16;j++){
 //Serial.print(dist[15-i][j].score);
 //Serial.print("|");
 }
 //Serial.println("");
 

 }
}
void backtrack(){

  int zplace[2]={0,15};
  int z=-10;
  int tracker[2]={0,15};
  
  while (dist[tracker[1] ][tracker[0]].score!=0){
     z=-10; 
     final_track[step][0]=zplace[0];
    final_track[step][1]=zplace[1];
    if ( tracker[1]>0 && dist[tracker[1] - 1][tracker[0]].score2>=0 && dist[tracker[1]][tracker[0]].wall[0] == 0) {
      if (dist[tracker[1] - 1][tracker[0]].score2>z){
        z=dist[tracker[1] - 1][tracker[0]].score2;
        zplace[0] = tracker[0];
        zplace[1] = tracker[1]-1;
  
          
        }
      }
      
        if (tracker[0]<15 && dist[tracker[1] ][tracker[0]+1].score2>=0 && dist[tracker[1]][tracker[0]].wall[1] == 0) {
          if  (dist[tracker[1] ][tracker[0]+1].score2>z){
            z=dist[tracker[1] ][tracker[0]+1].score2;
            zplace[0] = tracker[0]+1;
            zplace[1] = tracker[1]; 
            
        }
      }
      if (tracker[1]<15 && dist[tracker[1]+1][tracker[0] ].score2>=0 && dist[tracker[1]][tracker[0]].wall[2] == 0) {
        if  (dist[tracker[1]+1][tracker[0]].score2>z){
          z=dist[tracker[1]+1 ][tracker[0]].score2;
          zplace[0] = tracker[0];
          zplace[1] = tracker[1]+1;
  
          
      }
  }
  if (tracker[0]>0 && dist[tracker[1]][tracker[0] -1].score2>=0 && dist[tracker[1]][tracker[0]].wall[3] == 0) {
    if  (dist[tracker[1]][tracker[0]-1].score2>z){
      z=dist[tracker[1] ][tracker[0]-1].score2;
      zplace[0] = tracker[0]-1;
      zplace[1] = tracker[1];
  
      
  }
  }
  tracker[0] = zplace[0];
  tracker[1] = zplace[1];
  // final_track[step][0]=zplace[0];
  // final_track[step][1]=zplace[1];
  step++;
  
  }
  final_track[step][0]=zplace[0];
  final_track[step][1]=zplace[1];

  int forien=0;
  
  for (int i=0;i<step;i++){
    if (forien<0){
    forien+=360;}
    else if (forien>270){
    forien=forien%360;}
  if (forien==0){
      if (final_track[i][0]==final_track[i+1][0]){
          //fwd();
          final[i] = 0;
      }
      else if(final_track[i][1]==final_track[i+1][1] && final_track[i][0]<final_track[i+1][0]){
          //"turnRight();
          final[i] = 1;
          forien+=90;
      }
      else if(final_track[i][1]==final_track[i+1][1] && final_track[i][0]>final_track[i+1][0]){
         // turnLeft();
          final[i] = -1;
          forien-=90;
      }
  
  }else if (forien==180){
      if (final_track[i][0]==final_track[i+1][0]){
        //fwd();
          final[i] = 0;
      }
      else if (final_track[i][1]==final_track[i+1][1] && final_track[i][0]<final_track[i+1][0]){
          //turnLeft();
          final[i] = -1;
          forien-=90;
      }
      else if (final_track[i][1]==final_track[i+1][1] && final_track[i][0]>final_track[i+1][0]){
          //turnRight();
          final[i] = 1;
          forien+=90;
      }
  
  }
  else if (forien==90){
      if (final_track[i][1]==final_track[i+1][1]){
         // fwd();
          final[i] = 0;
      }
      else if (final_track[i][0]==final_track[i+1][0] && final_track[i][1]<final_track[i+1][1]){
          //turnRight();
          final[i] = 1;
                  forien+=90;
  
      }
      else if (final_track[i][0]==final_track[i+1][0] && final_track[i][1]>final_track[i+1][1]){
          //turnLeft();
          final[i] = -1;
          forien-=90;
  
      }
  
  }
  else if (forien==270){
      if (final_track[i][1]==final_track[i+1][1]){
          //fwd();
          final[i] = 0;
      }
      else if (final_track[i][0]==final_track[i+1][0] && final_track[i][1]<final_track[i+1][1]){
          //turnLeft();
          final[i] = -1;
          forien-=90;
  
      }
      else if (final_track[i][0]==final_track[i+1][0] && final_track[i][1]>final_track[i+1][1]){
        //turnRight();
          final[i] = 1;
          forien+=90;
  
      }
  
  }
  }
  final[step]=2;
}



void quit(){

 digitalWrite(2, HIGH);
 delay(1000);
 digitalWrite(2, LOW);
 delay(1000);
backtrack();
// if leg{
//  backtrack();

// }else{

// }


 digitalWrite(2, HIGH);
 delay(2000);
 digitalWrite(2, LOW);
 
 }
// while(1) {
// for (int i=0; i<16;i++){
// for (int j=0; j<16;j++){
// Serial.print(dist[i][j].score);
// Serial.print("|");
// }
// Serial.println("");
 

// }
// for (int i=0; i<16;i++){
// for (int j=0; j<16;j++){
// for (int k=0 ;k<4;k++){
// Serial.print(dist[i][j].wall[k]);
// Serial.print(",");
// }
// Serial.print("|");
// }
// Serial.println("");
 

// }}
 

bool once = true;

void loop() {
 // Example (commented-out) IMU update code
 // unsigned long currentTime = millis();
 // float dt = (currentTime - prevTime) / 1000.0;
 // prevTime = currentTime;
 // gyroZ = mpu.getRotationZ() / 131.0;
 // if (gyroZ < 1 && gyroZ > -1) gyroZ = 0;
 // accelX = mpu.getAccelerationX() / 16384.0;
 // accelY = mpu.getAccelerationY() / 16384.0;
 // accelZ = mpu.getAccelerationZ() / 16384.0;
 // float accelRoll = atan2(-accelX, accelZ) * 180 / PI;
 // yaw += gyroZ * dt;
 // orientation = 0.98 * yaw + (1 - 0.98) * accelRoll;
 int buttonState = digitalRead(buttonPin); // Read the state of the button
 
 // Check if the button is pressed (active low)
 if (buttonState == LOW){
 digitalWrite(2,1);
 delay(1000);
 digitalWrite(2,LOW);
 delay(1000);
//  for (int i=0;i<400;i++){
//  Serial.print(final[i]);
//  Serial.print("|");
 

//  }
//  for (int i=0;i<400;i++){
//  Serial.print(final_track[i][0]);
//  Serial.print("|");
//  Serial.println(final_track[i][1]);

//  }
 Serial.println("");
 finalRun();}
 
while ( once ){
 dist[counter[1]][counter[0]].score2=bc;
 bc++;

 cvalue = dist[counter[1]][counter[0]].score;
 // for (int i=0; i<16;i++){
 // for (int j=0; j<16;j++){
 // Serial.print(dist[i][j].score);
 // Serial.print("|");
 // }
 // Serial.println("");
 

 // }
// for (int i=0; i<16;i++){
// for (int j=0; j<16;j++){
// for (int k=0 ;k<4;k++){
// Serial.print(dist[i][j].wall[k]);
// Serial.print(",");
// }
// Serial.print("|");
// }
// Serial.println("");
 

// }
 if (target_orientation > 270) {
 target_orientation = target_orientation % 360;
 } else if (target_orientation < 0) {
 target_orientation += 360;
 }
 Serial.println(cvalue);
 wallStatus(wl, wr, wf);
 if (cvalue == 0 && once==true) {
 quit();
 once = false;
 }
 // Set walls based on target orientation and sensor thresholds
 if ((target_orientation == 180 && wl > leftwall) || 
 (target_orientation == 90 && wf > frontwall) || 
 (target_orientation == 0 && wr > rightwall)) {
 //Serial.println("right");

 dist[counter[1]][counter[0]].wall[1] = 1;
 
 try {
 dist[counter[1] ][counter[0]+1].wall[3] = 1; // Mark the north wall of the cell above
 }catch(...){
 //Serial.println("error aa raha hai");
 }
 floodfill();
 }
 if ((target_orientation == 90 && wl > leftwall) || 
 (target_orientation == 0 && wf > frontwall) || 
 (target_orientation == 270 && wr > rightwall)) { 
 dist[counter[1]][counter[0]].wall[0] = 1;
 try {
 dist[counter[1] - 1][counter[0]].wall[2] = 1; // Mark the north wall of the cell above
 }catch(...){
 }
 floodfill();

 
 }
 if ((target_orientation == 270 && wl > leftwall) || 
 (target_orientation == 180 && wf > frontwall) || 
 (target_orientation == 90 && wr > rightwall)) { 
 dist[counter[1]][counter[0]].wall[2] = 1;
 try {
 dist[counter[1] + 1][counter[0]].wall[0] = 1;
 }catch(...){
 }
 floodfill();

 }
 if ((target_orientation == 0 && wl > leftwall) || 
 (target_orientation == 270 && wf > frontwall) || 
 (target_orientation == 180 && wr > rightwall)) { 
 dist[counter[1]][counter[0]].wall[3] = 1;
 try {
 dist[counter[1] ][counter[0]-1].wall[1] = 1;
 }catch(...){

 }
 floodfill();

 }
 
 // Decide next move based on sensor thresholds and floodfill score
 if (wf < WallNotForward) {
 if (target_orientation == 0 && dist[counter[1]-1][counter[0]].score<=cvalue) {
 counter[1] -= 1;
 fwd();
 continue;
 } else if (target_orientation == 90 && dist[counter[1]][counter[0]+1].score<=cvalue) {
 counter[0] += 1;
 fwd();
 continue;
 } else if (target_orientation == 180 && dist[counter[1]+1][counter[0]].score<=cvalue) {
 counter[1] += 1;
 fwd();
 continue;
 } else if (target_orientation == 270 && dist[counter[1]][counter[0]-1].score<=cvalue) {
 counter[0] -= 1;
 fwd();
 continue;
 }
 }
 if (wl < WallNotLeft) {
 if (target_orientation == 90 && dist[counter[1] - 1][counter[0]].score <= cvalue) {
 counter[1] -= 1;
 turnLeft();
 fwd();
 target_orientation -= 90;
 continue;
 } else if (target_orientation == 180 && dist[counter[1]][counter[0] + 1].score <= cvalue) {
 counter[0] += 1;
 turnLeft();
 fwd(); 
 target_orientation -= 90;
 continue;
 } else if (target_orientation == 270 && dist[counter[1] + 1][counter[0]].score <= cvalue) {
 counter[1] += 1;
 turnLeft();
 fwd();
 target_orientation -= 90;
 continue;
 } else if (target_orientation == 0 && dist[counter[1]][counter[0] - 1].score <= cvalue) {
 counter[0] -= 1;
 turnLeft();
 fwd();
 target_orientation -= 90;
 continue;
 }
 }
 if (wr < wallNotRight) {
 if (target_orientation == 0 &&dist[counter[1]][counter[0]+1].score<=cvalue) {
 counter[0]+=1;
 turnRight();
 fwd();
 target_orientation += 90;
 continue;
 } else if (target_orientation == 90 && dist[counter[1]+1][counter[0]].score<=cvalue) {
 counter[1]+=1;
 turnRight();
 fwd();
 target_orientation += 90;
 continue;
 } else if (target_orientation == 180 && dist[counter[1]][counter[0]-1].score<=cvalue) {
 counter[0]-=1;
 turnRight();
 fwd();
 target_orientation += 90;
 continue;
 } else if (target_orientation == 270 && dist[counter[1]-1][counter[0]].score<=cvalue) {
 counter[1] -= 1;
 turnRight();
 fwd();
 target_orientation += 90;
 continue;
 }
 }
 if (wf>frontwall && wr>rightwall && wl>leftwall ){
 if ( target_orientation==270 && dist[counter[1]][counter[0]+1].score<=cvalue){
 counter[0]+=1;
 turn180();
 fwd();
 target_orientation=90;
 continue;
 }else if (target_orientation==0 && dist[counter[1]][counter[0]-1].score<=cvalue){
 counter[0]-=1;
 turn180();
 fwd();
 target_orientation=180;
 continue;
 }
 else if (target_orientation==90 && dist[counter[1]][counter[0]-1].score<=cvalue){
 counter[0]-=1;
 turn180();
 fwd();
 target_orientation=270;
 continue;
 }else if(target_orientation==180 && dist[counter[1]-1][counter[0]].score<=cvalue){
 counter[1]-=1;
 turn180();
 fwd();
 target_orientation=0;
 continue;
 }
}
}
}
