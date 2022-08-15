from pathlib import Path

# Absolute path -> from root dir
# Relative path -> from current dir

# By default the Path() refers to the current dir alternatively you could put your specified path inside a string
path = Path("./024_package/ecommerce")
print(path.exists()) # checks if the path object exists
path1 = Path('emails')
path1.mkdir() # make new dir called emails
path1.rmdir() # remove the dir

# using .glob() method -> to acess all files & dir in the current path
path2 = Path()
for file in path2.glob('*.py'):
    print(file)