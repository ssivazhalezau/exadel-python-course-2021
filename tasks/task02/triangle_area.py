import math, re
from textwrap import dedent

class clr:
    YELLOW  = '\033[38;5;193m'
    ORANGE  = '\033[38;5;209m'
    ENDC    = '\033[0;0m'

def mainmenu():
    m  = ''
    while m not in ['1', '2', '3']:
        m = input(dedent(f'''
        Menu:
        1. Calculate triangle area by base {clr.ORANGE}and{clr.ENDC} height
        2. Calculate triangle area by 2 sides {clr.ORANGE}and{clr.ENDC} angle between them
        3. Exit
        Enter menu item number: '''))
        if m in ['1', '2', '3']:
            break
        print('\nYou might try to use 1/2/3 numbers')
    return m

def submenu(s):
    if   s == '1':
        return triangle_by_base()
    elif s == '2':
        return triangle_by_twos()
    else:
        print('Goodbye!')
        exit()

def triangle_by_base():
    """
    We calculate triangle area by base and height.
    Please enter base and height as integers separated by space or comma
    """

    while True:
        try:
            i = re.findall(r'\b(\d+)\b', input('Enter base and height: '))
            # if len(i) == 2 and all(int(v) > 0 for v in i ):
            if all(int(v) > 0 for v in i ):
                b, h = map(int, i)
                area = b*h/2
                return area
        except KeyboardInterrupt:
            print('')
            exit(0)
        except:
            print(dedent(triangle_by_base.__doc__), '\nPlease try again.')

def triangle_by_twos():
    """
    We calculate triangle area by 2 sides and angle between them.
    Please enter two sizes value followed by angle as integers separated by space or comma
    """

    while True:
        try:
            i = re.findall(r'\b(\d+)\b', input('Enter 2 sides and angle(degrees) between them: '))
            if all(int(v) > 0 for v in i ):
                a, b, angle = map(int, i)
                area = a*b*math.sin(math.radians(angle))/2
                return area
        except KeyboardInterrupt:
            print('')
            exit(0)
        except:
            print(dedent(triangle_by_base.__doc__), '\nPlease try again.')

print(f'Welcome {clr.ORANGE}to{clr.ENDC} the triangle {clr.YELLOW}area{clr.ENDC} calculation tool.')
while True:
    result = submenu(mainmenu())
    print('Area is:', result)
