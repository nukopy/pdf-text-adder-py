from pathlib import Path
import glob
import os

import click

import pdf


@click.command()
@click.option(
    "--input-filename",
    default="./dummy.pdf",
    help="Input of PDF file path",
)
@click.option(
    "--output-filename",
    default="",
    help='Input of PDF file path. If not specified, the file name will be "{input file name}-edited.pdf"',
)
@click.option(
    "--text",
    default="Hello World Co., Ltd.",
    help="Insert text",
)
@click.option(
    "--text-position-x",
    default=pdf.LEFT,
    type=float,
    help=f"Insert text position x (mm). Default is {pdf.LEFT} mm.",
)
@click.option(
    "--text-position-y",
    default=pdf.TOP,
    type=float,
    help=f"Insert text position y (mm). Default is {pdf.TOP} mm.",
)
@click.option(
    "--text-position-preset",
    type=click.Choice(
        [
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "amazon-receipt",
            "",
        ]
    ),
    default="",
    help="Presets of insert text position. If empty, use --text-position-x and --text-position-y",
)
@click.option(
    "--font-size",
    type=int,
    default=pdf.FONT_SIZE,
    help=f"Font size. Default is {pdf.FONT_SIZE}",
)
def add_text_to_pdf(
    input_filename: str,
    output_filename: str,
    text: str,
    text_position_x: float,
    text_position_y: float,
    text_position_preset: str,
    font_size: int,
) -> None:
    """単一の PDF ファイルにテキストを挿入する"""

    pdf.add_text_to_pdf(
        input_filename,
        output_filename,
        text,
        text_position_x,
        text_position_y,
        text_position_preset,
        font_size,
    )


@click.command()
@click.option(
    "--input-dir",
    default="./",
    help="PDF files directory for input",
)
@click.option(
    "--output-dir",
    default="",
    help="PDF files directory for output. If not specified, the directory will be {input dir}.",
)
@click.option(
    "--text",
    default="Hello World Co., Ltd.",
    help="Insert text",
)
@click.option(
    "--text-position-x",
    default=pdf.LEFT,
    type=float,
    help=f"Insert text position x (mm). Default is {pdf.LEFT} mm.",
)
@click.option(
    "--text-position-y",
    default=pdf.TOP,
    type=float,
    help=f"Insert text position y (mm). Default is {pdf.TOP} mm.",
)
@click.option(
    "--text-position-preset",
    type=click.Choice(
        [
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "amazon-receipt",
            "",
        ]
    ),
    default="",
    help="Presets of insert text position. If empty, use --text-position-x and --text-position-y",
)
@click.option(
    "--font-size",
    type=int,
    default=pdf.FONT_SIZE,
    help=f"Font size. Default is {pdf.FONT_SIZE}.",
)
def add_text_to_pdf_files(
    input_dir: str,
    output_dir: str,
    text: str,
    text_position_x: float,
    text_position_y: float,
    text_position_preset: str,
    font_size: int,
) -> None:
    """複数の PDF ファイルにテキストを挿入する"""

    # get pdf files path from input dir
    pdf_filenames = glob.glob(f"{input_dir}/*.pdf")

    # add text to pdf files
    for input_fname in pdf_filenames:
        output_fname = ""
        if output_dir != "":
            # create output_dir if not exists
            output_path = Path(output_dir)
            output_path.mkdir(parents=True, exist_ok=True)

            # create output filename
            output_fname = os.path.join(
                output_dir,
                os.path.basename(input_fname),
            )

        pdf.add_text_to_pdf(
            input_fname,
            output_fname,
            text,
            text_position_x,
            text_position_y,
            text_position_preset,
            font_size,
        )
