! To optimize the structure
%mem=24GB
%chk=optim.chk
#p UB3LYP/6-31+G(2df,p) opt=(CalcAll,maxcycle=200,maxstep=10,maxEstep=300) scrf=(pcm,solvent=DiEthylEther) pop=reg freq nmr

Structure of r_P2S6Na_qm1_1sodium

-1  1
P -4.072188 1.734134 -0.082625
P -1.253886 2.051777 -0.191658
S -2.710778 2.782790 1.221173
S -2.606083 0.937054 -1.449406
S -5.567420 2.984761 -1.005873
S -4.763010 0.383070 0.823928
S -0.149457 3.595552 -1.215947
S -0.213117 0.895677 0.647785
Na 2.533799 2.873593 0.735799

