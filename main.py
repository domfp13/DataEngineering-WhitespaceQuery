# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by DataEngineering Team
# Copyright (c) 2019 CompuCom, All Rights Reserved
# To run: python main.py whitespace_usa

# Libs
from __future__ import annotations
from typing import Optional
from pathlib import Path
from etl.db_connection import OracleConnection
from etl.queries import (WhiteSpaceUSA)
from etl.extract import (ToCSV, GetMasterFilePath, MoveMasterFile, GetDirectoryPath)
import datetime
import logging
import sys
import os

REGISTRY = {
    "whitespace_usa": WhiteSpaceUSA()
}

if __name__ == "__main__":
    """ 
    This is the logic that runs a query agains the DB and retrives data for the WhiteSpace Analysis
  
    Parameters: 
    arg1 (str): Function Name that will be execute
  
    Returns: 
    None
    """
    try:
            
        # 0.- Setup the logging object
        LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
        loggin_file_path = str(Path('{path}/LOGGER.log'.format(path = os.getcwd())))
        logging.basicConfig(filename = loggin_file_path,
                            level = logging.DEBUG,
                            format = LOG_FORMAT,
                            filemode = 'w')
        
        logger = logging.getLogger()


        # Checking if the execution contains the function that will be execute
        if len(sys.argv) == 2 and str(sys.argv[1]) in REGISTRY:

            data_type = str(sys.argv[1])
        
            # 1.- Connecting to DW
            logger.info("1.-Stablishing connection with DW")
            oracle_conn = OracleConnection()

            # 2.- Running query and creating CSV
            logger.info(f"2.-Running query {data_type}")
            col_names, data = oracle_conn.sql_to_data_no_binding(REGISTRY[data_type])

            # 3.- Writting data to CSV
            logger.info("3.-Writting data to CSV")
            if data_type == 'whitespace_usa':
                file_name_output = 'us_zip_codes.csv'
            else:
                file_name_output = 'can_zip_codes.csv'

            ToCSV(fileName=file_name_output, data=data, fields=col_names)

            # 4.- Moving file
            logger.info("4.-Begin copying Master file")
            files_directory_path = GetDirectoryPath()
            
            if data_type == 'whitespace_usa':
                MoveMasterFile(GetMasterFilePath(0), files_directory_path)
            else:
                MoveMasterFile(GetMasterFilePath(1), files_directory_path)
            
    except Exception as e:        
        logger.error(e)
        sys.exit()