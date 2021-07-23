# PACE a virtual clipboard 


# This programm handels core functionality of pace such as copy paste and encryption part
#import alll required libraryies
# pyfirmata for serial communication with the arduinmo
# time have been used to give some delay to  the progamm

import pyfirmata
import time
import os
import platform
import clipboard
from typing import Pattern
import keyboard
import cryptocode
import pyperclip as clipboard
import send_note2andr as push

prev_e = " "
clipboard.copy("")  

datastack = ["" for i in range(6)]
password_manager = {}


CRED = '\033[91m'
CEND = '\033[0m'
CBLINK = "\033[5m"





print(CBLINK + "------------------PACE------------------------------"+CEND)

print( CRED +
'''
===============SHORTCUTS===============
push_pattern             = "ctrl+g+p"
copy_in_stack_pattern1    = "ctrl+g+1"
copy_in_stack_pattern2    = "ctrl+g+2"
copy_in_stack_pattern3    = "ctrl+g+3"
copy_in_stack_pattern4   = "ctrl+g+4"
copy_in_stack_pattern5    = "ctrl+g+5"
paste_from_stacl_pattern1 = "ctrl+0+1"
paste_from_stacl_pattern2 = "ctrl+0+2"
paste_from_stacl_pattern3 = "ctrl+0+3"
paste_from_stacl_pattern4 = "ctrl+0+4"
paste_from_stacl_pattern5 = "ctrl+0+5"
encrypt_pattern          = "ctrl+g+e"
decrypt_pattern          = "ctrl+g+d"
save_passwoed_pattern    = "ctrl+g+s"
retrive_password_pattern = "ctrl+g+r"
setup_push_pattern       = "ctrl+g+n"
show_password_pattern    = "ctrl+g+m"
print_stack_pattern      = "ctrl+g+0"
paste_pattern            = "ctrl+g+"

=======================================''' + CEND)
# ---------------------trigger methods----------------------------------


def push_message():
    #copy data from clipborad and send push notification to user
    push.send_push_msg(clipboard.paste())

def clipboard_e():
    #Take clipboard data and rncrypt it
    # clipboard.copy("temp")  
    temp = clipboard.paste()  
    if (temp.count("==")<3):
        print("rrr")
        temp = cryptocode.encrypt(temp,"mypassword")
    # prev_e  = temp
    clipboard.copy(temp)  # text will have the content of clipboard

def clipboard_d():
    # take clipboard data and dycrypt it
    temp = clipboard.paste()  
    temp = cryptocode.decrypt(temp,"mypassword")
    clipboard.copy(temp)  

def copytostack1():
    # copy data in stack1
    temp = clipboard.paste() 
    datastack[1] = temp

def copytostack2():
    # copy data in stack1
    temp = clipboard.paste() 
    datastack[2] = temp

def copytostack3():
    # copy data in stack1
    temp = clipboard.paste() 
    datastack[3] = temp

def copytostack4():
    # copy data in stack1
    temp = clipboard.paste() 
    datastack[4] = temp

def copytostack5():
    # copy data in stack1
    temp = clipboard.paste() 
    datastack[5] = temp


def pastefromstack1():
    # copy data from stack of index *
    clipboard.copy(datastack[1])

def pastefromstack2():
    # copy data from stack of index *
    clipboard.copy(datastack[2])

def pastefromstack3():
    # copy data from stack of index *
    clipboard.copy(datastack[3])

def pastefromstack4():
    # copy data from stack of index *
    clipboard.copy(datastack[4])

def pastefromstack5():
    # copy data from stack of index *
    clipboard.copy(datastack[5])

def print_stack():
    # print whole stack
    clipboard.copy(str(datastack))

def save_password():
    #save username and password
    username = clipboard.paste()
    while True:
        password = clipboard.paste()
        if(username != password):
            password_manager[username] = password
            break

def retrive_password():
    # retrive username usinf password
    try:

        clipboard.copy(password_manager[clipboard.paste()])
    except:
        clipboard.copy("no data found with given username : " )


def setup_push():
    # when first we wwant to setup push notification then need to run
    print("configration started")
    push.push_configure()

def show_password():
    # show all password stored inside the password manager
    clipboard.copy(str(password_manager))

print("Reached board retup")
# Set environment to communicate with the arduino Uno
# start communication
print("--------------------Arduino setup started ----------------------------")
board = pyfirmata.Arduino('/dev/ttyACM0')
it = pyfirmata.util.Iterator(board)
it.start()
board.digital[10].mode = pyfirmata.INPUT
#-------------------------------------------------- set varialbles----------------------------------------------------------------------------------------
virtual_clipboard_path_linux = "/media/mountDrive"
virtu_clipboard_path_windows = ""
dir_path = ""

