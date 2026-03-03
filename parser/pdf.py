from parser.base import BaseParser
from utils.file_stream import get_file_steam
from PyPDF2 import PdfReader


class PdfParser(BaseParser):
    def extract_text(self, source: str | bytes):
        """
        :param source: Path to file or bytes object
        :return: Text content from pdf file
        """
        with get_file_steam(source) as stream:
            # init pdf_reader object
            pdf_reader = PdfReader(stream)

            # get count of pages
            page_count = len(pdf_reader.pages)

            # list of text content by pages
            text_by_pages = []

            # iterate through every page
            for _ in range(0, page_count):
                text_by_pages.append(pdf_reader.pages[_].extract_text() or '')

        return ''.join(text_by_pages)
