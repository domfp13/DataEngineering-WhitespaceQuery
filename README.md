# DataEngineering-WhitespaceAnalysis
This is the DataEngineering-WhitespaceAnalysis project, this project takes a Excel file and different argumentes from a web form and runs a query against the DB (depending if is USA/Canada), the data that is produced it is later transformed to a CSV file and latter clean and merge with the original Excel file.

## Getting Started

### 1- Prerequisites
* [Anaconda]() - Anaconda allows us to keep virtual environments organize and it is the best setup tool for data analysis. This code needs python 3.7

### 2- Installing requirementes
```sh
$ git clone ~/DataEngineering-WhitespaceAnalysis.git
$ conda create -n WhitespaceAnalysis python=3.7
$ conda activate WhitespaceAnalysis
$ cd DataEngineering-WhitespaceAnalysis
$ pip install requirements.txt
```
### 3- Description
The process runs two different queries depending if the file that is being process is (USA/CANADA), these are the values that the web form needs to provide: 
* data_type ('US Zip Codes'/'CAN Postal Codes')
* sheet_name (Excel Sheet Name)
* code_column (Where the zip codes are)
* data_column (Where the program should start writting the values)

Every time the process is run it producess a .log file "*LOGGER.log*", this file will help to debug/chatch up errors.

```sh
$ python main.py
```
## Authors
* **Luis Fuentes**
* **Marco Rodriguez**