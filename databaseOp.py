import pandas as pd 
import json 
import shopify_siteParse  as ss 



class ShopifyDatabase:
    def __init__(self,databasepath):
        self.__databasePath = databasepath 
        self.__excelData = pd.read_excel(self.__databasePath,engine='openpyxl')
        
    def GetDatabase(self):
        return self.__excelData
    
    def updateExcel(self,df:pd.DataFrame):
        df.to_excel(self.__databasePath,index=False)
        self.__excelData = df 
    
    def readExcelFile(self,path):
        pass 
    
    def appendData(self,data):
        pass 
    
    def readJsonFile(self,path):
        pd.read_json(path)
        return pd.read_json(path)
    
    def readtxtFile(self,path):
        pass 
    
    def delteDuplicate(self):
        pass 
    
    
    def transferTodataFrame(self,data):
        pass 
    
    
if __name__ == "__main__":
    db = ShopifyDatabase("./database/database.xlsx" )
    # ss.ParseSiteInfo("./database/websites_info_0704.json")
    json_df = db.readJsonFile("./database/websites_info_0704.json")
    
    db.updateExcel(json_df)
    print(db.GetDatabase())
    # print(jsonfile)

    
    