import os
from datetime import datetime
from dateutil import parser

# Transforma Date String em Timestamp Int
def parseDateToTimestamp(value):
    newDate = parser.parse(value)
    return datetime.timestamp(newDate)

# Transforma Timestamp Int em Date String
def parseTimestampToDate(value):
    newDate = datetime.fromtimestamp(value)
    return newDate.strftime("%Y-%m-%dT%H:%M:%S")

# Cria a Pasta se Ainda Não Existir
def createFolder(path):
    
    if not os.path.exists(path):
        os.makedirs(path)