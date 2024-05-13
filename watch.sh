#!/bin/bash

find . -type f | grep -f exts | entr ./compileall.sh
