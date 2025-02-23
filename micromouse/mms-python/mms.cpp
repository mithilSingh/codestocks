

#include <Wire.h>
#include <MPU6050.h>

#define PWMA 32
#define AIN1 25
#define AIN2 33
#define PWMB 14
#define BIN1 26
#define BIN2 27
#define STBY 4
#define C1 18
#define C2 19

#define trigpinleft 16
#define trigpinright 17
#define trigpinfront 4

#define IR_left 34
#define IR_right 35
#define IR_front 36

#include <WiFi.h>

const char* ssid = "ESP32_AP";   // WiFi AP Name
const char* password = "12345678";  // WiFi Password (8+ characters)

WiFiServer server(80);  // TCP Server on port 80


MPU6050 mpu;

float gyroZ, accelX, accelY, accelZ;
const float alpha = 0.99;
float accelRoll;
unsigned long prevTime;
float yaw = 0.0;
double val = 18 / (3.141 * 3.2);
double count = 0;
float orientation = 0.0;
int turns = 0;
int wl, wr,wf;

void setup() {
    pinMode(trigpinleft, OUTPUT);
    pinMode(IR_left, INPUT);
    pinMode(trigpinright, OUTPUT);
    pinMode(IR_right, INPUT);
    pinMode(trigpinfront, OUTPUT);
    pinMode(IR_front, INPUT);
    Serial.begin(115200);

    pinMode(AIN1, OUTPUT);
    pinMode(AIN2, OUTPUT);
    pinMode(PWMA, OUTPUT);
    pinMode(BIN1, OUTPUT);
    pinMode(BIN2, OUTPUT);
    pinMode(PWMB, OUTPUT);
    pinMode(STBY, OUTPUT);
    pinMode(C1, INPUT);
    pinMode(2, OUTPUT);

    Wire.begin();
    mpu.initialize();

    digitalWrite(STBY, HIGH); // Enable the motor driver
    attachInterrupt(digitalPinToInterrupt(C1), increment, RISING);
    WiFi.softAP(ssid, password);
    Serial.println("ESP32 AP Started");
    Serial.print("IP Address: ");
    Serial.println(WiFi.softAPIP());

    server.begin();
    // Start Access Point (AP Mode)
    

}

void fwd() {
    count = 0;
    int x;
    while (count / 700 < val) {
        updateIMU();
        x++;
        if(x % 20 == 0){
          wallStatus(wl, wr, wf);
          if(wr>400 && wl>1000){
          yaw+=(wl-wr)/1000*1.5;
          orientation = alpha * yaw + (1 - alpha) * accelRoll;

        }}


        if (abs(orientation) < 2) {
            moveForward(125, 125);
        } else if (orientation < -2) {
            moveForward(50, 120); // Correcting towards right
        } else if (orientation > 2) {
            moveForward(120, 50); // Correcting towards left
        }
    }
    applyBrakes();
}
void fwdhalf() {
    count = 0;
    while (count / 700 < (val+2)/2) {
        updateIMU();

        if (abs(orientation) < 2) {
            moveForward(125, 125);
        } else if (orientation < -2) {
            moveForward(50, 120); // Correcting towards right
        } else if (orientation > 2) {
            moveForward(120, 50); // Correcting towards left
        }
    }
    //applyBrakes();
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
    orientation = alpha * yaw + (1 - alpha) * accelRoll;
}

void turnRight() {
   

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
    yaw+=75;
    orientation = alpha * yaw + (1 - alpha) * accelRoll;

    delay(10);
    fwd();
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
    yaw-=75;
    orientation = alpha * yaw + (1 - alpha) * accelRoll;

    delay(10);
    fwd();

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
    yaw-=170;
    orientation = alpha * yaw + (1 - alpha) * accelRoll;


    fwd();
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
    Serial.print(sensorLeft);
    Serial.print(".  ");
    Serial.print(sensorRight);
    Serial.print(".  ");
    Serial.println(sensorFront);
}

