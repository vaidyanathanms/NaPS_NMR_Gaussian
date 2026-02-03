! To optimize the structure
%mem=24GB
%chk=optim.chk
#p UB3LYP/6-31+G(2df,p) opt=(CalcAll,maxcycle=200,maxstep=10,maxEstep=300) scrf=(pcm,solvent=Water) pop=reg freq nmr

Structure of f_P2S7_q4m_cis

-4  1
P -3.998552 0.283283 -0.032871
P -0.750365 0.787230 -0.173899
S -4.021458 2.050727 0.043800
S -0.668597 2.362822 -0.972556
S -4.081391 -0.477560 1.985505
S -5.817712 -0.213072 -1.080103
S 1.193377 -0.086359 -0.507167
S -1.031937 1.165440 1.933509
S -2.281983 -0.368158 -1.196218

