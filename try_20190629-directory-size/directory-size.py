import os

# pick a folder you have ...
myvar = 'C:\\...'
folder_size = 0
for (path, dirs, files) in os.walk(myvar):
  for file in files:
    filename = os.path.join(path, file)
    folder_size += os.path.getsize(filename)
k_size=(folder_size/(1024*1024.0))
print(k_size)