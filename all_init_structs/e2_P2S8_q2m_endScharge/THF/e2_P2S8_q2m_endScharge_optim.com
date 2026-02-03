! To optimize the structure
%mem=24GB
%chk=optim.chk
#p UB3LYP/6-31+G(2df,p) opt=(CalcAll,maxcycle=200,maxstep=10,maxEstep=300) scrf=(pcm,solvent=THF) pop=reg freq nmr

Structure of e2_P2S8_q2m_endScharge

-2  1
P -4.473477 -0.470822 0.231577
S -3.946023 0.778835 -1.447122
S -4.083628 0.368705 1.737880
S -2.953900 -1.971637 -0.067333
P -2.426423 -0.721963 -1.746013
S -6.462432 -1.310757 0.191486
S -7.368642 0.589614 -0.124160
S -2.816218 -1.561491 -3.252328
S -0.437477 0.117996 -1.705860
S 0.468728 -1.782325 -1.389896

