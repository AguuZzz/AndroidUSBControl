import os
from ppadb.client import Client as AdbClient

client = AdbClient()
devices = client.devices()

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠶⠦⡄⠀⠀⠀⠀⠀⠀⡴⠀⠀⠀
⠀⢀⣀⠀⠀⠀⣀⠤⠖⠒⠋⡉⠙⢲⣺⢅⡀⠀⠹⡀⠀⠀⠀⢀⡜⠁⠀⠀⠀
⣼⠉⠀⠉⠓⠏⠁⠀⠀⠀⠀⢯⣧⠈⢿⡆⠈⠓⢴⠇⠀⠀⣠⠊⠀⠀⠀⡀⠀
⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠀⡀⠄⠠⢀⠈⢣⡀⠀⠁⠀⢀⡤⠊⠀⠀
⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⠎⠀⠀⠀⠘⡇⠀⢧⠀⠐⠊⠁⠀⠀⠀        Android Control w USB
⠀⢸⠳⣄⠀⠀⠀⠀⠀⠀⠀⠈⢺⠀⠀⠀⠀⠀⡇⠀⢸⠀⠀⠀⠀⢀⣀⣀⡀       By: AguuZzz
⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣆⠠⠄⢀⡀⢇⠀⢸⡀⠀⡀⠀⠀⠀⠀⠀       Press enter to continue
⠀⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢃⠀⠀⠀⠈⠙⠆⡼⠛⢦⡀⠑⠢⣄⠀⠀
⠀⠀⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡌⠢⣀⠀⢀⡴⡰⠁⠀⢀⡇⠀⠀⠈⠑⠀       You need to have USB depuration actived (Dev Options)
⠀⠀⠀⢸⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠗⠒⠚⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡜⠀⠉⠢⢄⣀⠀⠀⠀⠀⠀⣀⡤⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡇⠀⠀⠀⠀⣨⠟⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⠂⠴⠒⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")
input("")
clear()

#Try to find some device
if devices:
    print("One or more devices found")
    print("-----------------------------------------------------------")
else:
    print("No device found")
    print("-----------------------------------------------------------")

option = input("""Select a option:
1- Send a rickroll         2-Send a text
""")

#Send a rickroll to device
def rickroll():
    inp = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUIcmlja3JvbGw%3D"
    device = devices[0]
    device.shell(f'input text "{inp}"')
    device.shell("input keyevent 66")
    print("-----------------------------------------------------------")
    print("rickroll was send")


#Send a text to device
def texto():
    inp = input("texto: ")
    device = devices[0]
    device.shell(f'input text "{inp}"')
    print("-----------------------------------------------------------")
    print(f'"{inp}" was send')

if option == "1":
    rickroll()
elif option == "2":
    texto()
else:
    print("Error, exit and try again")
    exit
