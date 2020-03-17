import csv
import sys

from pathlib import Path
import os.path
from ruamel.yaml import YAML
import warnings
from ruamel.yaml.error import ReusedAnchorWarning

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def findId(item):
    possible = ["type", "name", "id"]
    for id in possible:
        if id in item:
            return id
    return "ID_NOT_FOUND"

def parseRuleFile(filename):
    with open(filename) as file:
        yaml = YAML()
        yaml.allow_duplicate_keys = True
        data = list(yaml.load_all(file))
        return data

def listToMap(itemList):
    itemMap = dict()
    for item in itemList:
        idcol = findId(item)
        itemMap[item[idcol]] = item
    return itemMap

def handleRuleFile(filename, userKey):
#    print("Trying to parse YAML in " + str(filename))
    data = parseRuleFile(filename)
    for docs in data:
        for key, value in docs.items():
            if key == userKey:
                if isinstance(value, list):
                    return listToMap(value)
    return list()

# USAGE: patchrules items patchData.csv targetRules.rul
def mergeNode(oldNode, newNode):
    mergedNode = oldNode
    for key, value in newNode.items():
        if key in mergedNode and isinstance(value, dict):
            mergedNode[key] = mergeNode(mergedNode[key], value) # value is a dict, merge recursively
        else:
            mergedNode[key] = value # value defined twice, use last definition
    return mergedNode


if len(sys.argv) > 1:
    key = sys.argv[1]
    csvFilename = sys.argv[2]
    rulFilename = sys.argv[3]
    itemMap = dict()
    if os.path.isfile(rulFilename):
        itemMap = handleRuleFile(rulFilename, key)

    if os.path.isfile(csvFilename):
        with open(csvFilename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            columnDefinitions = dict()
            columnLookup = dict()
            idcol = "type"
            for row in csv_reader:
                if line_count == 0:
                    columnDefinitions = row
                    idcol = columnDefinitions[0]
                    for i in range(0,len(row)):
                        columnLookup[row[i]] = i
                    line_count += 1
                else:
                    nodeObject = {idcol: row[columnLookup[idcol]]}
                    for i in range(0,len(row)):
                        if i == columnLookup[idcol]:
                            continue
                        value = row[i]
                        if len(value) > 0:
                            if is_number(value):
                                value = float(value)
                                if value.is_integer():
                                    value = int(value)
                            if '-' in columnDefinitions[i]:
                                parts = columnDefinitions[i].split('-')
                                if parts[0] in nodeObject and type(nodeObject[parts[0]]) is list:
                                    nodeObject[parts[0]].append(value)
                                else:
                                    subNode = list()
                                    subNode.append(value)
                                    nodeObject[parts[0]] = subNode
                            elif '.' in columnDefinitions[i]:
                                parts = columnDefinitions[i].split('.')
                                if parts[0] in nodeObject and type(nodeObject[parts[0]]) is dict:
                                    nodeObject[parts[0]][parts[1]] = value
                                else:
                                    subNode = dict()
                                    subNode[parts[1]] = value
                                    nodeObject[parts[0]] = subNode
                            else:
                                nodeObject[columnDefinitions[i]] = value
                    if len(nodeObject) > 1:
                        itemMap[row[columnLookup[idcol]]] = mergeNode(itemMap[row[columnLookup[idcol]]], nodeObject)
                    line_count += 1
        yaml=YAML()
        yaml.indent(mapping=2, sequence=4, offset=2)
        yaml.dump({key: list(itemMap.values())}, sys.stdout)
