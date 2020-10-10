import random as r

a="Q Write down the definition of cell. ///Q  Who wrote micrographia?///Q \"Omnis cellula e cellulae\". Explain the statement.///Q Who gave the cell theory ? What does it state ? Which organism is an exception of cell theory ?///Q Define prokaryotic cell.///Q Give one example of dedifferentiated cell.///Q Give one-one example of spindle shape cell,discoidal and branched cell.///Q Write down the name of largest plant cell.///Q Write down the name of smallest cell of human body.///Q Define protoplast.///q What is the composition of protoplasm ?///Q Who gave the fluid mosaic model of plasma membrane ?///Q What is osmosis ?///Q Which cell organelle is called as the head quarter of cell ? ///Q What is the difference between diffusion and osmosis ?///Q Why plasma membrane is called as selectively permeable membrane ? ///Q Draw a neat and labelled diagram of nucleus. State it's main functions.///Q  State any two functions of golgi body. ///Q Describe  the  types  of  endoplasmic  reticulum  and  draw  necessary  figure.  Give  it's  main  functions also. ///Q Which organelle controls osmotic pressure in a cell ? ///Q State any two functions of golgi body. ///Q State the main functions of lysosomes///Q Write down name of the all parts of microscope.///Q How we can prepare microscopic slide explain."
p=a.split("///")
pi=open("Questionbank.txt","w")
pi.write(" ")
for i in range(24):
    rc=r.choice(p)
    pi=open("Questionbank.txt","a")
    pi.write(rc+"\n")
    k=p.index(rc)
    p.pop(k)
    


pi=open("Qestionbank.txt","r")
print(pi.read())