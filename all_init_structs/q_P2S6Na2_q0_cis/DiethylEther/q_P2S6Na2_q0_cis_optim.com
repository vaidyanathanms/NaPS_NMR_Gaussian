! To optimize the structure
%mem=24GB
%chk=optim.chk
#p UB3LYP/6-31+G(2df,p) opt=(CalcAll,maxcycle=200,maxstep=10,maxEstep=300) scrf=(pcm,solvent=DiEthylEther) pop=reg freq nmr

Structure of q_P2S6Na2_q0_cis

0  1
P -4.076853 1.732328 -0.087679
P -1.257870 2.050921 -0.173205
S -2.726129 2.776876 1.230444
S -2.599372 0.937456 -1.443448
S -5.562280 2.986534 -1.021683
S -4.777009 0.379724 0.809380
S -0.148419 3.598672 -1.185975
S -0.221525 0.894387 0.671125
Na -8.568124 3.302328 0.516825
Na 2.567316 2.881511 0.684217

