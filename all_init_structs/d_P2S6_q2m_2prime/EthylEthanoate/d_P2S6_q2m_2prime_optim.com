! To optimize the structure
%mem=24GB
%chk=optim.chk
#p UB3LYP/6-31+G(2df,p) opt=(CalcAll,maxcycle=200,maxstep=10,maxEstep=300) scrf=(pcm,solvent=EthylEthanoate) pop=reg freq nmr

Structure of d_P2S6_q2m_2prime

-1  1
P -2.691600 0.830485 0.022587
S -1.477082 -0.844163 -0.373752
S -2.084889 1.844501 -1.721046
P -1.356953 -0.040097 -2.316850
S -2.275946 1.767210 1.704404
S -1.916516 -1.676746 -3.714259
S 0.456371 -0.015062 -3.084940
S -4.614517 0.493165 0.216921

