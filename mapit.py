

import webbrowser, sys, pyperclip

sys.argv    # [mapit.py', '870', 'Valenica', 'St.']

# Check if command line arguments were passed
if len(sys.argv) > 1:
    # [mapit.py', '870', 'Valenica', 'St.'] --> ' 870 Valencia St.'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# URL we want to access
# https://www.google.com/maps/place/870+Valencia+St,+San+Francisco,+CA+94110,+USA/.......
# check if shorter URL works
# check if only address string on back end works
# valid URL for example = https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)
