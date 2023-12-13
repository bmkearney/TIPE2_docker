# NDMC_docker
This is a series of scripts to automate the docking of ligands into a target protein using AutoDock Vina or Vina-GPU.

## vina_pipeline_3.py
This is a general script to dock all ligands in a subfolder named **converted.** 
Adjust the command line at the indicated places for your protein of interest.
Vina-GPU.exe --receptor protein_target.pdbqt --ligand ./converted/"+i+" --thread 8000 --center_x **63.3** --center_y **9.49** --center_z **5.66** --size_x **20** --size_y **20** --size_z **20** --out results/

We used webina https://durrantlab.pitt.edu/webina/ to get initial center_x, center_y, and center_z coordinates.
