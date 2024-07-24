
import os 
import json 

def ParseSiteInfo(jsonFile):
    websitedict = dict()
    with open(jsonFile, 'r') as file:
        websiteinfo = json.load(file)
    websitelist = [] 
    print(websiteinfo)
    for entry in websiteinfo:

        websitename = entry["url"].split("//")[1].split(".")[0]
        entry["name"] = websitename #entry 
        siteName = entry["url"].split("//")[1].split(".")[0]
        imgFileName = os.listdir(f"./screenshot/{siteName}")[0]
        imgPath = os.path.join(f"./screenshot/{siteName}",imgFileName)
        
        entry["imgPath"] = imgPath
        websitelist.append(entry)
        
    # print(websitelist)
    with open(jsonFile,"w") as f : 
        json.dump(websitelist,f)
        
    return websitelist
    
                    
if __name__ == "__main__":
    ParseSiteInfo("./database/websites_info_0704.json")