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
        
class DataValidationConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_validation_dir:str = os.path.join(training_pipeline_config.artifact_dir,training_pipeline.DATA_VALIDATION_DIR_NAME)
        self.valid_data_dir:str = os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_VALIDATE_DATA_DIR)
        self.invalid_data_dir:str = os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_INVALID_DATA_DIR)
        self.valid_train_file_path:str = os.path.join(self.valid_data_dir,training_pipeline.TRAIN_FILE_NAME)
        self.valid_test_file_path:str = os.path.join(self.valid_data_dir,training_pipeline.TEST_FILE_NAME)
        self.invalid_train_file_path:str = os.path.join(self.invalid_data_dir,training_pipeline.TRAIN_FILE_NAME)
        self.invalid_test_file_path:str = os.path.join(self.invalid_data_dir,training_pipeline.TEST_FILE_NAME)
        self.drift_report_file_path:str = os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_DRIFT_REPORT_DIR,training_pipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME)
    

class DataTransformationConfig:
     def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_transformation_dir: str = os.path.join( training_pipeline_config.artifact_dir,training_pipeline.DATA_TRANSFORMATION_DIR_NAME )
        self.transformed_train_file_path: str = os.path.join( self.data_transformation_dir,training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
            training_pipeline.TRAIN_FILE_NAME.replace("csv", "npy"),)
        self.transformed_test_file_path: str = os.path.join(self.data_transformation_dir,  training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
            training_pipeline.TEST_FILE_NAME.replace("csv", "npy"), )
        self.transformed_object_file_path: str = os.path.join( self.data_transformation_dir, training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
            training_pipeline.PREPROCESSING_OBJECT_FILE_NAME,)
        
class ModelTrainingConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.model_training_dir:str = os.path.join(training_pipeline_config.artifact_dir,training_pipeline.MODEL_TRAINER_DIR_NAME)
        self.trained_model_file_path:str = os.path.join(self.model_training_dir,training_pipeline.MODEL_TRAINER_TRAINED_MODEL_DIR,training_pipeline.MODEL_FILE_NAME)
        self.expected_accuracy:float = training_pipeline.MODEL_TRAINER_EXPECTED_SCORE
        self.overfitting_underfitting_score:float = training_pipeline.MODEL_TRAINER_OVER_FITTING_UNDER_FITTING_THRESHOLD
        