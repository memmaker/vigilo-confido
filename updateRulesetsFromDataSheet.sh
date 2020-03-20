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

ods2csv CSV_Manufacture data.sheet.ods > ./csv_data/manufacture.csv
patchrules manufacture csv_data/manufacture.csv ${MODPATH}

ods2csv CSV_Research data.sheet.ods > ./csv_data/research.csv
patchrules research csv_data/research.csv ${MODPATH}
