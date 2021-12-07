import os
import shutil

source_dir = r"C:\Users\%USERNAME%\Downloads\testfolder"
destination_dir = r"C:\Users\%USERNAME%\Downloads\test\testfolder"

if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)

shutil.copytree(source_dir, destination_dir)
