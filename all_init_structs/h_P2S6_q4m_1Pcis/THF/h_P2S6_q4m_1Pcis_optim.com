! To optimize the structure
%mem=24GB
%chk=optim.chk
#p UB3LYP/6-31+G(2df,p) opt=(CalcAll,maxcycle=200,maxstep=10,maxEstep=300) scrf=(pcm,solvent=THF) pop=reg freq nmr

Structure of h_P2S6_q4m_1Pcis

-4  1
P -4.598552 0.638134 0.256870
P -2.467116 0.859295 -0.256733
S -5.439607 2.023363 -0.450719
S -5.462422 -1.123382 -0.638976
S -4.939640 0.728006 2.385081
S -1.925124 2.381469 0.461699
S -2.153081 1.032426 -2.383964
S -1.262065 -0.696043 0.626741

