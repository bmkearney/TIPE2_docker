import math
import sys
import time
import numpy

import datetime
import os
import itertools

class Atom:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z


flagged_files=[]

def distance(x1,x2,y1,y2,z1,z2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** .5

def checker(atoms):
    for i,j in itertools.combinations(atoms,2):
        if (distance(float(i.x),float(j.x),float(i.y),float(j.y),float(i.z),float(j.z))<1):
            return -1

filenames = os.listdir(os.getcwd())
for f in filenames:
    if (f[-6:] == '.pdbqt'):
        file = open(f,'r')
        atoms=[]
        for line in file:
            if line.startswith("ATOM"):
                atoms.append(Atom(line.split()[5],line.split()[6],line.split()[7]))
            if line.startswith("ENDMDL"):
                if(checker(atoms) == -1):
                    flagged_files.append(f)
                break
for i in flagged_files:
    print(i)
