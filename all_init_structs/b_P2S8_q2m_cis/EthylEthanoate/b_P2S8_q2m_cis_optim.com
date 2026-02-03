! To optimize the structure
%mem=24GB
%chk=optim.chk
#p UB3LYP/6-31+G(2df,p) opt=(CalcAll,maxcycle=200,maxstep=10,maxEstep=300) scrf=(pcm,solvent=EthylEthanoate) pop=reg freq nmr

Structure of b_P2S8_q2m_cis

-2  1
P -3.436019 1.357741 0.017808
P 0.084361 0.220100 -0.008712
S -1.840900 2.485230 0.943385
S -0.538380 2.169702 -0.713232
S -2.821717 -0.584498 -0.713934
S -1.499838 -0.916917 0.923940
S -4.614398 1.039170 1.296634
S 1.277707 0.525614 1.259377
S 1.124724 -0.918461 -1.516571
S -4.493961 2.511637 -1.465970

