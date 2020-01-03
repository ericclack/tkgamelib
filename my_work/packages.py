# Copyright 2019, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

import sys, os

def parent(path): return os.path.split(path)[0]

project_path = parent(parent(__file__))
sys.path.append(project_path)

from tkgamelib import *
from tkgamelib.sound import *