#!/usr/bin/env python
import os
from hashlib import md5, sha256

def get_size(path):
    return os.stat(path).st_size
    #return file.st_size
    
def hashing(f, size):
    maxsize = 120 #we need to read in chunks of 120 otherwise we might use ALL the memory we have!!
    s = sha256()
    s.update("StOrM %u\0" %size) #include the size and "personal word in the hasing"
    while True:
        d = f.read(maxsize)
        if not d: break
        s.update(d)
    return s.hexdigest()

def check_file_and_commit(hashed_val, d, file_path):
    if hashed_val in d:
        if d[hashed_val] != file_path:
            try:
                os.remove(file_path)
                print("File deleted "+ file_path)
                return True
            except OSError as ex:
                if ex.errno == 13:
                    print "Can't delete file: " + file_path + "\nPermession Denied"
                elif ex.errno > 0:
                    print "Cant delete file: " + file_path + "\n errorno: " + str(ex.errno)
            return False
    else:
        d[hashed_val] = file_path
        return False
        
def get_files2(path):
    
    file_path_list = []
    for dirname, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirname, filename)
            file_path_list.append(file_path)
    return file_path_list


def get_folders(dir_name):
    folders = []
    for (dirname, dirnames, filenames) in os.walk(dir_name):
        for subdirname in dirnames:
            folders.append(os.path.join(dirname, subdirname))
    return folders
    
def main():
    #path = raw_input("Please, Enter directory path: ")
    deleted_files = 0
    deleted_size = 0
    deleted_dirs = 0
    scanned_files=0
    
    path = "/Users/macbookpro/Downloads"
    d = dict()
    file_list = get_files2(path)
    dir_list = get_folders(path)
    
    for file_name in file_list:
            try:
                f = open(file_name, 'rb')
                size = get_size(file_name)
                hashed_val = hashing(f, size)
                if check_file_and_commit(hashed_val, d, file_name):
                    deleted_files +=1
                    deleted_size += size
            except IOError as ex:
                if ex.errno == 2:
                    print "Couldn't open file: " + str(file_name) + "\nerrno[" + str(ex.errno) + "]"
                else:
                    print "Error: " + str(file_name) + "\nerrno[" + str(ex.errno) + "]"
            except:
                pass
            finally:
                scanned_files +=1
                f.close()
    dir_list.sort(reverse=True)
    try:

        for dir_path in dir_list:
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                print "Dir Deleted"
                deleted_dirs +=1
    except:
        print "Error occured while deleting " + str(dir_path)
        
        
    #print "No of deleted files is: %i \nNo of size deleted is: %i \nNo of deleted dirs is: %i" (deleted_files, deleted_size, deleted_dirs)  
    print "No of deleted files is: " + str(deleted_files)
    print "No of size deleted is: " + str(deleted_size) + " bytes"
    print "No of deleted dirs is: " + str(deleted_dirs)
    print "No of scanned files is: " + str(scanned_files)
    
    
if __name__ == '__main__':
    main()