print("--------------------- Arduino setup completed---------------------------")




# function to detect the operating system and set path for PACE stirage are
def  detect_os():
    if(platform.system()=="Linux"):
        dir_path = virtual_clipboard_path_linux
    else:
        dir_path = virtu_clipboard_path_windows


# set patterns
push_pattern             = "ctrl+g+p"
copy_in_stack_pattern1    = "ctrl+g+1"
copy_in_stack_pattern2    = "ctrl+g+2"
copy_in_stack_pattern3    = "ctrl+g+3"
copy_in_stack_pattern4   = "ctrl+g+4"
copy_in_stack_pattern5    = "ctrl+g+5"
paste_from_stacl_pattern1 = "ctrl+0+1"
paste_from_stacl_pattern2 = "ctrl+0+2"
paste_from_stacl_pattern3 = "ctrl+0+3"
paste_from_stacl_pattern4 = "ctrl+0+4"
paste_from_stacl_pattern5 = "ctrl+0+5"
encrypt_pattern          = "ctrl+g+e"
decrypt_pattern          = "ctrl+g+d"
save_passwoed_pattern    = "ctrl+g+s"
retrive_password_pattern = "ctrl+g+r"
setup_push_pattern       = "ctrl+g+n"
show_password_pattern    = "ctrl+g+m"
print_stack_pattern      = "ctrl+g+0"
paste_pattern            = "ctrl+g+"



# ----------------------adding hotkeys---------------------------------
keyboard.add_hotkey(push_pattern,lambda : push_message()) 
keyboard.add_hotkey(print_stack_pattern ,lambda : print_stack())
keyboard.add_hotkey(copy_in_stack_pattern1,lambda : copytostack1())
keyboard.add_hotkey(copy_in_stack_pattern2,lambda : copytostack2())
keyboard.add_hotkey(copy_in_stack_pattern3,lambda : copytostack3())
keyboard.add_hotkey(copy_in_stack_pattern4,lambda : copytostack4())
keyboard.add_hotkey(copy_in_stack_pattern5,lambda : copytostack5())
keyboard.add_hotkey(paste_from_stacl_pattern1,lambda : pastefromstack1())
keyboard.add_hotkey(paste_from_stacl_pattern2,lambda : pastefromstack2())
keyboard.add_hotkey(paste_from_stacl_pattern3,lambda : pastefromstack3())
keyboard.add_hotkey(paste_from_stacl_pattern4,lambda : pastefromstack4())
keyboard.add_hotkey(paste_from_stacl_pattern5,lambda : pastefromstack5())
keyboard.add_hotkey(encrypt_pattern,lambda : clipboard_e())
keyboard.add_hotkey(decrypt_pattern,lambda : clipboard_d())
keyboard.add_hotkey(save_passwoed_pattern,lambda : save_password())
keyboard.add_hotkey(retrive_password_pattern,lambda : retrive_password())
keyboard.add_hotkey(setup_push_pattern,lambda : setup_push())
keyboard.add_hotkey(show_password_pattern ,lambda : show_password())



# def find_pattern( *data_from_board ):
#     # the are total 2^10 combinations 1024
#     # Means 1024 functionality we can provide current we provide only limited features
#     for i in data_from_board:
#         if (i== True):
#             return "pattern_" + (i+1)

while True:
    l = []
    # Read all data of input pins of ardiono from 1 to 10
    #These data shows which task machine should perform when user doesnot remember shortcuts
    sw_10 = board.digital[10].read()
    sw_9 = board.digital[9].read()
    sw_8 = board.digital[8].read()
    sw_7 = board.digital[7].read()
    sw_6 = board.digital[6].read()
    sw_5 = board.digital[5].read()
    sw_4 = board.digital[4].read()
    sw_3 = board.digital[3].read()
    sw_2 = board.digital[2].read()
    # sw_1 = board.digital[1].read()
    # print("reached here")

    # try:  # used try so that if user pressed other than the given key error will not be shown
    #     if keyboard.is_pressed('q'):  # if key 'q' is pressed 
    #         print('You Pressed A Key!')
    #         # break  # finishing the loop
    # except:
    #     print("error")
        # break  # if user pressed a key other than the given key the loop will break


    # get pattern of input

    # set patterns





    # if sw is True:

    #     board.digital[13].write(1)

    # else:

    #     board.digital[13].write(0)

    # time.sleep(0.1)