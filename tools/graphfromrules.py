from pathlib import Path
import os.path
import sys
from ruamel.yaml import YAML
import warnings
from ruamel.yaml.error import ReusedAnchorWarning
import csv
from graphviz import Digraph
from pprint import pprint

warnings.simplefilter("ignore", ReusedAnchorWarning)

def findId(item):
    possible = ["type", "name", "id"]
    for id in possible:
        if id in item:
            return id
    return "ID_NOT_FOUND"

def getAttributes(item, fieldNames):
    attribs = dict()
    for i in fieldNames:
        if i in item:
            attribs[i] = str(item[i])
    return attribs

def graphColumns(idcol, itemList, columnNames, attribNames):
    dot = Digraph(comment='Ruleset Graph')
    for item in itemList:
        if not idcol in item:
            idcol = findId(item)
        if idcol in item:
            rowid = item[idcol]
            attributes = getAttributes(item, attribNames)
            dot.node(rowid, rowid, **attributes)
            for colName in columnNames:
                if colName in item:
                    if isinstance(item[colName], list):
                        for i in item[colName]:
                            dot.edge(rowid, i, colName)
                    else:
                        dot.edge(rowid, item[colName], colName)
    return dot

def parseRuleFile(filename):
    with open(filename) as file:
        yaml = YAML()
        yaml.allow_duplicate_keys = True
        data = list(yaml.load_all(file))
        return data

def handleRuleFile(filename, userKey, idcol, options, attribNames):
#    print("Trying to parse YAML in " + str(filename))
    data = parseRuleFile(filename)
    for docs in data:
        for key, value in docs.items():
            if key == userKey:
                return graphColumns(idcol, value, options, attribNames)
    return list()

# USAGE: graphfromrules "research:dependencies,unlocks" "cost,points" rulefile.rul

if len(sys.argv) > 1:
    idcol = "type"
    path = sys.argv[3]
    attribNames = sys.argv[2].split(',')
    parseDef = sys.argv[1]
    parts = parseDef.split(":")
    key = parts[0]
    if "-" in key:
        keyParts = key.split("-")
        key = keyParts[0]
        idcol = keyParts[1]
    columnNames = parts[1].split(",")
    if os.path.isfile(path):
        dotGraph = handleRuleFile(path, key, idcol, columnNames, attribNames)
        targetName = os.path.splitext(os.path.basename(path))[0] + '.gv'
        print(dotGraph.source)
