! To optimize the structure
%mem=24GB
%chk=optim.chk
#p UB3LYP/6-31+G(2df,p) opt=(CalcAll,maxcycle=200,maxstep=10,maxEstep=300) scrf=(pcm,solvent=Water) pop=reg freq nmr

Structure of g_P2S6_q2m_1PendStrans

10  1
P -3.085403 1.507597 0.000000
P -0.870415 1.491409 -0.000000
S -4.380412 3.259441 -0.000000
S -6.226285 2.181927 0.000000
S -3.831763 -0.093257 -0.000000
S 0.374976 -0.294976 0.000000
S 2.248955 0.729108 -0.000000
S -0.093763 3.078420 0.000000

