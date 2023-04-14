from dotenv import load_dotenv
import gspread
import os
import json
import pandas as pd

load_dotenv()

class driveBot:
    def __init__(self):
        self.gc = gspread.service_account(filename = "credentials.json")
    
    def get_data(self):
        sh = self.gc.open_by_key("1QJfnmupxqX0zIeYgd4IVTZm-bdL6RsEBLgSOI9Kw2ZQ")
        worksheet = sh.sheet1
        dataframe = pd.DataFrame(worksheet.get_all_records())
        return dataframe