import concurrent.futures
import math
import os
import glob
import re
import subprocess
import time
from time import sleep, perf_counter
import random

good_files=[] #Array of file names that meet RoF and/or bioavailability
file_count=len(glob.glob1('./ligands',"*"))
bestscore="999999"

def dock(current_ligand):
    command = "./vina  --receptor TIPE2.pdbqt --ligand ./ligands/" + current_ligand + " --cpu 3 --center_x 63.32 --center_y 12.29 --center_z 7.61 --exhaustiveness 8 --size_x 10.28 --size_y 10.64 --size_z 11.99 --out docked/" + current_ligand[:-6]+".pdbqt"
    print(command)
    exit(1)
    p=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()


def total_files():
    for file in os.listdir('./ligands'):
        if file.endswith('.pdbqt'):
            good_files.append(file)
    print(len(good_files))

def main():
    total_files()
    start_time = perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for ligand, command in zip(good_files, executor.map(dock, good_files)):
            a=1
            
    end_time = perf_counter()
    print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')
    


if __name__ == '__main__':
    main()

