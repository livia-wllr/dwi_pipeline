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





## Step 2 White matter pathways 


Change config file -> [config_white_matter_pathways](https://github.com/livia-wllr/dwi_pipeline/tree/main/tracula/config_white_matter_pathways)

1. Specify which white-matter pathways to reconstruct 

To specify which of the 42 pathways included in the TRACULA tract atlas to reconstruct, use the ```pathlist``` variable:

```  set pathlist = ( lh.uf rh.uf cc.rostrum ) ```


2. Specify the number of path control points

Use this variable to specify the number of control points that will be used to model each of the pathways in pathlist as a spline.  The default numbers of controls points have been chosen to be proportional to the length of each pathway, and are given in the last column of $FREESURFER_HOME/trctrain/hcp/pathlist.txt.

``` set ncpts = ( 7 7 5 ) ```


3. Start step with following command 

``` trac-all -path -c $SUBJECT_DIR/config_white_matter_pathways``` 

