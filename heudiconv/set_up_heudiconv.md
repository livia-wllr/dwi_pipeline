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

:exclamation::exclamation::exclamation: The heudiconv commands only work in bash a shells not in other shells. You need to use bash. :exclamation::exclamation::exclamation:


