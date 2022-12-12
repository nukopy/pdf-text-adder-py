import click

import commands


@click.group()
def cli():
    pass


cli.add_command(commands.add_text_to_pdf)
cli.add_command(commands.add_text_to_pdf_files)


if __name__ == "__main__":
    cli()
