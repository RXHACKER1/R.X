###__IMPORT__###
import os , time
 
###__COLOURS__###

GREEN ='\x1b[38;5;46m'
RED = '\x1b[38;5;196m' 
WHITE = '\033[1;97m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"

logo =(f'''{YELLOW}
    ██████      ██   ██     
    ██   ██      ██ ██      
    ██████        ███       
    ██   ██      ██ ██      
    ██   ██     ██   ██     ''')

menu =  (f'''{GREEN}
[1] Termux Setup 
[2] Contact Me 
[3] Exit 
''')

def setup ():
	os.system ("pkg update -y && pkg upgrade -y && pkg install git -y &&pkg install python -y && pkg install python2 -y && pkg install python3 -y && pkg install curl -y && pkg install wget -y && pip install requests  mechanize bs4 && termux-setup-storage")

def contact ():
	os.system ("xdg-open https://www.facebook.com/meraju1RX")

def main():
	os.system ('clear')
	print (logo)
	print ('')
	print (menu)
	option=input (f'{BLUE}Choose Option:{WHITE}')
	if option=='1':
		setup ()
		main ()
	elif option=='2':
		contact ()
		main ()
	elif option=='3':
		exit ()


main()
 