! To optimize the structure
%mem=24GB
%chk=optim.chk
#p UB3LYP/6-31+G(2df,p) opt=(CalcAll,maxcycle=200,maxstep=10,maxEstep=300) scrf=(pcm,solvent=THF) pop=reg freq nmr

Structure of c_P1S3_q1m_mon

-1  1
P -1.710834 0.564083 -0.000001
S -3.295866 1.346556 0.000000
S -0.386635 1.735017 0.000000
S -1.425292 -1.574332 0.000000

