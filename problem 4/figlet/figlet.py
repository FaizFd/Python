from pyfiglet import Figlet
import sys
import random

figlet = Figlet()


if len(sys.argv) == 3:

    if (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        for font in figlet.getFonts():
            figlet.setFont(font=sys.argv[2])
            response = input('Input: ')
            print('Output:\n', figlet.renderText(response))
            break
    else:
        sys.exit('Invalid usage')

elif len(sys.argv) < 2:
    figlet.setFont(font=random.choice(figlet.getFonts()))
    response = input('Input: ')
    print('Output:\n', figlet.renderText(response))
else:
    sys.exit('Invalid usage')