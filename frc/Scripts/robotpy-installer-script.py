#!c:\users\robotics\desktop\infiniterecharge2020\frc\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'robotpy-installer==2019.2.0','console_scripts','robotpy-installer'
__requires__ = 'robotpy-installer==2019.2.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('robotpy-installer==2019.2.0', 'console_scripts', 'robotpy-installer')()
    )
