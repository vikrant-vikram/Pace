from typing import Pattern
import keyboard
import cryptocode
import pyperclip as clipboard

prev_e = " "
clipboard.copy("")  

def clipboard_e(prev_e):
    
    # clipboard.copy("temp")  
    temp = clipboard.paste()  
    if (temp.count("==")<3):
        print("rrr")
        temp = cryptocode.encrypt(temp,"mypassword")
    prev_e  = temp
    clipboard.copy(temp)  # text will have the content of clipboard

def clipboard_d():
    temp = clipboard.paste()  
    temp = cryptocode.decrypt(temp,"mypassword")
    clipboard.copy(temp)  


keyboard.add_hotkey("ctrl+4+e",lambda : clipboard_e(prev_e))
keyboard.add_hotkey("ctrl+4+d", lambda : clipboard_d())

# keyboard.add_abbreviation("@pattern", )

while True:
    pass
    # keyboard.add_abbreviation('@a', "@b")
    # print(list(keyboard.get_typed_strings(events)))
    # keyboard.add_abbreviation('abhishek@786', 'my.long.email@example.com')
    # if keyboard.is_pressed('q'):  # if key 'q' is pressed 
    #     print('You Pressed A Key!')







# try:  # used try so that if user pressed other than the given key error will not be shown
#     if keyboard.is_pressed('q'):  # if key 'q' is pressed 
#         print('You Pressed A Key!')
#         # break  # finishing the loop
# except:
#     print("error")
#     # break  # if user pressed a ke
# @email @email 