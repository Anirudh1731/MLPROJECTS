import os
import sys
import src
from src.exception import CustomException
from src.logger import logging 

# this is because this files are present inside the src file 
import pandas as pd
from sklearn.model_selection import train_test_split

from dataclasses import dataclass



# //data class can be used to declase any variable but for function u should define constructor like init 
@dataclass
class DataIngestionConfig:
    train_data_path=os.path.join('artifacts',"train.csv")
    test_data_path=os.path.join('artifacts',"test.csv")
    raw_data_path=os.path.join('artifacts',"data.csv")
# // given the input it will store the splitted data in this path 

class DataIngestion:
    def __init__(self): 
        # this is constructor 
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        # reading the data u can directly read from mongo db too 
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info("Read the database")

            # //making director for train from the config and checking if file is aldready there if there then exiting out 
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info(" Train test split initiated")

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Data ingestion completed")

            # .returned the path so that it can be used for tranforming data at later stage 
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
          

        except Exception as e:
            raise CustomException(e,sys)


if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()

