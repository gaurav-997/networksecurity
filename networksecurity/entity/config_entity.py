# this file has all basic info like Data ingestion dir , feature store file path , training file path , testing file path ,
# train test split ratio , collection name , data base name 

from datetime import datetime
import os
from networksecurity.constants import training_pipeline

print(training_pipeline.ARTIFACT_DIR)
print(training_pipeline.DATA_INJESTION_DATABASE_NAME)

#  for this I need basic info like timestamp , pipeline name , artifact dir name and path ( and these values we get from constants __init__ file ) 
class TrainingPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.timestamp:str = timestamp
        self.pipeline_name= training_pipeline.PIPELINE_NAME # comes from constant 
        self.artifact_name = training_pipeline.ARTIFACT_DIR
        self.artifact_dir = os.path.join(self.artifact_name,timestamp)
  
#  for this I need  Data ingestion dir , feature store file path , training file path , testing file path ,train test split ratio ,
# collection name , data base name   
class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_ingestion_dir:str = os.path.join(training_pipeline_config.artifact_dir,training_pipeline.DATA_INJESTION_DIR_NAME) # training_pipeline is constnats file
        self.feature_store_file_path:str = os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INJESTION_FEATURE_STORE_DIR,training_pipeline.FILE_NAME)  # inside artifacts we have raw file 
        self.training_file_path:str = os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INJESTION_INGESTED_DIR,training_pipeline.TRAIN_FILE_NAME) # inside injestion dir we have test and trin files 
        self.testing_file_path:str = os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INJESTION_INGESTED_DIR,training_pipeline.TEST_FILE_NAME)
        self.train_test_split_ratio:float = training_pipeline.DATA_INJESTION_TRAIN_TEST_SPLIT_RATIO
        self.database_name:str = training_pipeline.DATA_INJESTION_DATABASE_NAME
        self.collection_name:str = training_pipeline.DATA_INJESTION_COLLECTION_NAME
        
        