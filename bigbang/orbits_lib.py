# Copyright 2019, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General
# Public License

from geekclub_packages import *


def say(s, *args, **kwargs):
    banner(s, *args, fill="white", **kwargs)

def delete_all(spritelist):
    while spritelist:
        spritelist.pop().delete()

# ------------------------------------------------------------------

