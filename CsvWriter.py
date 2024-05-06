import os
import csv
import traceback

class CSVWriter:
    def __init__(self,list_of_data,logger):
        """initializing the variable which need to write the data into CSV

        Args:
            list_of_data (list): List of Dictonary(JSON)
        """
        try:
        
            self.passed_data = list_of_data
            self.logger = logger
            current_path = os.getcwd()
            self.headerList = self.passed_data.keys()
            path = os.path.join(self.current_path,"data.csv")
            self.path_is = os.path.isfile(path)
        except:
            self.logger.error(traceback.format_exc())
    def csv_writer(self):
        """Write the data into CSV"""
        try:
            with open("data.csv", 'a') as file: 
                dw = csv.DictWriter(file, delimiter=',',fieldnames=self.headerList)

                # Write the header if the file does not exist
                if not self.path_is:
                    dw.writeheader()
                # Write the data to the file

                for data in self.passed_data:
                    dw.writerow(data)
        except:
            self.logger.error(traceback.format_exc())