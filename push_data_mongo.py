import os
import sys
import json
import certifi
import pandas as pd
import numpy as np
import pymongo
from networksecurity.logging.logger import logging
from networksecurity.exception_handling.exception import NetworkSecurityException

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

# we need certificate for making secure HTTP connection 
# certify is the python package that provides the root package , its used by python libraries that makes a secure HTTP connection 
ca = certifi.where() # this where retrives the part of bundle of CA certificats provided by certify and stored in certificate autority 

# creating ETL pipeline 
class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_convertor(self,file_path):
        try:
            data = pd.read_csv(file_path) # read file 
            data.reset_index(drop=True,inplace=True) # reset the index
            records = list(json.loads(data.T.to_json()).values()) # list of json , transpose(T) the data and convert it to json 
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mongo(self,records,database,collection):
        try:
            self.records = records
            self.database = database
            self.collection = collection
            
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__ == '__main__':
    FILEPATH = "Network_Data\phisingData.csv"
    DATABASE = "GauravAI"
    Collection = "NetworkData"
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_convertor(FILEPATH)
    print(records)
    number_of_records = networkobj.insert_data_mongo(records,DATABASE,Collection)
    print(number_of_records)
    

