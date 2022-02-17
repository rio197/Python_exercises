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
      # use the glob module
      ii = 1
      # define the path to search in
      for filepath in glob.iglob(r"\\somedrive\somefolder",recursive=True):
        if ii = 100:
          break
        if os.path.isfile(filepath) and seconds >= get_file_or_folder_age(filepath) and os.path.getsize(filepath) > 5000000:
          filesize = os.path.getsize(filepath)
          du[filepath] = filesize
          print("Deleting file {} {}".format(filepath,filesize))
          file.write("Deleting file {} {}".format(filepath,filesize))
          os.remove(filepath)
          ii += 1
      
      if not du:
        print("No files had been deleted since none are older than {} days and larger than 5,000,000 bytes had been found".format(days))
      else:
          #Sort the dictionary by value in reverse and print to standard output
          for jj in sorted (du.items)_, key = lambda kv:(kv[1], kv[0], reverse=True)):
            print(jj)
            # Example of writing a tuple into a file
            # https://stackoverflow.com/questions/8366276/writing-a-list-of-tuples-to-a-text-file-in-python
            #
            # for t in some_list:
            #   f.write(' '.join(str(s) for s in t) + '\n')
            file.write(' '.join(str(s) for s in jj) + '\n')
  
  else:
    # file/folder is not found
    print(f'"{path}" is not found')
  
def get_file_or_folder_age(path):
  # time will be in seconds
  ctime = os.stat(path).st_mtime
  
  # return the time
  return ctime

if __name__ == '__main__':
  main()
