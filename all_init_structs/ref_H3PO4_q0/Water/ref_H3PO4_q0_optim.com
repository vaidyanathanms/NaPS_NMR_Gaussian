! To optimize the structure
%mem=24GB
%chk=optim.chk
#p UB3LYP/6-31+G(2df,p) opt=(CalcAll,maxcycle=200,maxstep=10,maxEstep=300) scrf=(pcm,solvent=Water) pop=reg freq nmr

Structure of ref_H3PO4_q0

0  1
P -1.361114 1.577979 -0.015705
O -0.262900 0.239231 0.115769
O -2.057931 1.687600 -1.601478
O -2.590971 1.529500 1.209343
H 0.491195 0.470506 -0.483206
H -2.107247 1.679249 2.060552
H -2.589325 0.857567 -1.697852
O -0.546711 2.879923 0.212719

