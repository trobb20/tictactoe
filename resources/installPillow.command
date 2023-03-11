#!/bin/bash

directory="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd "$directory"

sudo pip install Pillow-3.4.2-cp27-cp27m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl
