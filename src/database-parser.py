#!/usr/bin/python3
import rich_click as click
from util import Util
from model.Parser import Parser


@click.command()
@click.argument('filename')
def main(filename):

    option = ''

    # Create Parser instance
    parser = Parser(filename)

    # Show Headers
    Util.Show_headers(parser.get_filename(), parser.get_headers())

    while True:
        # Division line
        print("")

        # show options
        click.echo("Avalilable actions:")
        click.echo("1) remove columns")
        click.echo("2) fill up phone")
        click.echo("3) save")
        click.echo("0) exit")

        try:
            option = int(input("-> "))
            if (option == 0):
                break

            elif (option == 1):
                pass

            elif (option == 2):
                pass

            elif (option == 3):
                parser.Save()

            else:
                raise ValueError

        except ValueError:
            click.echo(click.style(text="Invalid Option.",
                                   fg="red", bold=True))
            click.echo(click.style(text="Please use numbers only.",
                                   fg="red", bold=True))


if __name__ == "__main__":
    main()
