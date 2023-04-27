# qsiprep - Preprocessing 

The qsiprep preprocessing workflow takes as principal input the path of the dataset that is to be processed. The input dataset is required to be in valid BIDS formate at least one diffusion MRI series. The T1w image and the DWI may be in separate BIDS <session> folders for a given subject. If you want to make sure that your dataset is vaild, you can use a online BIDS Validatior .



## Install qsiprep on HPC-Cluster 
  
### qsiprep Singularty 
  
  
You can run qsiprep while using an Singularty Container. In order to build this Sinhularty Image use the follwoing command: 
  
  
  ```
  singularity build qsiprep-<version>.sif docker://pennbbl/qsiprep:<version>
  ```
  
  
 ## Run qsiprep 
  
 
```


  
```
  
 
