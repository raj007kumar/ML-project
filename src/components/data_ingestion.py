import os
import sys
from src.exception import customException

from src.logger import logging

from src.components.data_transformation import datatransformation
from src.components.data_transformation import data_transformationconfig


import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class data_ingestion_config:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')
    
    
class data_ingestion:
    def __init__(self,config:data_ingestion_config):
        self.config=config
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('C:\\Users\\HP\\Downloads\\ML-project\\notebook\\data\\stud.csv')
            logging.info("Read the dataset as pandas dataframe")
            
            os.makedirs(os.path.dirname(self.config.raw_data_path),exist_ok=True)
            df.to_csv(self.config.raw_data_path,index=False,header=True)
            
            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            
            train_set.to_csv(self.config.train_data_path,index=False,header=True)
            test_set.to_csv(self.config.test_data_path,index=False,header=True)
            
            logging.info("Ingestion of the data is completed")
            
            return(
                self.config.train_data_path,
                self.config.test_data_path
            )
        except Exception as e:
            raise customException(e,sys)
        
if __name__ == "__main__":
    config_ingestion = data_ingestion_config()  # Data ingestion config instance
    obj_ingestion = data_ingestion(config_ingestion)  
    train_data, test_data = obj_ingestion.initiate_data_ingestion()
    
    config_transformation = data_transformationconfig()  # Fix: Create transformation config instance
    data_transformation = datatransformation(config_transformation)  # Fix: Pass the correct config

    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

    

