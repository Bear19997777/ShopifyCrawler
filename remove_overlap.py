
import os 

def remove_duplicateURL():
    url_list = []  
    with open("url.txt","r") as f : 
        for line in f.readlines(): 
            print(line)
            if line not in url_list:
                url_list.append(line)
    with open("url0701.txt","w+") as f : 
        for url in url_list:
            print(url)
            f.write(url)

def get_newURL(*,oldpath="",NewPath=""):
    oldurllist = [] 
    with open("url_old.txt","r") as f : 
        for line in f.readlines():
            if line not in oldurllist : 
                oldurllist.append(line)
    new_urlList = [] 
    with open("url0701.txt","r") as f:
        for line in f.readlines():
            if line not in oldurllist : 
                new_urlList.append(line)
    with open("url_new.txt","w+") as f: 
        for line in new_urlList:
            f.write(line)
            
    
            
        

if __name__ == "__main__":
    # remove_duplicateURL()
    get_newURL()