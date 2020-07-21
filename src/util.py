import os
from datetime import datetime
from dateutil import parser

def parseDateToTimestamp(value):
    """
    Transform Date String into Timestamp Int.

    Args:
        value (str): the datetime to be converted.

    Returns:
        int: corresponding timestamp.
    """

    newDate = parser.parse(value)
    return datetime.timestamp(newDate)

def parseTimestampToDate(value):
    """
    Transform Timestamp Int into Date String.

    Args:
        value (str): the timestamp to be converted.

    Returns:
        int: corresponding datetime.
    """

    newDate = datetime.fromtimestamp(value)
    return newDate.strftime("%Y-%m-%dT%H:%M:%S")

def createFolder(path):
    """
    Create a folder if not exists.

    Args:
        path (str): folder path.
    """

    if not os.path.exists(path):
        os.makedirs(path)
