from soupsieve.util import lower
from re import findall


def string_processing(raw: str) -> (list, str):
    """
    :param raw: Raw string from parsed file
    :return: Useful words for context in list and string formats
    """
    words = findall(r"[а-яёa-z]+", raw.lower())

    return words, ' '.join(words)
