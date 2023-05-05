#!/bin/bash

### ABSOLUTE PATH
cd "${HOME}/develop/moving_market" || exit
source .venv/bin/activate
cd docs/ || exit
make clean html
rm source/mktsim_jk*
(cd ../market-simulator-package || exit; sphinx-apidoc -f -d 5 -o ../docs/source mktsim_jk/)
make html
