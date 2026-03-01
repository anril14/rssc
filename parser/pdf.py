from parser.base import BaseParser
from utils.file_stream import get_file_steam
import PyPDF2


class PdfParser(BaseParser):
    def extract_text(self, source):
        with get_file_steam(source) as stream:
            # init pdf_reader object
            pdf_reader = PyPDF2.PdfReader(stream)

            # get count of pages
            page_count = len(pdf_reader.pages)

            # list of text content by pages
            text_by_pages = []

            # iterate through every page
            for _ in range(0, page_count):
                text_by_pages.append(pdf_reader.pages[_].extract_text())
        return text_by_pages
