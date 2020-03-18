#!/bin/bash

mkdir -p csv_data

MODPATH="./Ruleset/"

if test -f "$1"; then
    MODPATH=$1
fi

ods2csv CSV_Units data.sheet.ods > ./csv_data/units.csv
patchrules units csv_data/units.csv ${MODPATH}

ods2csv CSV_Items data.sheet.ods > ./csv_data/items.csv
patchrules items csv_data/items.csv ${MODPATH}

ods2csv CSV_Armors data.sheet.ods > ./csv_data/armors.csv
patchrules armors csv_data/armors.csv ${MODPATH}
