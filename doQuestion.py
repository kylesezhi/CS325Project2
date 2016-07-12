#!/usr/bin/env python

import sys
from helpers import doQuestion
from changegreedy import changegreedy
from changedp import changedp

doQuestion(sys.argv[1], changegreedy)
doQuestion(sys.argv[1], changedp)
