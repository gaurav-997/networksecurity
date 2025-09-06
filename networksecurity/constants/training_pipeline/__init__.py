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

""" Data ingestion related constants starts with DATA INJESTION VAR name"""

DATA_INJESTION_COLLECTION_NAME:str= 'NetworkData'
DATA_INJESTION_DATABASE_NAME:str= 'GauravAI'
DATA_INJESTION_DIR_NAME: str = 'data_ingestion'
DATA_INJESTION_FEATURE_STORE_DIR: str = 'feature_store'
DATA_INJESTION_INGESTED_DIR: str = 'ingested'
DATA_INJESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2


