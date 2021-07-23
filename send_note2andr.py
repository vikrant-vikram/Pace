import os 
import time

def push_configure():
    os.system('notify-run register')
# time.sleep(2)

def send_push_msg(data):

    # data= "configure test"
    cmnd="notify-run send"
    f= cmnd+" '"+data+"'"
    os.system(f)


# while True:
#     f= cmnd+" '"+data+"'"
#     print(f)
#     os.system(f)
#     data = input()