from io import BytesIO, IOBase
from typing import IO


def get_file_steam(source: str | bytes) -> IO[bytes]:
    """
    :param source: Path to file or bytes object
    :return: IO[bytes] stream
    """
    if isinstance(source, str):
        return open(source, 'rb')
    elif isinstance(source, bytes):
        return io.BytesIO(source)
    else:
        raise TypeError(f'Unsupported source format {type(source)}')
