#!/usr/bin/env python

from subprocess import call

call("cat requirements.txt | xargs -n 1 pip install", shell=True)
