! To compute the IR frequency of the system
%mem=24GB
%oldchk=optim_fin.chk
%chk=freq.chk
#p py_basis opt=(CalcAll,maxcycle=py_maxcyc,maxstep=py_maxstep) scrf=(py_cavity,solvent=py_solv) pop=reg freq=noraman

Structure of py_struct

py_charge  py_mult
