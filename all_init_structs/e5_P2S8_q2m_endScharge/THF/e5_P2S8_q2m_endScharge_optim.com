! To optimize the structure
%mem=24GB
%chk=optim.chk
#p UB3LYP/6-31+G(2df,p) opt=(CalcAll,maxcycle=200,maxstep=10,maxEstep=300) scrf=(pcm,solvent=THF) pop=reg freq nmr

Structure of e5_P2S8_q2m_endScharge

-2  1
P -2.421561 0.657529 -0.196085
S -0.915518 -0.804550 -0.692181
S -3.252827 1.076566 -1.699129
S -3.676695 -0.643727 0.982139
P -2.169424 -2.105919 0.485154
S -1.590926 2.358047 0.843789
S -3.496729 2.979031 1.561135
S -1.256895 -2.529874 1.938866
S -2.852772 -3.814876 -0.644255
S -4.414832 -4.233428 0.740327

