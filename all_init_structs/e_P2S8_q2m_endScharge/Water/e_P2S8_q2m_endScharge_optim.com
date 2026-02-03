! To optimize the structure
%mem=24GB
%chk=optim.chk
#p UB3LYP/6-31+G(2df,p) opt=(CalcAll,maxcycle=200,maxstep=10,maxEstep=300) scrf=(pcm,solvent=Water) pop=reg freq nmr

Structure of e_P2S8_q2m_endScharge

-2  1
P -2.817229 0.681809 0.537107
S -1.635682 -0.484544 -0.835119
S -1.703812 1.747160 1.402560
S -3.358217 -0.908493 1.884668
P -2.345303 -2.109483 0.401472
S -4.465076 1.767551 -0.339794
S -5.256403 0.020957 -1.264728
S -2.949601 -3.440356 1.396435
S -1.224607 -3.189243 -1.095063
S 0.476486 -3.379175 0.173309

