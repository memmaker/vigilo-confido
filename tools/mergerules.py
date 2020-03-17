from pathlib import Path
import os.path
import sys
from ruamel.yaml import YAML
import warnings
from ruamel.yaml.error import ReusedAnchorWarning
from pprint import pprint

warnings.simplefilter("ignore", ReusedAnchorWarning)

def mergeNode(oldNode, newNode):
    mergedNode = oldNode
    for key, value in newNode.items():
        if key in mergedNode and isinstance(value, dict):
            mergedNode[key] = mergeNode(mergedNode[key], value) # value is a dict, merge recursively
        else:
            mergedNode[key] = value # value defined twice, use last definition
    return mergedNode

def mergeNodes(oldItems, newItems):
    entries = dict()
    idcol = "type"
    for item in oldItems:
        if "delete" in item:
            continue
        if not "type" in item and "name" in item:
            idcol = "name"
        entries[item[idcol]] = item
    for item in newItems:
        if "delete" in item:
            continue
        if not "type" in item and "name" in item:
            idcol = "name"
        itemId = item[idcol]
        if itemId in entries:
            entries[itemId] = mergeNode(entries[itemId], item)
        else:
            entries[itemId] = item
    return list(entries.values())

def parseRuleFile(filename):
    with open(filename) as file:
        yaml = YAML()
        yaml.allow_duplicate_keys = True
        data = list(yaml.load_all(file))
        return data

def handleRuleFile(filename, userKey):
    data = parseRuleFile(filename)
    for docs in data:
        for key, value in docs.items():
            if key == userKey:
                return value
    return list()

# USAGE: mergerules items file1.rul file2.rul file3.rul (...)
# USAGE: mergerules items path
key = "items"
items = list()
if len(sys.argv) == 3:
    key = sys.argv[1]
    path = sys.argv[2]
    if os.path.isdir(path):
        for filename in sorted(Path(path).rglob('*.rul')):
            newItems = handleRuleFile(filename, key)
            items = mergeNodes(items, newItems)
elif len(sys.argv) > 3:
    key = sys.argv[1]
    for i in range(2, len(sys.argv)):
        filename = sys.argv[i]
        newItems = handleRuleFile(filename, key)
        items = mergeNodes(items, newItems)
yaml = YAML()
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.dump({ key: items }, sys.stdout)