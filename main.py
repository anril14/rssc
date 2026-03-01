from parser.base import BaseParser
from parser.pdf import PdfParser


def process_document(parser: BaseParser, source):
    return parser.extract_text(source)


if __name__ == "__main__":
    print(process_document(PdfParser(), source='files/Sample-PDF.pdf'))
