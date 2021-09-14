import os
import sys



if '-u' in sys.argv:
    if not 'CONFIRM_UPGRADE' in os.environ or not os.environ['CONFIRM_UPGRADE'] in ('1', 'true'):
        print("The update has been cancelled.\n"
"If you are 100% sure that your update does not reset existing data "
"that has been manually changed and has noupdate set to 0, set "
"environment variable CONFIRM_UPDATE=1 to confirm that that is really "
"what you want to do.", file=sys.stderr)
        sys.exit(1)
