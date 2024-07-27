
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
        websitename = str(entry["url"].split("//")[1].split(".myshopify")[0]).replace(".","_")
        entry["name"] = websitename #entry 
        if os.path.exists(f"{screenshotdir}/{websitename}"):
            imgFileName = os.listdir(f"{screenshotdir}/{websitename}")[0]
            imgPath = os.path.join(f"{screenshotdir}/{websitename}",imgFileName)
            entry["imgPath"] = imgPath
    
        websitelist.append(entry)
        
    # print(websitelist)
    with open(jsonFile,"w") as f : 
        json.dump(websitelist,f)
        
    return jsonFile
    
                    
if __name__ == "__main__":
    ParseSiteInfo("./database/websites_info_0704.json")