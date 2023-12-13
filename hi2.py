import os
import subprocess
import shutil

res = []
best=[]
ligands=[]
bestscore="0.0"
start=0
current=0
runcounter=0


print ("Starting PDBQT cleanup")
for file in os.listdir('.\hi'):
    if file.endswith('.pdbqt'):
        if os.path.exists('hiresults/'+file) or os.path.exists('hifailed/'+file):
             continue
        else:
            ligands.append(file)
print ("PDBQT cleanup complete")
print(len(ligands))
        
current=start
for i in ligands:
    command="Vina-GPU.exe --receptor tipe2.pdbqt --ligand ./hi/"+i+" --thread 8000 --seed 1521165304 --center_x 63.3 --center_y 9.49 --center_z 5.66 --size_x 20 --size_y 20 --size_z 20 --out hiresults/"+i
    p=subprocess.Popen(command, shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    p.wait()
    if not os.path.exists('hiresults/'+i):
        print("Failed to dock: "+i)
        shutil.copy(".//hi//"+i, ".//hifailed//"+i)

        
