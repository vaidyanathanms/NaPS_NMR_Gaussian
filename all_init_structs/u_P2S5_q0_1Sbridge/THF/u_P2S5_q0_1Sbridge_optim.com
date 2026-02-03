! To optimize the structure
%mem=24GB
%chk=optim.chk
#p UB3LYP/6-31+G(2df,p) opt=(CalcAll,maxcycle=200,maxstep=10,maxEstep=300) scrf=(pcm,solvent=THF) pop=reg freq nmr

Structure of u_P2S5_q0_1Sbridge

0  1
P -1.727519 0.479719 0.581945
P 1.369452 0.494939 0.698319
S -0.128861 1.015868 -0.761886
S -2.408237 -0.722422 -0.520572
S -2.786097 1.782764 0.029195
S 2.329950 1.949271 0.404468
S 2.289689 -0.505491 -0.431469

