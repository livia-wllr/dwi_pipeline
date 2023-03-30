# Heudiconv


We want to use HeudiConv to convert our DICOM files into Nifti files . 
Since the computational expense is not to large we can run this step locally. 


## Installation 

For detailed information how to install Heudiconv see ->  [heudiconv docu](https://heudiconv.readthedocs.io/en/latest/installation.html)


### Install heudiconv with pip 

Heudiconv is available ind PyPi and conda. Use the following command in your enviroment to install heudiconv. 

```
pip install heudiconv[all]
```

Also you need to manually install ```dcm2niix```. You can to this with pip : 

```
pip install dcm2niix
```




### Install heudiconv with Docker 

If you want to use Docker for running heudicon use the following command for installation : 

``` 
$ docker pull nipy/heudiconv:latest
```



## Run heudiconv 

> **_NOTE:_**  :exclamation::exclamation::exclamation: The heudiconv commands only work in bash a shells not in other shells. You need to use bash. :exclamation::exclamation::exclamation:





#### 1. Step 
Store  all your DICOMs in one directory. By passing some path information and flags to HeuDiConv, you generate a heuristic (translation) file and some associated descriptor text files. These all get placed in a hidden directory, .heudiconv under the Nifti directory. Use the following command : 

When you run with docker ->
```
docker run --rm -it -v ${PWD}:/base nipy/heudiconv:latest -d /base/dicom/sub-{subject}/ses-{session}/*/*.dcm -o /base/Nifti/ -f convertall -s 219 -ss 333 -c none
```

When you run with pip -> 

```
heudiconv -d /base/dicom/sub-{subject}/ses-{session}/*/*.dcm -o /base/Nifti/ -f convertall -s 219 -ss 333  -c none
```

*  ```--rm```means Docker should cleanup after itself
* ```-it```means Docker should run interactively
* ```-v``` should define your base directory. With ```-v ${PWD}:/base```you can binds your current directory to /base inside the docker container. You could also provide an absolute path to your directory (when using pip instead of docker).

* ```nipy/heudiconv:latest``` identifies the Docker container to run (the latest version of heudiconv)
* ```-d /base/dicom/{subject}/{session}/*/*.dcm``` should define the path to the DICOM files.  The ```{subject}``` and ```{session}``` are going to be repalced by the numbers your define later with the command ```-s``` and ```-ss```.  ```.dcm``` shows the extentions your DICOM files have. The wildcard ```*```  will match all the characters/ file or folder names. 
* ```-o /base/Nifti/```should define the output directory  in Nifti. If the output directory does not exist, it will be created.
* ```-f convertall```  creates a heuristic.py template from an existing heuristic module.
* ```-s 219```specifies the subject number. 219 will replace {subject} in the -d argument when Docker actually runs.
* ```-ss 333``` specifies the session number. 333 will replace {session} in the -d argument when Docker actually runs.
* ```-c none``` indicates you are not actually doing any conversion right now.

Heudiconv generates a hidden directory base/Nifti/.heudiconv/219/333/info and populates it with two files of interest: a skeleton heuristic.py and a dicominfo.tsv file.



#### 2. Step 

Now we are have to modify the heuristic.py Create a new directory (```mkdir code ```) and popy the /Nifti/.heudiconv/heuristic.py to /Nifti/code/heuristic.py. 

##### -> Now the copied heuristic.py has to be modified : 
1. specify BIDS output names and directories,

Section 1a in heudiconv.py : 
```

def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where

    allowed template fields - follow python string module:

    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """

    t1w = create_key('sub-{subject}/{session}/anat/sub-{subject}_{session}_T1w')
    dwiRL4 = create_key('sub-{subject}/{session}/dwi/sub-{subject}_{session}_acq-dwepi112dirs4shb3000monop2s3_dir-RL_dwi')
    dwiLR5 = create_key('sub-{subject}/{session}/dwi/sub-{subject}_{session}_acq-dwepi112dirs4shb3000monop2s3_dir-LR_dwi')
    dwiRL6 = create_key('sub-{subject}/{session}/dwi/sub-{subject}_{session}_acq-dwepi268dirs4shMDDWmonop2s3_dir-RL_dwi')
    dwiLR8 = create_key('sub-{subject}/{session}/dwi/sub-{subject}_{session}_acq-dwepi268dirs4shMDDWmonop2s3_dir-LR_dwi')
    
```

- You have to create a key for all the TW1 and dwi sequences. The key name is to the left of the ```=``` for each row in the above example(e.g t1w, dwiRL4..). 

- Now you have to define the output path and name vor all the sequences. Use ```{subject}```and ```{session}``` wildcards to generelaize your code. 


> **_NOTE:_**  :exclamation::exclamation::exclamation: You need to make sure that the name you give your sequence has to be in the correct BIDS format. Otherwise further preprocessiong steps will not work.   :exclamation::exclamation::exclamation:
> 
> BIDS conform format (see example above): 
>  - The ending of the seqeunce-file name = ```dir-RL_dwi```
>  - The beginning of the sequence_file name = ```sub-{subject}_{session}_acq


- ```subject``` =  participant id   and  ```session```=  session id , will be repalced later when you call the heudiconv command, with the flaggs ```-s```and ```-ss```. 





Section 1a in heudiconv.py : 

Based on your chosen keys, create a data dictionary called info:

```
# Section 1b: This data dictionary (below) should be revised by the user.
###########################################################################
# info is a Python dictionary containing the following keys from the infotodict defined above.
# This list should contain all and only the sequences you want to export from the dicom directory.
 info = {
            t1w: [],
            dwiRL4: [],
            dwiLR5: [],
            dwiRL6: [],
            dwiLR8: [],
            }
```

- Enter each key in the dictionary in this format key: [], for example, t1w: [].
- Separate the entries with commas as illustrated above.





Section 2 in heudiconv.py : 

- Define the criteria for identifying each DICOM series that corresponds to one of the keys you want to export:

```
# Section 2: These criteria should be revised by the user.
##########################################################
# Define test criteria to check that each DICOM sequence is correct
# seqinfo (s) refers to information in dicominfo.tsv. Consult that file for
# available criteria.
# Each sequence to export must have been defined in Section 1 and included in Section 1b.
# The following illustrates the use of multiple criteria:

for idx, s in enumerate(seqinfo):
   if ('anat-T1w_acq' in s.series_description):
            info[t1w].append(s.series_id)
   if ('dwi_dir-RL_acq-112dirsX4shXb3000XmonoXp2Xs3' in s.series_description):
            info[dwiRL4].append(s.series_id)
   if ('dwi_dir-LR_acq-112dirsX4shXb3000XmonoXp2Xs3' in s.series_description):
            info[dwiLR5].append(s.series_id)
   if ('dwi_dir-RL_acq-112dirsX4shXMDDWXmonoXp2Xs3' in s.series_description):
            info[dwiRL6].append(s.series_id)
   if ('dwi_dir-LR_acq-112dirsX4shXMDDWXmonoXp2Xs3' in s.series_description):
            info[dwiLR8].append(s.series_id)
        
   return info

```

- ```'anat-T1w_acq'``` has to be identical to the ```series_description```name writen in the ```/Nifti/.heudiconv/dicominfo.tsv``` file . 
- ```info[t1w]``` : must define the key name of the sequence 









#### 3. Step 
Now we can run heudiconv again 

DOCKER:
```
docker run --rm -it -v ${PWD}:/base nipy/heudiconv:latest -d /base/dicom/{subject}/*/*.dcm -o /base/Nifti/ -f /base/Nifti/code/heuristic.py -s 219 -ss itbs -c dcm2niix -b --overwrite
```

conda enviroment: 
```
heudiconv -d /base/dicom/{subject}/*/*.dcm -o /base/Nifti/ -f /base/Nifti/code/heuristic.py -s 219 -ss itbs -c dcm2niix -b --overwrite

```

* ```-f``` /base/Nifti/code/heuristic.py now tells HeuDiConv to use your heuristic.py file your just created  in the code directory.
*  ```-s 219```specifies the subject number. 219 will replace {subject} in the -d argument 
* ```-ss 333``` specifies the session number. 333 will replace {session} in the -d argument -> we specify the subject we wish to process -s 219 and the name of the session -ss 333.
* ```-c dcm2niix -b``` indicates that we want to use the dcm2niix converter with the -b flag (which creates BIDS).
* ```--overwrite```  With it, everything gets written again (even if it already exists).
Step 3 should produce a tree like this:

```
Nifti
├── CHANGES
├── README
├── code
│   └── heuristic2.py
├── dataset_description.json
├── participants.json
├── participants.tsv
├── sub-219
│   └── ses-333
│       ├── anat
│       │   ├── sub-219_ses-333_T1w.json
│       │   └── sub-219_ses-333_T1w.nii.gz
│       ├── dwi
│       │   ├── sub-219_ses-333_dir-AP_dwi.bval
│       │   ├── sub-219_ses-333_dir-AP_dwi.bvec
│       │   ├── sub-219_ses-333_dir-AP_dwi.json
│       │   └── sub-219_ses-333_dir-AP_dwi.nii.gz
│       ├── sub-219_ses_333_scans.json
│       └── sub-219_ses-333_scans.tsv
```














## Trouble shoot :

Common errors : 

* ```AssertionError: Conflicting study identifiers found [1.3.12.2.1107.5.2.50.167110.30000022051710262587100000003, 1.3.12.2.1107.5.2.50.167110.30000022051009185348600000003] ```

This errors arises because the Study IDs in your T1 and other DICOM files are not matching. You can fix this with using the flag ``` --grouping all ```.

See github forum -> [AssertionError: ](https://github.com/nipy/heudiconv/issues/377)


