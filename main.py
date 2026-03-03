from parser.base import BaseParser
from parser.pdf import PdfParser
from parser.docx import DocxParser
from utils.string_processing import string_processing

SAMPLE_PATH = 'files/Sample-PDF.pdf'


def process_document(parser: BaseParser, source):
    return parser.extract_text(source)


if __name__ == "__main__":
    print(string_processing(process_document(PdfParser(), source=SAMPLE_PATH)))

# TODO Разделение слов в отдельный список + создание структуры(@dataclass) для хранения
