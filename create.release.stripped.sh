#!/bin/bash
if bumpversion $@ --tag --commit; then
    cd ..
    7z a -r -xr@./Vigilo_Confido/release.stripped.exclude Vigilo_Confido_S.zip Vigilo_Confido/
    cd Vigilo_Confido
fi