import math, re
from textwrap import dedent

sel  = ''
area = 0.0

class clr:
    YELLOW  = '\033[38;5;193m'
    ORANGE  = '\033[38;5;209m'
    ENDC    = '\033[0;0m'

def mainmenu():
    sel = input(dedent(f'''
    Menu:
    1. Calculate triangle area by base {clr.ORANGE}and{clr.ENDC} height
    2. Calculate triangle area by 2 sides {clr.ORANGE}and{clr.ENDC} angle between them
    3. Exit
    Enter menu item number: '''))

    if sel not in ['1', '2', '3']:
        print('\nYou might try to use 1/2/3 numbers')
    else:
        return sel

def submenu(sel):
    if   sel == '1':
        return triangle_by_base()
    elif sel == '2':
        return triangle_by_twos()
    else:
        print('Goodbye!')
        exit()

def triangle_by_base():
    i = re.findall(r'\b(\d+)\b', input('Enter base and height: '))
    if len(i) == 2 and all(int(v) > 0 for v in i ):
        b, h = map(int, i)
        area = b*h/2
    else:
        area = 'doomed'
    return area

def triangle_by_twos():
    i = re.findall(r'\b(\d+)\b', input('Enter 2 sides and angle(degrees) between them: '))
    if len(i) == 3 and all(int(v) > 0 for v in i ):
        a, b, angle = map(int, i)
        area = a*b*math.sin(math.radians(angle))/2
    else:
        area = 'doomed'
    return area

print(f'Welcome {clr.ORANGE}to{clr.ENDC} the triangle {clr.YELLOW}area{clr.ENDC} calculation tool.')
while True:
    result = submenu(mainmenu())
    print('Area is:', result)
