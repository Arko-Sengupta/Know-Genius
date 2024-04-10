import os
import logging
import pandas as pd

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)
logging.basicConfig(level=logging.WARNING)

class PrepareDataset:
    def __init__(self) -> None:
        self.Dataset_Dir_Path = 'backend/data'
    
    def CountDatasets(self):
        try:
            return len([file for file in os.listdir(self.Dataset_Dir_Path) if os.path.isfile(os.path.join(self.Dataset_Dir_Path, file))])
        except Exception as e:
            logging.error('An Error Occured: ', exc_info=e)
            raise e
        
    def run(self):
        try:
            datasets_count = self.CountDatasets()
            
            dfs = [pd.read_excel(f'backend/data/General_Knowledge_Sheet_{i}.xlsx') for i in range(1, datasets_count + 1)]
            df = pd.concat(dfs, ignore_index=True)
            df.drop_duplicates(inplace=True)
            
            return df
        except Exception as e:
            logging.error('An Error Occured: ', exc_info=e)
            raise e