void loop() {
    
    // yaw+=(wl-wr)/1000*1.5;
    // orientation = alpha * yaw + (1 - alpha) * accelRoll;
    // if (wl > 1600 && wr > 1800 && wf > 150) {
    //     turn180();
    //     orientation = alpha * yaw + (1 - alpha) * accelRoll;       
    // } 
    // else if (wl < 400 && wr < 150 && wf < 20) {
    //     stopMotors();
    // } 
   
    // else if (wl > 500 && wr < 500 && wf >150) {
    //     turnRight();
    //     orientation = alpha * yaw + (1 - alpha) * accelRoll;
    // } else if (wr > 500 && wl < 1600 && wf>150 ) {
    //     turnLeft();
    //     orientation = alpha * yaw + (1 - alpha) * accelRoll;
    // } else {
    //     digitalWrite(2, HIGH);
    //     fwd();
    //     digitalWrite(2, LOW);

    // }
    WiFiClient client = server.available();  // Wait for a client

    if (client) {
        Serial.println("Client Connected!");

        while (client.connected()) {
            String dataToSend = "  " + String(orientation)+ "  " +String(wl)+"  " + String(wf)+ "  " +String(wr);

            client.print(dataToSend);  // Send data
            Serial.println("Sent: " + dataToSend);
            wallStatus(wl, wr, wf);
            updateIMU();
            yaw+=(wl-wr)/1000*1.5;            
            // if( (wl-wr)/1000>2){
            //   updateIMU();
            //   digitalWrite(AIN1, HIGH);
            //   digitalWrite(AIN2, LOW);
            //   digitalWrite(BIN1, HIGH);
            //   digitalWrite(BIN2, LOW);
            //   analogWrite(PWMA, 100);
            //   analogWrite(PWMB, 100);
            //   delay(100);
            //    stopMotors() ;
            // }
            // if( (wl-wr)/1000>){
            //   updateIMU();
            //   digitalWrite(AIN1, LOW);
            //   digitalWrite(AIN2, HIGH);
            //   digitalWrite(BIN1, LOW);
            //   digitalWrite(BIN2, HIGH);
            //   analogWrite(PWMA, 100);
            //   analogWrite(PWMB, 100);
            //   delay(100);
            //    stopMotors() ;
            // }
            orientation = alpha * yaw + (1 - alpha) * accelRoll;
            if (wl > 1800 && wr > 1600 && wf > 1200) {
                turn180();
                orientation = alpha * yaw + (1 - alpha) * accelRoll;       
            } 
            else if (wl < 400 && wr < 150 && wf < 20) {
                stopMotors();
            } 
          
            else if (wl > 400 && wr < 780 && wf >1200) {
                turnRight();
                orientation = alpha * yaw + (1 - alpha) * accelRoll;
            } else if (wr > 700 && wl < 1800 && wf>1200 ) {
                turnLeft();
                orientation = alpha * yaw + (1 - alpha) * accelRoll;
            } else {
                digitalWrite(2, HIGH);
                fwd();
                digitalWrite(2, LOW);

            }
            
        }
            Serial.println("clint disconnected");

        client.stop();  // Close connection
    }
  delay(100);
}
// #include <Wire.h>
// #include <MPU6050.h>

// #define PWMA 32
// #define AIN1 25
// #define AIN2 33
// #define PWMB 14
// #define BIN1 26
// #define BIN2 27
// #define STBY 4
// #define C1 18
// #define C2 19

// #define trigpinleft 16
// #define trigpinright 17
// #define trigpinfront 4

// #define IR_left 34
// #define IR_right 35
// #define IR_front 36

// MPU6050 mpu;

// float gyroZ, accelX, accelY, accelZ;
// const float alpha = 0.98;
// float accelRoll;
// unsigned long prevTime;
// float yaw = 0.0;
// double val = 18 / (3.141 * 3.2);
// double count = 0;
// float orientation = 0.0;
// int wl, wr, wf;
// float gyroBias = 0.0;
// float Kp = 1.2; // PID proportional gain

// void setup() {
//     Serial.begin(115200);
//     Wire.begin();
//     mpu.initialize();
//     calibrateGyro();

//     pinMode(AIN1, OUTPUT);
//     pinMode(AIN2, OUTPUT);
//     pinMode(PWMA, OUTPUT);
//     pinMode(BIN1, OUTPUT);
//     pinMode(BIN2, OUTPUT);
//     pinMode(PWMB, OUTPUT);
//     pinMode(STBY, OUTPUT);
//     pinMode(C1, INPUT);
//     pinMode(2, OUTPUT);
    
