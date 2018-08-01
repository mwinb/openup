import os
import sys
import platform
import subprocess

def main():
    if len(sys.argv)-1 >= 1:
        try:
            toRun = sys.argv[1]
            programOpen(toRun)
        except Exception:
            print "----Invalid Command----"
    else:
        print "----Please pass file to open----"
        raise SystemExit
 
def programOpen(progToRun):
    if platform.system() == "Windows":
        os.startfile(progToRun)
    elif platform.system() == "Linux":
        subprocess.Popen(["xdg-open", progToRun])
    else:
        subprocess.Popen(["open", path])
main()
