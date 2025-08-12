import pandas as pd
from os import path
from typing import List
from model.Serializable import Serializable


class Parser(Serializable):
    def __init__(self, filename):
        self.filename = path.basename(filename)  # File name
        self.fullPath = path.abspath(filename)  # Full Path
        self.original_headers = []  # Headers on the file
        # Read the CSV file into a DataFrame
        self.df = pd.read_csv(filename)
        self.original_headers = self.df.columns.values

    def get_headers(self):
        return self.original_headers

    def get_filename(self):
        return self.filename

    def Save(self, data: pd.DataFrame, filename: str = '',
             extention: str = "csv"):
        if (not filename):
            filename = f"Cleaned_{self.filename}"
        print(f"{filename}.{extention}")

    def RemoveUnusedColumns(self, phoneCol: int, altPhone: int,
                            collumnsToRemove: List[int]) -> pd.DataFrame:
        pass

    # TODO
    # Show options
    #   Delete one or many columns [Clean](Delete_indexes[])
    #   Filtering a column by one or many values (ignore case)[search](values[])
    #   Auto Split Files over 400K rows [split](rows=400).
    #   Change Phone numbers format into vicidial (delete +1, parenthesis and
    #       blank spaces) [format](vicidial=True)
    #   Export to another file with changes (default prefix Cleanned_{filename})[save](extention)

    # OPTIONAL
