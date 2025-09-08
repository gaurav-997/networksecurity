import os
import numpy as np
import pandas as pd 
import sys

""" Defining common constant variable for training pipeline"""
TARGET_COLUMN= 'Result' # the label I m trying to predict in ML mode
PIPELINE_NAME: str = 'NetworkSecurity'
ARTIFACT_DIR: str = 'Artifacts'
FILE_NAME: str = 'phisingData.csv' # this is our raw.csv
TRAIN_FILE_NAME: str = 'train.csv'
TEST_FILE_NAME: str = 'test.csv'
SCHEMA_FILE_PATH:str = os.path.join("data.schema","schema.yaml")  # we have a folder data_schema and inside that we have file schema.yaml 

""" Data ingestion related constants starts with DATA INJESTION VAR name"""

DATA_INJESTION_COLLECTION_NAME:str= 'NetworkData'
DATA_INJESTION_DATABASE_NAME:str= 'GauravAI'
DATA_INJESTION_DIR_NAME: str = 'data_ingestion'
DATA_INJESTION_FEATURE_STORE_DIR: str = 'feature_store'
DATA_INJESTION_INGESTED_DIR: str = 'ingested'
DATA_INJESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2

""" Data validation related constants starts with DATA_VALIDATION VAR name"""
DATA_VALIDATION_DIR_NAME:str = 'data_validation'
DATA_VALIDATION_VALIDATE_DATA_DIR:str = 'validated'
DATA_VALIDATION_INVALID_DATA_DIR:str = 'invalid'
DATA_VALIDATION_DRIFT_REPORT_DIR:str = 'drift_report'
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str = 'report.yaml'
# DATA_VALIDATION_VALIDATE_TRAIN_FILE_PATH:str = ''
# DATA_VALIDATION_INVALID_TRAIN_FILE_PATH:str = ''
# DATA_VALIDATION_INVALID_TEST_FILE_PATH:str = ''


