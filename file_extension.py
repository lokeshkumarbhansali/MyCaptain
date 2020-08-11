import os

file = input('Enter the filename : ')

extension_dict = {'.py' : 'Python' , '.java' : 'Java' , '.doc' : 'Microsoft Word File' ,
                  '.pdf' : 'PDF File' , '.ppt' : 'Powerpoint presentation' , '.html' : 'HTML File' ,
                  'png' : 'PNG Image' , 'jpeg' : 'JPEG File'}
for i in extension_dict:
    if i == os.path.splitext(file)[1]:
        print(extension_dict[i])
