! To optimize the structure
%mem=24GB
%chk=optim.chk
#p UB3LYP/6-31+G(2df,p) opt=(CalcAll,maxcycle=200,maxstep=10,maxEstep=300) scrf=(pcm,solvent=DiethylEther) pop=reg freq nmr

Structure of k_P2S6_q4m_1Ptrans

-4  1
P -4.188839 0.979652 -0.288699
P -2.099994 1.364870 0.288701
S -4.825632 2.516071 -0.886994
S -5.411833 0.423905 1.399097
S -4.338006 -0.423599 -1.920220
S -1.950821 2.768155 1.920191
S -0.876994 1.920570 -1.399105
S -1.463212 -0.171541 0.887030

