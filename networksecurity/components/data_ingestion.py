""" here we will target data ingestion initation ( it includes 1. read data from mongoDB , 2. create feature store , 
3. do the train - test split , 4. save the train test data into ingested    ) """
from networksecurity.exception_handling.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

# call the config file for  data ingestion config

from networksecurity.entity.config_entity import DataIngestionConfig
import os
import sys
import numpy as np
import pandas as pd
import pymongo
from typing import List
from sklearn.model_selection import train_test_split 
from networksecurity.entity.artifact_entity import DataIngestionArtifact

from dotenv import load_dotenv
load_dotenv()

# read the data from mongoDB url ( this value will comes from env variable )
"""Data Ingestion → Load raw data (CSV, JSON, DB) into a DataFrame.
1. Read data from Mongo DB 
   from where we will get data frames :- read it from MongoDB itself here we need DB name , collection name , DB client 
2. Export data to feature store means Inside the feature store folder I need to have raw csv file ( create function export_data_to_feature_store)
3. drop the columns ( if its required ) and split data as train and test then save inside ingested folder 
4. create DataIngestionArtifact dataclass and call it in dataingestion fuction 
    """
    
MONGO_DB_URL =  os.getenv("MONGO_DB_URL")

class Dataingestion:
    def __init__(self,dataingestionconfig:DataIngestionConfig):
        try:
            self.dataingestionconfig = dataingestionconfig
        except Exception as e:
            raise NetworkSecurityException(e,sys)
       
    #    to connect to DB I need DB name , collection name , mongoDB client , read and clean data 
    def export_collection_as_dataframes(self):
        try:
            database_name = self.dataingestionconfig.database_name
            collection_name = self.dataingestionconfig.collection_name
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            collection = self.mongo_client[database_name][collection_name]
            # if we read data from mongoDB we will get a additional column called _id 
            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"],axis=1)
                
            df = df.replace({"na":np.nan},inplace=True)
            return df
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    
    def export_data_into_feature_store(self,dataframe:pd.DataFrame):
        feature_store_file_path = self.dataingestionconfig.feature_store_file_path
        dir_path = os.path.dirname(feature_store_file_path)
        os.makedirs(dir_path,exist_ok=True)
    # convert entire data frame to csv which will be storing in feature_store_file_path
        dataframe.to_csv(feature_store_file_path,index=False,header=True)
        return dataframe
    
    def split_data_as_train_test(self,dataframe:pd.DataFrame):
        train_set,test_set = train_test_split(dataframe,test_size=self.dataingestionconfig.train_test_split_ratio)
        logging.info("Perform train test split on dataframe")
        # logging.info()
        
        dir_path = os.path.dirname(self.dataingestionconfig.training_file_path)
        os.makedirs(dir_path,exist_ok=True)
             
        logging.info("exporting train and test file path")
        train_set.to_csv(self.dataingestionconfig.training_file_path,header=True,index=False)
        test_set.to_csv(self.dataingestionconfig.testing_file_path,header=True,index=False)
        
        logging.info("successfully exported data to train and test csv")         
    def initiate_data_ingestion(self):
        try:
            dataframe = self.export_collection_as_dataframes()
            dataframe = self.export_data_into_feature_store(dataframe)
            self.split_data_as_train_test(dataframe)
            dataingestionartifact = DataIngestionArtifact( training_file_path=self.dataingestionconfig.training_file_path,test_file_path=self.dataingestionconfig.testing_file_path)
            return dataingestionartifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
