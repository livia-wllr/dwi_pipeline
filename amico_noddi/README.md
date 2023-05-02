# AMICO NODDI - qsiprep

For the reconstruction we use the software package [AMICO NODDI ]([https://github.com/user/repo/blob/branch/other_file.md](https://qsiprep.readthedocs.io/en/latest/reconstruction.html#amico-noddi)). 
You can send the output from the preprocessing to the  pre-configured recon_workflows.
Under the flag   ```--recon-spec``` you can specify the workflow. The list of workflows you can use -> [recon_workflows](https://qsiprep.readthedocs.io/en/latest/reconstruction.html). 



## How to start AMICO NODDI


1. Assign the paths from your directorys. 

```
export WORKDIR="/home/path/to/directory/work"
export OUTDIR="/home/path/to/directory/derivatives"
export RECONINPUT="/home/path/to/directory/derivatives/qsiprep"
export FSLICENSE="/home/path/to/directory/freesurfer/license.txt"
```




2. start qsiprep with the ```--recon-spec amcio noddi``` flag. 



```
singularity run --cleanenv --contain --nv \
-B ${RECONINPUT}:/input:ro \
-B ${OUTDIR}:/output \
-B ${WORKDIR}:/work \
-B ${FSLICENSE}:/license.txt:ro \
/home/path/to/directory//qsiprep-0.16.1.sif \
/input /output participant \
   -w /work \
   --participant_label sub-1234 \
   --recon-only \
   --recon_input /input \
   --recon_spec amico_noddi \
   --fs-license-file /license.txt \
   -vv
```

As a input (RECONINPUT) for the AMICO NODDI workflow use the derivatives folder you got as a outout from the preprocessing with qsiprep. 
Create the ```work```and ```derivativtes```folder with the ```mkdir```command. 





