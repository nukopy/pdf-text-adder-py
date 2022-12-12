from io import BytesIO
import os

from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


# constants
FONT_SIZE = 13

# A4 = (210*mm, 297*mm)
TOP = 280  # y
BOTTOM = 10  # y
LEFT = 10  # x
RIGHT = 150  # x
AMAZON_X = 150
AMAZON_Y = 243

TEXT_POSITION_PRESETS = [
    "top-left",
    "top-right",
    "bottom-left",
    "bottom-right",
    "amazon-receipt",
    "",  # 空文字列の場合、x, y で指定した位置に挿入
]

# フォントの登録
pdfmetrics.registerFont(TTFont("ipaexg", "./assets/fonts/ipaexg/ipaexg.ttf"))


def get_position_preset(position_preset: str) -> tuple[float, float]:
    if position_preset == "top-left":
        # 呼び名は y-x、位置は x, y
        return LEFT * mm, TOP * mm
    elif position_preset == "top-right":
        return RIGHT * mm, TOP * mm
    elif position_preset == "bottom-left":
        return LEFT * mm, BOTTOM * mm
    elif position_preset == "bottom-right":
        return RIGHT * mm, BOTTOM * mm
    elif position_preset == "amazon-receipt":
        # Amazon の領収書の右上の宛名記入欄
        return AMAZON_X * mm, AMAZON_Y * mm
    else:
        raise ValueError("Invalid position preset")


def add_text_to_pdf(
    input_filename: str,
    output_filename: str,
    text: str,
    text_position_x: float,
    text_position_y: float,
    text_position_preset: str,
    font_size: int = FONT_SIZE,
) -> None:
    """単一の PDF ファイルにテキストを挿入する"""

    # 編集対象の PDF を読み込み
    input_stream = None
    existing_pdf = None
    try:
        input_stream = open(input_filename, "rb")
        existing_pdf = PdfFileReader(input_stream, strict=False)
    except Exception:
        print(f"Input file is not found: {input_filename}")
        return

    input_stream = open(input_filename, "rb")
    existing_pdf = PdfFileReader(input_stream, strict=False)

    # テキスト挿入用の PDF を作成
    buffer = BytesIO()
    cv = canvas.Canvas(buffer, pagesize=A4)  # A4 = (210*mm,297*mm)

    # テキスト挿入
    x, y = text_position_x * mm, text_position_y * mm  # 挿入位置 (mm 指定)
    if text_position_preset != "":
        # preset の設定を選択した場合は preset の値を優先
        x, y = get_position_preset(text_position_preset)

    cv.setFont("ipaexg", font_size)
    cv.drawString(x, y, text)
    cv.showPage()
    cv.save()

    buffer.seek(0)
    pdf_for_addition_text = PdfFileReader(buffer)

    # 編集対象の PDF の 1 ページ目を読み取り、テキスト挿入用の PDF の 1 ページ目をマージ
    page_input = existing_pdf.getPage(0)
    page_text = pdf_for_addition_text.getPage(0)
    page_input.mergePage(page_text)

    # 出力
    output = PdfFileWriter()
    output.addPage(page_input)
    if output_filename == "":
        # input ファイルと同じディレクトリに出力
        output_dir = os.path.dirname(input_filename)
        input_filename_no_ext = os.path.splitext(os.path.basename(input_filename))[0]
        output_filename = f"{output_dir}/{input_filename_no_ext}-edited.pdf"

    with open(output_filename, "wb") as output_stream:
        output.write(output_stream)

    print(f"input: {input_filename}")
    print(f"output: {output_filename}")

    # close stream
    input_stream.close()
