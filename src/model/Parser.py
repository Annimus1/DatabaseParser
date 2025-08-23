import pandas as pd
from os import path, getcwd, path
from rich_click import echo, style
from typing import List
from model.Serializable import Serializable


class Parser(Serializable):
    """
    Parser class for handling CSV files and performing data cleaning operations.

    Attributes:
        fullPath (str): Absolute path to the file.
        filename (str): Name of the file.
        original_headers (list): List of original column headers.
        df (pd.DataFrame): Current DataFrame loaded from the file.
    """

    def __init__(self, filename: str):
        """
        Initialize the Parser object.

        Args:
            filename (str): Path to the CSV file.
        """
        self.fullPath = path.abspath(filename)
        self.filename = path.basename(self.fullPath)
        self.original_headers = []
        self.df = pd.read_csv(filename)
        self.original_headers = self.df.columns.values

    def set_current_dataframe(self, new_data_frame: pd.DataFrame) -> None:
        """
        Set the current DataFrame.

        Args:
            new_data_frame (pd.DataFrame): DataFrame to set as current.
        """
        self.df = new_data_frame

    def get_current_dataframe(self) -> pd.DataFrame:
        """
        Get the current DataFrame.

        Returns:
            pd.DataFrame: The current DataFrame.
        """
        return self.df

    def get_headers(self) -> list:
        """
        Get the original headers of the DataFrame.

        Returns:
            list: List of column headers.
        """
        return self.original_headers

    def get_filename(self) -> str:
        """
        Get the filename.

        Returns:
            str: The filename.
        """
        return self.filename

    def set_current_headers(self) -> None:
        """
        Update the original headers to match the current DataFrame columns.
        """
        self.original_headers = self.df.columns.values

    def Save(self) -> None:
        """
        Save the DataFrame to a file.

        Args:
            data (pd.DataFrame): DataFrame to save.
            filename (str, optional): Filename to save as. Defaults to 'Cleaned_{filename}'.
            extention (str, optional): File extension. Defaults to 'csv'.
        """

        filename = f"Cleaned_{self.filename}"

        output = path.join(getcwd(), filename)

        try:
            self.df.to_csv(output, index=False)
            echo(style(text=f"File saved successfully: {
                 output}", bold=True, fg="green"))

        except IOError:
            echo(style(
                text=f"There was a problem\nThe file could not be processed", bold=True, fg="red"))

    def RemoveUnusedColumns(self, columnsToKeep: List[int]):
        """
        Remove unused columns from the DataFrame.

        Args:
            columnsToKeep (List[int]): List of column indices to keep.
        """

        columns = []

        try:
            # Fill up columns headers
            for i in columnsToKeep:
                columns.append(self.original_headers[i])

            # Create new df with selected columns
            new_df = self.df[columns]

            self.set_current_dataframe(new_df)
            self.set_current_headers()
            echo(style(text=f"Dataframe updated successfully -> Columns: {columns}",
                       fg="green", bold=True))

        except IndexError:
            echo(style(text=f"Some columns doesn't match, please try again.",
                       fg="red", bold=True))

    def Fillup_phones(self, phone_column: int, alt_column: int,
                      phones_columns: List[int],
                      alt_phones_columns: List[int]) -> pd.DataFrame:
        """
        Fill missing phone and alternative phone numbers from specified columns.

        Args:
            phone_column (int): Index of the main phone column.
            alt_column (int): Index of the alternative phone column.
            phones_columns (List[int]): List of indices for phone alternatives.
            alt_phones_columns (List[int]): List of indices for alt phone alternatives.

        Returns:
            pd.DataFrame: Updated DataFrame with filled phone columns.
        """
        for index, row in self.df.iterrows():
            # Check if main phone is missing
            if pd.isna(row[self.original_headers[phone_column]]):
                alternatives = phones_columns + [alt_column]
                self.df.iloc[index, phone_column] = self._fill_collum(
                    index, alternatives)
                if pd.isna(self.df.iloc[index, phone_column]):
                    echo(style(text=f"[{index}] Phone not updated.", fg="red"))
                else:
                    echo(style(text=f"[{index}] Phone updated: {
                         str(self.df.iloc[index, phone_column])}", fg="yellow"))

            # Check if alternative phone is missing
            if pd.isna(row[self.original_headers[alt_column]]):
                self.df.iloc[index, phone_column] = self._fill_collum(
                    index, alt_phones_columns)
                if pd.isna(self.df.iloc[index, phone_column]):
                    echo(
                        style(text=f"[{index}] Alt Phone not updated.", fg="red"))
                else:
                    echo(style(text=f"[{index}] Alt Phone updated: {
                         str(self.df.iloc[index, phone_column])}", fg="yellow"))

        return self.df

    def _fill_collum(self, index: int, alternatives: List[int]) -> str | None:
        """
        Helper method to fill a column from alternative columns.

        Args:
            index (int): Row index.
            alternatives (List[int]): List of column indices to check.

        Returns:
            str | None: Value found or None.
        """
        result = None
        row = self.df.iloc[index]

        for col_index in alternatives:
            value = row.iloc[col_index]
            if pd.notna(value) and (isinstance(value, str) and value.strip() != ''):
                self.df.iloc[index, col_index] = None
                return str(value).strip()

        return result

    def Filter_by(self, column_values: List[str]):
        """
        Filter the DataFrame by specified column values.

        Args:
            column_values (List[str]): List of column values to filter by.
        """
        pass

    def Vicidialize(self, data: pd.DataFrame):
        """
        Format phone numbers for Vicidial (remove +1, parentheses, and spaces).

        Args:
            data (pd.DataFrame): DataFrame containing phone numbers.
        """
        pass

    # TODO: Auto Split Files over
