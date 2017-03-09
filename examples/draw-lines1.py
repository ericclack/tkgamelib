# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

import sys
sys.path.append('..')
from geekclub.pyscratch import *

create_canvas()

for x in range(0, 500, 4):
    canvas().create_line(x,0, 500-x,500)

mainloop()
