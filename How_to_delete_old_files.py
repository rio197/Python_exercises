import os
import shutil
import time
import glob

def main():
  # initialize list of files
  du = {}
  
  # specify the path
  path = r"\\somedrive\somefolder"
  
  # specify the days threshold
  days = 40
  
  # convert days to seconds
  # time.time() returns current time in seconds since the epoch
  seconds = time.time() - (days * 24 * 60 * 60)
  
  # check whether the file is present in path or no
  if os.path.exists(path):
    # open the output file in Append mode
    with open ("list_old_files.output.txt","a") as file:
      # use glob
      
  
def get_file_or_folder_age(path):
  # time will be in seconds
  ctime = os.stat(path).st_mtime
  
  # return the time
  return ctime

if __name__ == '__main__':
  main()
