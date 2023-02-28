# Set up Tracula


1. Install FSL (MAC OS Installation)

See documentation of [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FslInstallation/MacOsX) for more information. 

Download [installer.py](https://git.fmrib.ox.ac.uk/fsl/conda/installer/-/blob/master/fsl/installer/fslinstaller.py) for installing  FSL. 

Use following commands: 

``` python3 fslinstaller.py```

For the ```$FSLDIR``` enviroment variable use /Application/fsl Folder on your local Machine. 

Test with command ```pwd```if the path is set up correctly. 

If not use the following command -> ```export FSL_DIR=/Applications/fsl```






2. Install Freesurfer 

Download the .tar file from the [freesurfer website](https://surfer.nmr.mgh.harvard.edu/fswiki/rel7downloads).

Run the following commands for setup: 

```tar -zxvpf freesurfer-darwin-macOS-7.1.1.tar.gz ```

``` cd freesurfer```

```pwd```

/Applications/freesurfer/

``` export FREESURFER_HOME=/Applications/freesurfer```

```source $FREESURFER_HOME/SetUpFreeSurfer.sh```

The output should look like the following : 


```
-------- freesurfer-darwin-macOS-7.3.2-20220804-6354275 --------
Setting up environment for FreeSurfer/FS-FAST (and FSL)
FREESURFER_HOME   /Applications/freesurfer/
FSFAST_HOME       /Applications/freesurfer//fsfast
FSF_OUTPUT_FORMAT nii.gz
SUBJECTS_DIR      /Applications/freesurfer//subjects
MNI_DIR           /Applications/freesurfer//mni
FSL_DIR           /Applications/fsl/
```





Command to start bedpostX : 

```trac-all -bedp -c dmrirc.tutorial ```



