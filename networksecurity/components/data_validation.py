"""
1.Initiate the data validation :- 
1. Data validation config = read the data from data ingestion artifacts ( train.csv and test.csv )
2. Initiate Data validation = validate number of columns ( train and test status) 
                            is numerical columns exists ( train and test status )
4. comparision as compare to schema.yaml 
"""

from networksecurity.entity.artifact_entity import DataIngestionArtifact  # input ( train and test.csv of data_ingestion)
from networksecurity.entity.artifact_entity import DataValidationArtifact # output of data validation 
from networksecurity.entity.config_entity import DataValidationConfig  # file and dir -  path & names 
from networksecurity.exception_handling.exception import NetworkSecurityException
from networksecurity.constants.training_pipeline import SCHEMA_FILE_PATH
from networksecurity.logging.logger import logging
from scipy.stats import ks_2samp  # used to check data drift 
import os 
import numpy as np
import pandas as pd
import sys
from networksecurity.utils.main_utils.utils import read_yaml_file , write_yaml_file

class DataValidation:
    #  Data validation config get all the file path ( from DataValidationConfig) ) and common info 
    def __init__(self,data_ingestion_artifact:DataIngestionArtifact,datavalidationconfig:DataValidationConfig):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.datavalidationconfig = datavalidationconfig
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    #  read the data 
    @staticmethod
    def read_data(file_path) ->pd.DataFrame:
        return pd.read_csv(file_path)
    
    def validate_number_of_columns(self,dataframe:pd.DataFrame) ->bool:
        try:
            logging.info("validating number of columns in data frame")
            number_of_columns = len(self._schema_config)
            logging.info(f"Required number of columns {number_of_columns} and columns in datafram is {len(dataframe.columns)} ")
            if len(dataframe.columns) == number_of_columns:
                return True
            else:
                return False
            
        except Exception as e:
            raise NetworkSecurityException(e,sys)
     
    #   checkin if their is a data drift or not if not create a status report and update it via write yaml 
    def detect_data_drift(self,base_df,current_df,threshold=0.5) -> bool:
        try:
            status = True
            report = {}
            for column in base_df.columns:
                d1 = base_df[column]
                d2 = current_df[column]
                is_same_distance = ks_2samp(d1,d2)  # comparing the columns 
                if threshold <= is_same_distance.pvalue:
                    is_found = False
                else:
                    is_found = True
                    status = False
                report.update({column:{
                    "p_value":float(is_same_distance.pvalue),
                    "status": is_found
                }})
            drift_report_file_path:str = self.datavalidationconfig.drift_report_file_path
            
            # create directory
            dir_path = os.path.dirname(drift_report_file_path)
            os.makedirs(dir_path,exist_ok=True)
            
            write_yaml_file(drift_report_file_path,content=report)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    #  Initiate Data validation 
    def initiate_data_validation(self) ->DataIngestionArtifact:
        try:
            train_file_path = self.data_ingestion_artifact.training_file_path # from output of data ingestion (under artifact_antity )
            test_file_path = self.data_ingestion_artifact.test_file_path 
            
            # read above data
            train_dataframe = DataValidation.read_data(train_file_path)
            test_datafram = DataValidation.read_data(test_file_path)
            
            # validate number of columns 
            status = self.validate_number_of_columns(dataframe=train_dataframe)
            if not status:
                error_message = "train data frame not contain all columns "
        
            status = self.validate_number_of_columns(dataframe=test_datafram)
            if not status:
                error_message = "test data frame not contain all columns "
                
            # check data drift
            status = self.detect_data_drift(base_df=train_dataframe, current_df= test_datafram)
            dir_path = os.path.dirname(self.datavalidationconfig.invalid_train_file_path)
            os.makedirs(dir_path)
            
            # is status is true upload data
            train_dataframe.to_csv(self.datavalidationconfig.valid_train_file_path,index=False,header=True)
            test_datafram.to_csv(self.datavalidationconfig.valid_test_file_path,index=False,header=True)
            
            data_validation_artifact = DataValidationArtifact(
                validation_status= status,
                valid_train_file_path = self.data_ingestion_artifact.training_file_path,
                valid_test_file_path= self.data_ingestion_artifact.test_file_path,
                invalid_train_file_path= None,
                invalid_test_file_path = None,
                drift_report_file_path = self.datavalidationconfig.drift_report_file_path )
            return data_validation_artifact
            
        except Exception as e:
            raise NetworkSecurityException(e,sys)