class BaseParser:
    """
    BaseParser Class
    To implement different parser - inherit from it
    """

    def extract_text(self, source):
        """
        Method for redefining in an inherited class
        """
        raise NotImplementedError
