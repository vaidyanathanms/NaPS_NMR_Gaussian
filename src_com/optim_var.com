! To optimize the structure
%mem=24GB
%chk=optim.chk
#p py_basis opt=(CalcAll,maxcycle=py_maxcyc,maxstep=py_maxstep) scrf=(py_cavity,solvent=py_solv) pop=reg

Structure of py_struct

py_charge  py_mult
