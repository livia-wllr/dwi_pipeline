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
heudiconv  -v ${PWD}:/base nipy/heudiconv:latest -d /base/dicom/sub-{subject}/ses-{session}/*/*.dcm -o /base/Nifti/ -f convertall -s 219 -ss 333  -c none
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

Heudiconv generates a hidden directory base/Nifti/.heudiconv/219/info and populates it with two files of interest: a skeleton heuristic.py and a dicominfo.tsv file.



#### 2. Step 
Copy the /Nifti/.heudiconv/heuristic.py to /Nifti/code/heuristic.py. You will modify the copied heuristic.py to specify BIDS output names and directories, and the input DICOM characteristics. Available input DICOM characteristics are listed in MRIS/Nifti/.heudiconv/dicominfo.tsv.


#### 3. Step 
Having revised MRIS/Nifti/code/heuristic.py, you can now call HeuDiConv to run on more subjects and sessions. Each time you run it, additional subdirectories are created under .heudiconv that record the details of each subject (and session) conversion. Detailed provenance information is retained in the .heudiconv hidden directory. You can rename your heuristic file, which may be useful if you have multiple heuristic files for the same dataset.















## Trouble shoot :

Common errors : 

* ```AssertionError: Conflicting study identifiers found [1.3.12.2.1107.5.2.50.167110.30000022051710262587100000003, 1.3.12.2.1107.5.2.50.167110.30000022051009185348600000003] ```

This errors arises because the Study IDs in your T1 and other DICOM files are not matching. You can fix this with using the flag ``` --grouping all ```.

See github forum -> [AssertionError: ](https://github.com/nipy/heudiconv/issues/377)


