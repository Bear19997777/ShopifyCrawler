
import os 
import json 

def ParseSiteInfo(jsonFile,screenshotdir="./screenshot"):
    websitedict = dict()
    with open(jsonFile, 'r') as file:
        websiteinfo = json.load(file)
    websitelist = [] 
    print(websiteinfo)
    for entry in websiteinfo:
        print(entry)
        websitename = entry["url"].split("//")[1].split(".")[0]
        entry["name"] = websitename #entry 
        siteName = entry["url"].split("//")[1].split(".")[0]
        if os.path.exists(f"{screenshotdir}/{siteName}"):
            imgFileName = os.listdir(f"{screenshotdir}/{siteName}")[0]
            imgPath = os.path.join(f"{screenshotdir}/{siteName}",imgFileName)
            
            entry["imgPath"] = imgPath
        websitelist.append(entry)
        
    # print(websitelist)
    with open(jsonFile,"w") as f : 
        json.dump(websitelist,f)
        
    return jsonFile
    
                    
if __name__ == "__main__":
    ParseSiteInfo("./database/websites_info_0704.json")