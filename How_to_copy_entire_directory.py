import os
import shutil

def main():
        source_dir = r"C:\Users\%USERNAME%\Downloads\testfolder"
        destination_dir = r"C:\Users\%USERNAME%\Downloads\test\testfolder"
        copy_entire_directory(source_dir,destination_dir)

def copy_entire_directory(source,destination):
        if os.path.exists(source):
                shutil.rmtree(destination)
                print("Deleted: {}".format(destination)
        shutil.copytree(source, destination)
        print("Replaced: {}".format(destination)

main()
