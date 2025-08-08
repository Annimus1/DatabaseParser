#!/usr/bin/python3
import rich_click as click
import pandas as pd

@click.command()
@click.argument('filename')
def main(filename):
    original_headers = [] # Headers on the file
    chosen = '' # Option the user chose

    # Read the CSV file into a DataFrame
    df = pd.read_csv(filename)

    # Fill up original_headers with file's headers
    original_headers = df.columns.values

    # Show actual Headers with Index
    Show_headers(filename, original_headers)

    # TODO
    # Show options 
    #   Delete one or many columns [Clean](Delete_indexes[])
    #   Filtering a column by one or many values (ignore case) [search](values[]).
    #   Auto Split Files over 400K rows [split](rows=400).
    #   Change Phone numbers format into vicidial (delete +1, parenthesis and blank spaces) [format](vicidial=True)
    #   Export to another file with changes (default prefix Cleanned_{filename}) [save](extention)

    # OPTIONAL

def Show_headers(filename, original_headers):
    """
    Displays the headers of the given CSV file.

    Parameters:
        filename (str): The name of the CSV file.
        original_headers (list or array-like): The headers extracted from the CSV file.
    """
    click.echo(f"Headers of: {filename}")
    for index, title in enumerate(original_headers):
        click.echo(f"{index}) {title}")


if __name__ == "__main__":
    main()
