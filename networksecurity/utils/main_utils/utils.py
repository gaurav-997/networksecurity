from networksecurity.exception_handling.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import yaml
import os
import sys
import numpy as np
import pickle
import dill

def  read_yaml_file(filepath:str) ->dict:
    try:
        with open(filepath, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e,sys) from e

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
def save_numpy_array_data(filepath:str, array: np.array):
    """ save numpy array data to a file 
    filepath:str = location of file to save 
    array: np.array = data to save 
    """
    try:
        dir_path = os.path.dirname(filepath)
        os.makedirs(dir_path,exist_ok=True)
        with open(filepath,"wb") as file_object:
            np.save(file_object,array)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
def save_object(file_path:str,obj:object) -> None:
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_object:
            pickle.dump(file_object,obj)
    except Exception as e:
        raise NetworkSecurityException(e,sys)