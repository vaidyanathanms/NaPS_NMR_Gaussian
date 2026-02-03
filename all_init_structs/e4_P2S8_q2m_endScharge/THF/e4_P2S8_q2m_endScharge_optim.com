! To optimize the structure
%mem=24GB
%chk=optim.chk
#p UB3LYP/6-31+G(2df,p) opt=(CalcAll,maxcycle=200,maxstep=10,maxEstep=300) scrf=(pcm,solvent=THF) pop=reg freq nmr

Structure of e4_P2S8_q2m_endScharge

-2  1
P -4.012488 -1.067220 -1.271985
S -3.341018 0.802409 -0.432739
S -4.904870 -0.678776 -2.747913
S -2.065260 -1.837811 -1.793645
P -1.390072 -0.005393 -0.878721
S -5.143090 -2.238321 0.146934
S -4.906073 -4.025581 -0.985215
S -0.632807 0.958375 -2.152811
S -0.106309 -0.367062 0.819578
S -0.362405 1.611236 1.563213

