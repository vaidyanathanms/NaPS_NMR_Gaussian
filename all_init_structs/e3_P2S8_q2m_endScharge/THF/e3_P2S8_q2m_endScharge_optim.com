! To optimize the structure
%mem=24GB
%chk=optim.chk
#p UB3LYP/6-31+G(2df,p) opt=(CalcAll,maxcycle=200,maxstep=10,maxEstep=300) scrf=(pcm,solvent=THF) pop=reg freq nmr

Structure of e3_P2S8_q2m_endScharge

-2  1
P -4.125996 -1.490581 -0.363919
S -3.966148 0.659160 -0.426970
S -3.778567 -1.987689 1.296777
S -2.421555 -1.920225 -1.616185
P -2.261694 0.229516 -1.679218
S -6.033745 -2.184283 -1.100338
S -5.317737 -4.169199 -1.382652
S -2.609099 0.726646 -3.339912
S -0.353952 0.923201 -0.942764
S -1.070002 2.908077 -0.660267

