! To optimize the structure
%mem=24GB
%chk=optim.chk
#p UB3LYP/6-31+G(2df,p) opt=(CalcAll,maxcycle=200,maxstep=10,maxEstep=300) scrf=(pcm,solvent=THF) pop=reg freq nmr

Structure of j_P2S6_q2m_2primetrans

-2  1
P -2.905995 1.497412 -0.793928
P -0.353919 1.155611 0.797625
S -1.038081 2.571208 -0.680407
S -2.209732 0.063104 0.659725
S -5.794192 2.385855 -0.171246
S -3.876694 2.739070 0.680200
S 0.655202 -0.087542 -0.648612
S 2.564605 0.395153 0.156642

