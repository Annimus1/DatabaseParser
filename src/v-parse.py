#!/usr/bin/python3
import rich_click as click
from util import Util
from model.Parser import Parser


@click.command()
@click.argument('filename', required=True, type=click.Path(exists=True))
def main(filename):
    """
    Main entry point for the database parser CLI.

    Args:
        filename (str): Path to the CSV file to process.
    """
    # Option selected by the user
    option = ''
    # DataFrame that will contain the result file
    global result

    # Create Parser instance
    parser = Parser(filename)

    # Display headers to the user
    Util.Show_headers(parser.get_filename(), parser.get_headers())

    while True:
        # Division line
        print("")

        # Show available actions
        click.echo("Available actions:")
        click.echo("1) Fill up phones")
        click.echo("2) Remove columns")
        click.echo("3) Save")
        click.echo("0) Exit")

        try:
            option = int(input("-> "))

            if option == 1:
                # Fill up Phone columns
                phone_column = int(input("Enter Phone Column > "))
                alt_column = int(input("Enter Alternative Phone Column > "))

                # Ask for additional phone columns
                msg = "Enter additional phone columns (separated by commas) > "
                phones_columns = input(msg)
                phones_columns = [int(p.strip())
                                  for p in phones_columns.split(',')]

                # Ask for additional alternative phone columns
                msg = "Enter additional alt_phone columns (separated by commas) > "
                alt_phones_columns = input(msg)
                alt_phones_columns = [int(p.strip())
                                      for p in alt_phones_columns.split(',')]

                # Call parser method
                result = parser.Fillup_phones(
                    phone_column,
                    alt_column,
                    phones_columns,
                    alt_phones_columns
                )
                parser.set_current_dataframe(result)
                # Update headers
                parser.set_current_headers()
                input("Press Enter to continue")
                continue

            elif option == 2:
                # Remove columns
                prompt = "Enter columns you would like to keep (separated by commas): "
                keep_columns = input(prompt)
                keep_columns = keep_columns.split(
                    ",")  # Convert string into list

                # Call parser method to remove unused columns
                result = parser.RemoveUnusedColumns()
                parser.set_current_dataframe(result)
                # Update headers
                parser.set_current_headers()
                break

            elif option == 3:
                # Save the current DataFrame
                parser.Save(Parser.get_filename())
                break

            elif option == 0:
                # Exit the program
                break

            else:
                raise ValueError

        except ValueError:
            click.echo(click.style(
                text="Invalid Option.", fg="red", bold=True))
            click.echo(click.style(
                text="Please use numbers only.", fg="red", bold=True))


if __name__ == "__main__":
    main()
