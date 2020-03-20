#!/bin/bash

MODPATH="./Ruleset/"

if test -f "$1"; then
    MODPATH=$1
fi

rul2ods ${MODPATH} CSV_Items data.sheet.ods
rul2ods ${MODPATH} CSV_Armors data.sheet.ods
rul2ods ${MODPATH} CSV_Units data.sheet.ods
rul2ods ${MODPATH} CSV_Research data.sheet.ods
rul2ods ${MODPATH} CSV_Manufacture data.sheet.ods
