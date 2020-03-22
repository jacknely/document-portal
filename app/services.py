import mimetypes
import os

import arrow


def format_date_time(date_str):
    """
    takes a datetime string and converts it 'XXX days ago'
    :param date_str: str
    :return: str
    """
    dt = arrow.get(date_str)
    return dt.humanize()


def file_type(key):
    """
    takes a s3 key path and returns file type
    :param key: str
    :return: str
    """
    file_info = os.path.splitext(key)
    file_extension = file_info[1]
    try:
        return mimetypes.types_map[file_extension]
    except KeyError():
        return "Unknown"
    finally:
        return "Unknown"
