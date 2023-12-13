import re
import os
import subprocess
from time import sleep
from alive_progress import alive_bar

res = []
best=[]
ligands=[]
bestscore="0.0"
start=0
current=0
runcounter=0

if os.path.exists('continue.log') == False:
    with open('continue.log', 'w') as file1:
        file1.write("0")
        file1.close()
else:
    with open('continue.log', 'r') as file1:
        line=file1.readline()
        start = int(line)
        file1.close()

if os.path.exists('best.log') == False:
    with open('best.log', 'w') as file1:
        file1.write("0")
        file1.close()

else:
    with open('best.log', 'r') as file1:
        line=file1.readline()
        bestscore = line
        file1.close()
        print ("Current best is " +bestscore)


print ("Restarting at "+str(start))


print ("Starting PDBQT cleanup")
#print (mylist)
for file in os.listdir('.\converted'):
    if file.endswith('.pdbqt'):
        #print(file)
        ligands.append(file)
print ("PDBQT cleanup complete")
        
#print (len(ligands))
if start != 0:
    del ligands[0:start]
current=start
for i in ligands:
    command="Vina-GPU.exe --receptor tipe2.pdbqt --ligand ./converted/"+i+" --thread 8000 --seed 1521165304 --center_x 63.3 --center_y 9.49 --center_z 5.66 --size_x 20 --size_y 20 --size_z 20 --out results/"+i
    p=subprocess.Popen(command, shell=True)
    p.wait()
    print("cycle")
    if os.path.exists('results/'+i) == False:
        continue
    file=open('results/'+i, 'r')
    lines=file.readlines()
    for line in lines:
        if "VINA RESULT" in line:
            #mylist=line.split("      ")[1]
            mylist=re.split(' +',line)[3]
            #print (mylist)
            if float(mylist)<float(bestscore):
                #print ("Better Score")
                bestscore=mylist
                file2=open('best.log', 'w')
                #file2.write("file: "+i+" score: "+bestscore)
                file2.write(bestscore+'\n')
                file2.write(i)
                file2.close()
            break                                
    file.close()
    current=current+1
    runcounter=runcounter+1
    with open('continue.log', 'w') as file1:
        file1.write(str(current))
        file1.close()
    with open('out.log', 'a') as file2:
        file2.write(i+' '+mylist+'\n')
        file2.close()
    if runcounter == 10000000:
        break

"""
for i in ligands:
    command='"'+"C:\\Program Files (x86)\\The Scripps Research Institute\\Vina\\vina.exe"+'"'+" --receptor 3f4m.pdbqt --ligand ./ligands/"+i+" --seed 1521165304 --center_x 63.3 --center_y 9.49 --center_z 5.66 --cpu 10 --exhaustiveness 15 --size_x 20 --size_y 20 --size_z 20 --out results/"+i
    print ("Now running ligand "+i)
    #p=subprocess.Popen(command, shell=True)
    p=subprocess.Popen(command, shell=True)
    p.wait()
    #print (command)
"""
"""
# Iterate directory
for file in os.listdir('results'):
    # check only pdbqt files
    if file.endswith('.pdbqt'):
        res.append(file)
#print(res)
scores = []
minmax = []
for i in res:
    file=open('results/'+i,'r')
    lines=file.readlines()
    for line in lines:
        if "VINA RESULT" in line:
            #mylist=line.split("      ")[1]
            mylist=re.split(' +',line)
            #print(mylist)
            best.append({"file":i, "score":mylist})
            minmax.append(float(mylist))
            break
#for i in best:
    #print(i["file"],i["score"])

#print (max(minmax))
#print (min(minmax))

file=open('out.log', 'a')
for i in best:
    file.write(i["file"]+' '+i["score"]+'\n')
file.close()
       
"""
