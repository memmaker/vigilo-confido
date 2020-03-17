from pathlib import Path
import os.path
import sys
from ruamel.yaml import YAML
import warnings
from ruamel.yaml.error import ReusedAnchorWarning
import csv

warnings.simplefilter("ignore", ReusedAnchorWarning)

def dumpColumns(idcol, itemList, columnNames):
    allRows = list()
    for item in itemList:
        if idcol in item:
            row = list()
            row.append(item[idcol])
            foundSomeValues = False
            subListIndex = 0
            for colName in columnNames:
                colFound = False
                if '.' in colName:
                    parts = colName.split('.')
                    if parts[0] in item:
                        subNode = item[parts[0]]
                        if parts[1] in subNode:
                            row.append(subNode[parts[1]])
                            foundSomeValues = True
                            colFound = True
                if '-' in colName:
                    # we got a list
                    parts = colName.split('-')
                    if parts[0] in item and subListIndex < len(item[parts[0]]):
                        row.append(item[parts[0]][subListIndex])
                        foundSomeValues = True
                        colFound = True
                    subListIndex += 1
                if colName in item:
                    row.append(item[colName])
                    foundSomeValues = True
                    colFound = True
                if not colFound:
                    row.append(None)
            if foundSomeValues:
                allRows.append(row)
    return allRows

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
                return dumpColumns(idcol, value, options)
    return list()

# USAGE: rul2csv "items:costBuy,costSell" [PATH_TO_MOD_DIR_WITH_RUL_FILES]
# USAGE: rul2csv "units:stats.tu,stats.health" [PATH_TO_MOD_DIR_WITH_RUL_FILES]
# USAGE: rul2csv "armors:damageModifier-none,damageModifier-armorpierce" [PATH_TO_MOD_DIR_WITH_RUL_FILES]
# USAGE: rul2csv "research-name:cutscene" [PATH_TO_MOD_DIR_WITH_RUL_FILES]

if len(sys.argv) > 1:
    idcol = "type"
    path = sys.argv[2]
    parseDef = sys.argv[1]
    parts = parseDef.split(":")
    key = parts[0]
    if "-" in key:
        keyParts = key.split("-")
        key = keyParts[0]
        idcol = keyParts[1]
    columnNames = parts[1].split(",")
    if os.path.isfile(path):
        allRows = handleRuleFile(path, key, idcol, columnNames)
    else:
        allRows = list()
        for filename in Path(path).rglob('*.rul'):
            allRows = allRows + handleRuleFile(filename, key, idcol, columnNames)
    firstRow = columnNames
    firstRow.insert(0, idcol)
    allRows.insert(0, firstRow)
    writer = csv.writer(sys.stdout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in allRows:
        writer.writerow(row)