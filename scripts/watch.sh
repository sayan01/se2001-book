#!/bin/bash

find . -type f | grep -f <(
cat <<EOF
\.tex$
\.sty$
\.cls$
\.bib$
\.jpe\?g$
\.png$
\.svg$
\.sh$
EOF
) | entr ./compile.sh
