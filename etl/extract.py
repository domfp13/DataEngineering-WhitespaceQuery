# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by DataEngineering Team
# Copyright (c) 2019 CompuCom, All Rights Reserved

from __future__ import annotations
from typing import Optional

def ToCSV(fileName:str, data:list, fields:list) -> None:
    """Takes a list object and creates a CSV file that will me located under the root of this project directory.
    
    Arguments:
     fileName (str): String containing the final nambe on witch the data will be written.
     data (list): List of tuples that will be written in a CSV format
     fields (list): List that will contain the headers for the CSV file that will be written.
    
    Returns:
        None
    """
    import csv
    import os
    from pathlib import Path

    csv.register_dialect('dblquote',
                         delimiter=',',
                         lineterminator='\n',
                         quotechar='"',
                         quoting=csv.QUOTE_ALL,
                         skipinitialspace=True)
  
    path = Path(f'{os.getcwd()}/{fileName}')

    with path.open('w', encoding='utf-8') as csvfile:
        csv_out = csv.writer(csvfile, dialect='dblquote')
        csv_out.writerow(fields)
        for tub in data:
            csv_out.writerow(tub)

def DecoratorGetDirectoryPath(function):
    import os
    from pathlib import Path
    def wrapper():
        return Path('/data/whitespace')
    return wrapper    
@DecoratorGetDirectoryPath
def GetDirectoryPath():
    """This function returns the Path of where the process will place the file
    Arguments: 
     file_type (int): 0 if USA, 1 if Canada 
    
    Returns:
     path (Path): Path object

    """
    import os
    from pathlib import Path

    return Path('C:/Users/lf188653/Desktop/Data/global/WHITESPACE')

def GetMasterFilePath(file_type: int) -> object:
    """This function returns the location of the Master file, this is included under the Masterfile folder under this repo
    
    Arguments: 
     file_type (int): 0 if USA, 1 if Canada 
    
    Returns:
     path (Path): Path object

    """
    import os
    from pathlib import Path
    
    path = None

    if file_type == 0:
        path = Path('{path}/us_zip_codes.csv'.format(path = os.getcwd()))
    else:
        path = Path('{path}/can_zip_codes.csv'.format(path = os.getcwd()))
    
    return path

def MoveMasterFile(file_path_ext, file_path_destination) -> None:
    """This function moves the Master file to a working directory.
    
    Arguments
     file_path_ext (Path): file_path_ext: This is the file path of the Master file including file extension
     file_path_destination (Path): file_path_destination: This is the file path where the file will be copy, with out the extension.
    
    Returns:
     None
    """
    from shutil import copy2
    
    copy2(file_path_ext, file_path_destination)