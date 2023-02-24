import click

import commands


@click.group()
def cli():
    pass


cli.add_command(commands.add_text_to_pdf, name="add-text-to-pdf")
cli.add_command(commands.add_text_to_pdfs, name="add-text-to-pdfs")


if __name__ == "__main__":
    cli()
