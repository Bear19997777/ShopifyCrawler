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
        # df.to_excel(self.__databasePath,index=False)
        # self.__excelData = df 
        newdf = pd.concat([df,self.__excelData])
        newdf.to_excel(self.__databasePath,index=False)
        self.__excelData = newdf
    
    def readExcelFile(self,path):
        pass 
    
    
    def readJsonFile(self,path):
        pd.read_json(path)
        return pd.read_json(path)
    
    def readtxtFile(self,path):
        pass 
    
    def deleteExistsData(self,newdf):
        
        df_overlap = pd.merge(self.__excelData, newdf, on='name')
        df_new_unique = newdf[~newdf['name'].isin(df_overlap['name'])]
        print(df_new_unique)
        print(f"Origin update ocunt:{newdf.shape[0]}")
        print(f"overlap count : {df_overlap.shape[0]}")
        print(f"Total update count: {df_new_unique.shape[0]}")
        raise Exception
        return df_new_unique
    
    
    def transferTodataFrame(self,data):
        pass 
    
    
if __name__ == "__main__":
    db = ShopifyDatabase("./database/database.xlsx" )
    jsonfilepath = "./tempdir/urljsonfile.json"
    ss.ParseSiteInfo(jsonfilepath)
    json_df = db.readJsonFile(jsonfilepath)
    newdf = db.deleteExistsData(json_df)
    db.updateExcel(newdf)
    print(db.GetDatabase())
    # print(jsonfile)

    
    