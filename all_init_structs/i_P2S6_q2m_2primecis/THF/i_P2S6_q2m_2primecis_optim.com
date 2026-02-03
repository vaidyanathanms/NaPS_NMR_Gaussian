! To optimize the structure
%mem=24GB
%chk=optim.chk
#p UB3LYP/6-31+G(2df,p) opt=(CalcAll,maxcycle=200,maxstep=10,maxEstep=300) scrf=(pcm,solvent=THF) pop=reg freq nmr

Structure of i_P2S6_q2m_2primecis

-2  1
P -1.529085 1.880560 0.882475
P 1.494088 1.960135 0.878887
S 0.014957 0.648159 0.013920
S -0.051994 3.264657 1.630967
S -1.877699 2.993490 -0.932730
S -3.984752 2.756937 -0.760933
S 1.779362 3.089747 -0.937073
S 3.896236 2.956012 -0.775513

