#!/usr/bin/python3
import rich_click as click
import pandas as pd
from util import Util
from model.Parser import Parser


@click.command()
@click.argument('filename')
def main(filename):
    # Create Parser instance
    parser = Parser(filename)

    # Show Headers
    Util.Show_headers(parser.get_filename(), parser.get_headers())

if __name__ == "__main__":
    main()