//     digitalWrite(STBY, HIGH);
//     attachInterrupt(digitalPinToInterrupt(C1), increment, RISING);
// }
// void increment() {
//     count++;
// }
// void calibrateGyro() {
//     float sum = 0;
//     for (int i = 0; i < 100; i++) {
//         sum += mpu.getRotationZ();
//         delay(10);
//     }
//     gyroBias = sum / 100.0;
// }

// void updateIMU() {
//     unsigned long currentTime = millis();
//     float dt = (currentTime - prevTime) / 1000.0;
//     prevTime = currentTime;

//     gyroZ = (mpu.getRotationZ() - gyroBias) / 131.0;
//     if (abs(gyroZ) < 1) gyroZ = 0;

//     yaw += gyroZ * dt;
//     orientation = alpha * yaw + (1 - alpha) * accelRoll;
// }

// void fwd() {
//     count = 0;
//     while (count / 700 < val) {
//         updateIMU();
//         float correction = constrain(Kp * -orientation, -30, 30);
//         moveForward(100 + correction, 100 - correction);
//     }
//     applyBrakes();
// }

// void turnRight() {
//     float targetYaw = yaw + 90;
//     while (yaw < targetYaw) {
//         updateIMU();
//         float error = targetYaw - yaw;
//         int turnSpeed = constrain(Kp * error, 40, 100);
//         moveForward(turnSpeed, turnSpeed);
//     }
//     applyBrakes();
// }

// void turnLeft() {
//     float targetYaw = yaw - 90;
//     while (yaw > targetYaw) {
//         updateIMU();
//         float error = targetYaw - yaw;
//         int turnSpeed = constrain(Kp * -error, 40, 100);
//         moveForward(turnSpeed, turnSpeed);
//     }
//     applyBrakes();
// }

// void applyBrakes() {
//     int brakeTime = map(abs(gyroZ), 0, 100, 10, 40);
//     analogWrite(PWMA, 100);
//     analogWrite(PWMB, 100);
//     delay(brakeTime);
//     stopMotors();
// }

// void moveForward(int leftSpeed, int rightSpeed) {
//     digitalWrite(AIN1, HIGH);
//     digitalWrite(AIN2, LOW);
//     digitalWrite(BIN1, LOW);
//     digitalWrite(BIN2, HIGH);
//     analogWrite(PWMA, leftSpeed);
//     analogWrite(PWMB, rightSpeed);
// }

// void stopMotors() {
//     digitalWrite(AIN1, LOW);
//     digitalWrite(AIN2, LOW);
//     digitalWrite(BIN1, LOW);
//     digitalWrite(BIN2, LOW);
//     analogWrite(PWMA, 0);
//     analogWrite(PWMB, 0);
// }

// int avgSensor(int pin) {
//     int sum = 0;
//     for (int i = 0; i < 5; i++) {
//         sum += analogRead(pin);
//         delay(5);
//     }
//     return sum / 5;
// }

// void wallStatus(int &sensorLeft, int &sensorRight, int &sensorFront) {
//     sensorLeft = avgSensor(IR_left);
//     sensorRight = avgSensor(IR_right);
//     sensorFront = avgSensor(IR_front);
//     Serial.print(sensorLeft);
//     Serial.print(".  ");
//     Serial.print(sensorRight);
//     Serial.print(".  ");
//     Serial.println(sensorFront);
// }

// void loop() {
//     wallStatus(wl, wr, wf);
//     yaw += (wl - wr) / 1000.0 * 1.5;
//     orientation = alpha * yaw + (1 - alpha) * accelRoll;

//     if (wl > 1600 && wr > 1800 && wf > 150) {
//         turn180();
//         orientation = alpha * yaw + (1 - alpha) * accelRoll;       
//     } 
//     else if (wl < 400 && wr < 150 && wf < 20) {
//         stopMotors();
//     } 
   
//     else if (wl > 500 && wr < 500 && wf >150) {
//         turnRight();
//         orientation = alpha * yaw + (1 - alpha) * accelRoll;
//     } else if (wr > 500 && wl < 1600 && wf>150 ) {
//         turnLeft();
//         orientation = alpha * yaw + (1 - alpha) * accelRoll;
//     } else {
//         digitalWrite(2, HIGH);
//         fwd();
//         digitalWrite(2, LOW);

//     }
// }
