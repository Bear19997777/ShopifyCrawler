import json 
import shopify_siteParse as ss 
websitelist = [] 
tmpDict = {}
start = False 
with open ("./database/websites_info.txt","r") as f:
    for line in f.readlines():
        
        if "https" in line: 
            websitename = line.split("//")[1].split(".")[0]
            tmpDict["name"] = websitename
            url = "".join([x for x in line if not x.isdigit()]).rstrip().replace(". ","")
            tmpDict["url"] = url
            start = True
        if "- " in line and start: 
            tmpDict["description"] = line.replace("    - ","").rstrip().replace("  - ","")
            
            websitelist.append(tmpDict)
            tmpDict = {}
            start = False
oldjsonfilepath = "./database/oldproductInfo.json"
print(websitelist)
with open(oldjsonfilepath,"w+") as f :
    json.dump(websitelist,f)

ss.ParseSiteInfo(oldjsonfilepath,"screenshot_ild")
