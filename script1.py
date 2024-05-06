from dotenv import load_dotenv
import requests
import os
from CsvWriter import CSVWriter
from logger import get_logger
import traceback
load_dotenv()

def api_calling(first_name,last_name):
    """Calling API

    Args:
        first_name ([str]): first name of the person
        last_name ([str]): last name of the person
    """
    try:
        params = {
            'projection': f'({first_name},{last_name})'
        }


        headers = {
            'Authorization': f'Bearer {os.getenv("ACCESS_TOCKEN")}'
        }

        response = requests.get(os.getenv("URL"), headers=headers, params=params)

        if response.status_code == 200:
            list_of_data = response.json()
            CSVWriter(list_of_data,logger)
        else:
            logger.exception(f"Error: {response.status_code} - {response.text}")
            logger.error(traceback.format_exc())
    except:
        pass        
if __name__=="__main__":
    logger = get_logger("log/file.log")
    first_name = input()
    last_name = input()
    api_calling(first_name,last_name)
    