#!f:\2_work\20_study\208_assignment\assignment\black-jack-game-env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Django==1.11','console_scripts','django-admin'
__requires__ = 'Django==1.11'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Django==1.11', 'console_scripts', 'django-admin')()
    )
