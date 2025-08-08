import rich_click as click

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

