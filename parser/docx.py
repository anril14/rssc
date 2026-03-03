from io import BytesIO
from parser.base import BaseParser
from utils.file_stream import get_file_steam
from docx2python import docx2python as docp


class DocxParser(BaseParser):
    def extract_text(self, source):
        """
        :param source: Path to file or bytes object
        :return: Text content from docx file
        """
        with get_file_steam(source) as stream:
            # transform to a BytesIO stream
            text = docp(BytesIO(stream.read())).text

        return text
