from pathlib import Path
import os.path
import sys
from ruamel.yaml import YAML
import warnings
from ruamel.yaml.error import ReusedAnchorWarning
import csv

warnings.simplefilter("ignore", ReusedAnchorWarning)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def splitColumns(idcol, itemList, columnNames):
    oldList = list()
    newList = list()
    for item in itemList:
        tempItem = item
        if idcol in item:
            row = dict()
            row[idcol] = item[idcol]
            foundSomeValues = False
            for colName in columnNames:
                if colName in item:
                    row[colName] = item[colName]
                    del tempItem[colName]
                    foundSomeValues = True
            if foundSomeValues:
                newList.append(row)
            if len(tempItem) > 1:
                oldList.append(tempItem)
    return oldList, newList

def parseRuleFile(filename):
    with open(filename) as file:
        yaml = YAML()
        yaml.allow_duplicate_keys = True
        data = list(yaml.load_all(file))
        return data

def handleRuleFile(filename, userKey, idcol, options):
#    print("Trying to parse YAML in " + str(filename))
    data = parseRuleFile(filename)
    for docs in data:
        for key, value in docs.items():
            if key == userKey:
                return splitColumns(idcol, value, options)
    return list()

# USAGE: splitrules "items:costBuy,costSell" merged.rul
# USAGE: splitrules "research-name:cutscene" merged.rul
# USAGE: splitrules 1 "items:costBuy,costSell" merged.rul
# USAGE: splitrules 2 "items:costBuy,costSell" merged.rul

idcol = "type"
outputMode = 0
parseDef = ""
if len(sys.argv) > 3:
    outputMode = int(sys.argv[1])
    path = sys.argv[3]
    parseDef = sys.argv[2]
elif len(sys.argv) > 2:
    path = sys.argv[2]
    parseDef = sys.argv[1]

parts = parseDef.split(":")
key = parts[0]
if "-" in key:
    keyParts = key.split("-")
    key = keyParts[0]
    idcol = keyParts[1]
columnNames = parts[1].split(",")
oldList = list()
newList = list()
if os.path.isfile(path):
    oldList, newList = handleRuleFile(path, key, idcol, columnNames)
yaml=YAML()
yaml.indent(mapping=2, sequence=4, offset=2)
if outputMode == 0:
    yaml.dump({key: oldList}, sys.stdout)
    print("------------------------------------")
    yaml.dump({key: newList}, sys.stdout)
elif outputMode == 1:
    yaml.dump({key: oldList}, sys.stdout)
elif outputMode == 2:
    yaml.dump({key: newList}, sys.stdout)