from networksecurity.components.data_ingestion import Dataingestion
from networksecurity.exception_handling.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__=='__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestion = Dataingestion(dataingestionconfig=DataIngestionConfig(trainingpipelineconfig))
        logging.info("initiated the data ingestion ")
        dataingestionartifact = dataingestion.initiate_data_ingestion()
        print(dataingestionartifact)
    except Exception as e:
           raise NetworkSecurityException(e,sys)  # raising our custom error 

