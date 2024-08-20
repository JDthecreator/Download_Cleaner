import os
import shutil

path = input("Enter Path: ") 
files = os.listdir(path)  

directory = ['Audio_downloads', 'Picture_downloads', 'Apps_downloads','Document_downloads','Zipfile_downloads', 'Lostnfound_downloads'] 


if os.path.exists(path):
    for folder in directory:
        os.makedirs(os.path.join(path, folder),exist_ok=True) 
    print("Directory folders created successfully")


for file in files:
    filename,extension = os.path.splitext(file)
    extension = extension[1:]

    if extension in ('mp4','wav','mp3'):
        shutil.move(path+'\\'+file, path+'\\'+directory[0]+'\\'+file)

    elif extension in ('jpg','png'):
        shutil.move(path+'\\'+file, path+'\\'+directory[1]+'\\'+file)
        
    elif extension == 'exe':
        shutil.move(path+'\\'+file, path+'\\'+directory[2]+'\\'+file)
        
    elif extension in ('docx','pdf','txt','xlsx'):
        shutil.move(path+'\\'+file, path+'\\'+directory[3]+'\\'+file)
        
    elif extension == 'zip':
        shutil.move(path+'\\'+file, path+'\\'+directory[4]+'\\'+file)
        
    else:
        shutil.move(path+'\\'+file, path+'\\'+directory[5]+'\\'+file)
print("finished")