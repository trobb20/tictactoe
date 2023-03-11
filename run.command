#!/bin/bash

directory="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd "$directory"

cd resources

python ticTacToe.py

killall Preview