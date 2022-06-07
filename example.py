#define function for reading a file and replace the specific content
import os

def findCWD():
    return os.getcwd()

def checkFileExist():
    fileStatus = False
    cwd = findCWD()
    pathname = os.path.join(cwd, "example.txt")
    fileStatus = os.path.exists(pathname)
    return fileStatus

def replaceSpecificContent(org_file_content, replace_text_data):
    #open the file
    try:
        #fileStatus = checkFileExist()
        cwd = findCWD()
        pathname = os.path.join(cwd, "example.txt")
        with open(pathname, 'r+') as file:
            filedata = file.read()
            data = filedata.replace(org_file_content, replace_text_data)
        with open(pathname, 'w') as file:
            file.write(data)
    except (FileNotFoundError, IOError):
        print("File does not exists!!")

if __name__ == "__main__":
    org_String = input("Enter the original string:")
    replaced_String = input("Enter the replaced string:")
    replaceSpecificContent(org_String, replaced_String)