# column-groups-storage

This is the repository for column groups storage in IoTDB. 

The evaluation code is based on IoTDB Python API.

User Guide for setting up the python environment for IoTDB Python API could be found here: https://iotdb.apache.org/UserGuide/V0.13.x/API/Programming-Python-Native-API.html

## File Structure

+ `src/`: include all the codes and datasets used for evaluations

  + `src/results`: results for experiments
  + `src/iotdb-server-and-cli`: iotdb instances, implemented with our proposal and packaged
  + `src/iotdb`: iotdb python interface
  + `src/dataset`: all the datasets used for experiments

+ `doc/`: the full version technical report

  

## How to reproduce

+ Install the python packages for the project according to `requirements.txt` and `requirements_dev.txt`

+ unzip dataset following the instruction below

+ unzip iotdb servers and clients following `src/iotdb-server-and-cli/README.md ` 

+ In command line, change dir to the `iotdb-server-autoalignment/sbin` and type `./start-server.sh`  (or `sbin\start-server.bat` in Windows), instructions could be find in https://iotdb.apache.org/UserGuide/V0.13.x/QuickStart/QuickStart.html.

+ In command line, change dir to the `iotdb-server-iotdb-server-single/sbin` and type `./start-server.sh`  (or `sbin\start-server.bat` in Windows), instructions could be find in https://iotdb.apache.org/UserGuide/V0.13.x/QuickStart/QuickStart.html.

+ Run `python BaselinesEvaluation.py` for single-column and single-group baselines

+ Run `python AutoAlignedEvaluation.py` for column-groups baselines

+ Find results in `src/results`

  

## Dataset

### Instruction

Due to the file size limitation of the Github, the datasets are provided with samples.

The data are all masked for research use.

To reproduce, please unzip `src/dataset/dataset.zip`  put them under following path:

**File Structure**

+ `src/dataset`

  + `src/dataset/Chemistry`
  + `src/dataset/Climate`
  + `src/dataset/opt`
  + `src/dataset/Ship`
  + `src/dataset/Train`
  + `src/dataset/Vehicle2`
  + `src/dataset/WindTurbine`
  
