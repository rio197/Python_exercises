# Reference: https://stackoverflow.com/questions/12485666/python-deleting-all-files-in-a-folder-older-than-x-days

#!"C:\Python39\python.exe"
import os
import time
    
path = r"c:\users\%USERNAME%\downloads"
now = time.time()
filelist = []

################################################
# 1- List those files that are older than 7 days
################################################
for f in os.listdir(path):
    fullPath = os.path.join(path, f)
    if os.stat(fullPath).st_mtime < now - 7 * 86400 and os.path.isfile(fullPath):
            fileList.append(fullPath)

if not fileList:
    print("##############################################")
    print("No files older than 7 days have been detected.")
    print("##############################################")
##################################################################################
# 2- Delete those files that are older than 7 days
# WARNING: Do not execute this block unless you really want to delete those files!
##################################################################################
else:
    print("############################################")
    print("The following file(s) are older than 7 days:")
    print("############################################")
    for f in fileList:
        print(f)

    while True:
        try:
            text = input('\nPress Enter to delete the above files or Ctrl-C to cancel:\n')
            if text == "":
                for f in fileList:
                    print("Deleting {}".format(f))
                    os.remove(f)
                break
        except KeyboardInterrupt:
            print("####################################################")
            print("NOTIFICATION: Cancelled. No files have been deleted.")
            print("####################################################")
            break
