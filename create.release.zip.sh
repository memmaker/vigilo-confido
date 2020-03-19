#!/bin/bash

if bumpversion $@ --tag --commit; then
    cd ..
    7z a -r -xr@./Vigilo_Confido/release.exclude Vigilo_Confido.zip Vigilo_Confido/
    cd Vigilo_Confido
fi