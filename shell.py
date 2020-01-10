import os
import signal

def getuser():
     userhome = os.path.expanduser('~')
     return os.path.split(userhome)[-1].strip()
user = getuser()

for i in range(1, 2):
  import threading
  import colors
  import pty
  def shell():
        while 1:
                print("\033[36m")
                help = """
This is a python restricted shell, developed by 60x.
You can install it here: https://github.com/60x/Python-RestrictedShell

This is just an example of the use of a restricted shell.
You can add more commands as you please; the current commands are help, ls and clear.
Any other input will output an error message.
"""
                try:
                        comm = raw_input("[Restricted Shell > ] " )
                except: comm = "shell"

                if comm.lower().strip() == "help":
                 print help

                elif comm.lower().strip() == "l" or comm.lower().strip() =="ls":
                 os.system('ls')

                elif comm.lower().strip() == "clear":
                 os.system('clear')

                else:
                 print("This is a restricted shell.")
user = getuser()
if user.lower() == "shell":
        threading.Thread(target=shell).start()
else: threading.Thread(target=shell).start()
