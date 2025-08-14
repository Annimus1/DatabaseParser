import rich_click as click
from rich.console import Console
from rich.table import Table
from typing import List


def Show_headers(filename, original_headers):
    """
    Displays the headers of the given CSV file.

    Parameters
    ----------
        filename (str): The name of the CSV file.
        original_headers (list or array-like): The
        headers extracted from the CSV file.
    """
    # Create a Console object for printing
    console = Console()

    # Create a Table object
    table = Table(title=filename)

    # Add columns to the table
    table.add_column("Index", justify="center", style="cyan2")
    table.add_column("Column", justify="center", style="royal_blue1")

    for index, title in enumerate(original_headers):
        # Add rows to the table
        table.add_row(str(index), title)

    # Print the table to the console
    console.print(table)


def Get_options(options: List[str], type: str = "int"):
    """
    Ask user via standard input to choose one of the given options.

    Parameters
    ----------
        options (list or array-like): list that contains all options, Key
                represents option and Value represents label to show.
        type (str): The type of resulting option ["int","str"].

    Returns
    ----------
        Option_Chosen (T)
    """

    choose = None

    while True:

        try:
            for index, value in enumerate(options):
                click.echo(click.style(text=f"{index}) ", fg="blue"), "value")
            if type == "int":
                choose = int(input("Select an option > "))
            if type == "str":
                choose = input("Select an option > ")

        except ValueError:
            click.echo(click.style(text="", fg="red"))

        return choose
