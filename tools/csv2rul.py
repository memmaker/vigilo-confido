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

if len(sys.argv) > 1:
    filename = sys.argv[1]
    yaml=YAML()
    yaml.indent(mapping=2, sequence=4, offset=2)
#    yaml.default_flow_style = False
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        itemList = list()
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
                    itemList.append(nodeObject)
                line_count += 1
        name = os.path.splitext(os.path.basename(filename))[0]
        yaml.dump({name: itemList}, sys.stdout)
