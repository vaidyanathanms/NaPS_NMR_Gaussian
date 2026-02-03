! To optimize the structure
%mem=24GB
%chk=optim.chk
#p UB3LYP/6-31+G(2df,p) opt=(CalcAll,maxcycle=200,maxstep=10,maxEstep=300) scrf=(pcm,solvent=Water) pop=reg freq nmr

Structure of e6_P2S8_q2m_endScharge

-2  1
P -3.888162 -1.185950 -1.187122
S -3.208969 0.707813 -0.409873
S -4.789820 -0.842299 -2.668503
S -1.945510 -1.974544 -1.697842
P -1.262701 -0.114786 -0.842457
S -5.010050 -2.312618 0.274078
S -4.776621 -4.134730 -0.801873
S -0.549201 0.887836 -2.111804
S -0.036449 -0.283433 0.927001
S 1.297311 -1.656618 -0.004501

