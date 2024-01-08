
from os import scandir , rename , mkdir , stat , remove
from os.path import splitext , join , exists , getctime
from shutil import move
from datetime import datetime

from Cocoa import NSWorkspace , NSImage 

#! pip3  install pyobjc-core pyobjc-framework-Cocoa

##Folder and file structure 
dic={
   'image':['.png','.jpg','.jpeg','.tiff','.dwg'],
   'documents':['.pdf','.doc','.docx','.csv','.xlsx','.xls'],
   'code':['.cpp','.c','.rs','.java','.cs','.swift','.html','.css','.js'],
   'text':['.txt','.log','.dat','.key'],
   'video':['.mp3','.mov','.mp4','.gif','.mkv'],
   'icon':['.ico','.icns']
}


## Cleanup threshold 
WEEK_THRESHOLD = 7


## Set the icon to the folders 
def set_icon(folder_name , sourcedir):
   icon_path = f"{sourcedir}/{folder_name}/Icon\r"
   if not exists(icon_path):
      icon_image = f"{sourcedir}/icon/{folder_name}.png"
      folder_path = f"{sourcedir}/{folder_name}"
      if exists(icon_image):
         NSWorkspace.sharedWorkspace().setIcon_forFile_options_(NSImage.alloc().initWithContentsOfFile_(icon_image), folder_path, 0)
   return None 

## Is file empty for so long .
def is_unecessary(file_path):
   creation_time = getctime(file_path)

   # Convert the creation time to a human-readable format
   creation_datetime = datetime.fromtimestamp(creation_time)
   
   current_datetime = datetime.now()
   day_diff = (current_datetime - creation_datetime).days
   
   return day_diff >= WEEK_THRESHOLD
   

## Is file empty 
def is_empty_file(file_path):
   return stat(file_path).st_size == 0

## Delete the empty file 
def delete_empty_file(full_filepath):
   name_of_file = full_filepath.split('/')[-1]
   
   if is_empty_file(full_filepath):
      print(f"[+] Warning {name_of_file} is empty ..")
      
      if is_unecessary(full_filepath):
         remove(full_filepath)
         print(f"[+] This {name_of_file} is taking space and it is empty from a week")
         print(f"[+]The file {name_of_file} has been deleted.")
         return True 
   return False 

## Move the file to correct folder 
def move_file(dest , sourcedir , name):
   
   file_exist = exists(f"{dest}/{name}")
   new_name = name 
   
   if file_exist:
      filename , ext = splitext(name)
      count = 1
      while exists(f"{dest}/{new_name}"):
         new_name = f"{filename}_{str(count)}{ext}"
         count += 1
         
      old_path_name = join(sourcedir, name)
      new_path_name = join(sourcedir , new_name)
      rename(old_path_name,new_path_name)

   move(new_name , dest)



## Organize the file in right folders
def organize_files(sourcedir):
   # loop over the path 
   for entry in scandir(sourcedir):
      # if entry is file 
      if entry.is_file():
         # get the name 
         name_of_file = entry.name
         # get filename and extesion of file
         filename , ext = splitext(name_of_file)
      
         file_path = f"{sourcedir}/{name_of_file}"
         if delete_empty_file(file_path):
            continue 
         
         # loop to keys of dictonary
         for dir in dic.keys():
            
            if ext in dic[dir]:
               dest = f"{sourcedir}/{dir}"
               # if directory not exists create it .
               if not exists(dest):
                  mkdir(dest)
               # call move function to move the file  
               move_file(dest , sourcedir , name_of_file)
               print(f"[+] Moved {name_of_file} -> {dir} directory")
            else:
               print(f"Given .{ext} extension Not Found ")



## Clean up the unecessary files and set the icon to the folder 
def clean_up(sourcedir):
#  add icon to folder and delete files that are unnecessary and empty for more than a week
   for dir in dic.keys():
      folder_path = f"{sourcedir}/{dir}"
      
      if exists(folder_path):
         set_icon(dir , sourcedir)
         
         for entry in scandir(folder_path):
            if entry.is_file():
               name_of_file = entry.name 
               file_path = f"{folder_path}/{name_of_file}"
               delete_empty_file(file_path)


if __name__ == '__main__':
   sourcedir = "/Users/Shared/python_code/file_cleanup"
   organize_files(sourcedir)
   clean_up(sourcedir)