#!/usr/bin/python3
import rich_click as click
from util import Util
from model.Parser import Parser


@click.command()
@click.argument('filename', required=True, type=click.Path(exists=True))
def main(filename):

    # Variables definition
    option = ''
    # DataFrame that will contain the result file.
    global result

    # Create Parser instance
    parser = Parser(filename)

    # Show Headers
    Util.Show_headers(parser.get_filename(), parser.get_headers())

    while True:
        # Division line
        print("")

        # show options
        click.echo("Avalilable actions:")
        click.echo("1) fill up phones")
        click.echo("2) remove columns")
        click.echo("3) save")
        click.echo("0) exit")

        try:
            option = int(input("-> "))

            if (option == 1):  # Fill up Phone
                # ask for Phone and Alt
                phone_column = int(input("Enter Phone Collumn > "))
                alt_column = int(input("Enter Alternative Phone Column > "))

                # Ask for alternatives phone
                msj = "Enter aditionals phone collumns (separated by commas) >"
                phones_columns = input(msj)

                # Ask for alternatives Alt
                msj = "Enter aditionals alt_phone collumns (separated by commas) >"
                alt_phones_columns = input(msj)

                # Call parser method
                result = parser.Fillup_phones(phone_column,
                                              alt_column,
                                              phones_columns,
                                              alt_phones_columns)
                parser.set_current_dataframe(result)
                # Set up new headers
                parser.set_current_headers()
                break

            elif (option == 2):  # Remove columns
                # Ask columns to be keeped
                prompt = "Enter columns you like to keep (separated by commas)"
                keep_columns = input(prompt)
                keep_columns = keep_columns.split(
                    ",")  # Convert string into list

                # Call parser method to cremove those columns
                result = parser.RemoveUnusedColumns()
                parser.set_current_dataframe(result)
                # Set up new headers
                parser.set_current_headers()
                break

            elif (option == 3):  # Save
                parser.Save(Parser.get_filename())
                break

            else:
                raise ValueError

        except ValueError:
            click.echo(click.style(text="Invalid Option.",
                                   fg="red", bold=True))
            click.echo(click.style(text="Please use numbers only.",
                                   fg="red", bold=True))


if __name__ == "__main__":
    main()
