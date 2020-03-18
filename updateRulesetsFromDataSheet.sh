#!/bin/bash

ods2csv CSV_Units data.sheet.ods > ./csv_data/units.csv
patchrules units csv_data/units.csv ./Ruleset/

ods2csv CSV_Items data.sheet.ods > ./csv_data/items.csv
patchrules items csv_data/items.csv ./Ruleset/

ods2csv CSV_Armors data.sheet.ods > ./csv_data/armors.csv
patchrules armors csv_data/armors.csv ./Ruleset/
