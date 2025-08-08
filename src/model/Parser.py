import pandas as pd 

class Parser:
    def __init__(self, filename):
        self.filename = filename # File name
        self.original_headers = [] # Headers on the file
        # Read the CSV file into a DataFrame
        self.df = pd.read_csv(filename)
        self.original_headers = self.df.columns.values

    def get_headers(self):
        return self.original_headers

    def get_filename(self):
        return self.filename

    # TODO
    # Show options 
    #   Delete one or many columns [Clean](Delete_indexes[])
    #   Filtering a column by one or many values (ignore case) [search](values[]).
    #   Auto Split Files over 400K rows [split](rows=400).
    #   Change Phone numbers format into vicidial (delete +1, parenthesis and blank spaces) [format](vicidial=True)
    #   Export to another file with changes (default prefix Cleanned_{filename}) [save](extention)

    # OPTIONAL

