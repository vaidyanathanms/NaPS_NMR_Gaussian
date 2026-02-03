! To optimize the structure
%mem=24GB
%chk=optim.chk
#p UB3LYP/6-31+G(2df,p) opt=(CalcAll,maxcycle=200,maxstep=10,maxEstep=300) scrf=(pcm,solvent=Water) pop=reg freq nmr

Structure of e7_P2S8_q2m_endScharge

-2  1
P -3.899211 -1.185075 -1.144473
S -3.285802 0.681515 -0.255490
S -4.750594 -0.787588 -2.642056
S -1.923900 -1.915871 -1.615338
P -1.308561 -0.087630 -0.651173
S -5.054735 -2.396623 0.219338
S -4.752305 -4.161604 -0.932018
S -0.527293 0.908337 -1.885383
S -0.073559 -0.455600 1.081581
S -0.385913 1.506232 1.847017

