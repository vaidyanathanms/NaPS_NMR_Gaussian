! To optimize the structure
%mem=24GB
%chk=optim.chk
#p UB3LYP/6-31+G(2df,p) opt=(tight,maxcycle=200,maxstep=10,maxEstep=300) Guess=mix scrf=(pcm,solvent=THF) pop=reg freq nmr

Structure of e2_P2S8_q2m_endScharge

-2  1
P	-4.455036	-0.292849	0.269516
S	-3.654488	0.820586	-1.461305
S	-4.186111	0.671927	1.952121
S	-3.282825	-2.023419	-0.159998
P	-2.440624	-0.888633	-1.849419
S	-6.376842	-1.051466	-0.156571
S	-7.774543	0.362356	0.368594
S	-2.636526	-1.839448	-3.551431
S	-0.545545	-0.124109	-1.327832
S	0.853047	-1.598789	-1.655445

