import databaseOp as dbo 
import requests
from bs4 import BeautifulSoup
import html_text
from deep_translator import GoogleTranslator
from llama_index.llms.ollama import Ollama
import pandas as pd 
# 定義要獲取的URL
"""
   1.Clothing and Fashion
    2.Beauty and Personal Care
    3.Electronics and Gadgets
    4.Home Decor and Furniture
    5.Food and Beverage
    6.Sports and Outdoor
    7.Subscription Services
    8.Specialty Products
    9.Cultural and Niche Products
    10.Other
"""
categoriesDict = {"1":"Clothing and Fashion",
                  "2":"Beauty and Personal Care",
                  "3":"Electronics and Gadgets",
                  "4":"Home Decor and Furniture",
                  "5":"Food and Beverage",
                  "6":"Sports and Ourdoor",
                  "7":"Subscription Services",
                  "8":"Specialty Products",
                  "9":"Cultural and Niche Products",
                  "10":"Other"}


def extractWebsiteText(url):
    # dbobj = dbo.ShopifyDatabase("./database/database.xlsx")
    # dbDf = dbobj.GetDatabase()
    # urls = dbDf["url"]
        # 發送HTTP GET請求
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        # 打印解析後的HTML
    else:
        print(f"Failed to retrieve the URL: {response.status_code}")
    
    extract = html_text.extract_text(soup.prettify(),guess_layout=False)
    translator = GoogleTranslator(source='auto', target='en')
    text = "".join([translator.translate(extract[i*4000:(i+1)*4000]) for i in range(len(extract)//4000)])
    

    return text

def summerize(text):
    
    llm = Ollama(model="llama3.1",request_timeout=3600)
    result = llm.complete("Please summerize this text  as short and detail as possiblly "+text)
    return result.text

def classifyproductTag(text):
    llm = Ollama(model="llama3.1",request_timeout=3600)
    result = llm.complete("""
    Please help me determine which of the following nine categories the content of the website described belongs to and just provide  classify result  please don't provide any description:
    1.Clothing and Fashion
    2.Beauty and Personal Care
    3.Electronics and Gadgets
    4.Home Decor and Furniture
    5.Food and Beverage
    6.Sports and Outdoor
    7.Subscription Services
    8.Specialty Products
    9.Cultural and Niche Products
    10.Other """+text)
    result = result.text
    return result

def assignDescription(row:pd.DataFrame):
    url = row["url"]
    text = extractWebsiteText(url=url)
    result = summerize(text)
    print(url)
    print(f"result:{result}")
    return result

def assignTag(row:pd.DataFrame):
    description = row["description"]
    # text = extractWebsiteText(url=url)
    result = classifyproductTag(description)
    print(result)
    return result
def tagReview(row:pd.DataFrame):
    tag = row["tag"]
    print(type(tag))
    tag = "".join([str(x) for x in tag if str(x).isdigit()])
    print(tag)
    tag = categoriesDict[tag]
    return tag
    

if __name__ == "__main__":
    dbobj = dbo.ShopifyDatabase("./database/database.xlsx")
    dbDf = dbobj.GetDatabase()
    dbDf["description"] = dbDf.apply(assignDescription,axis=1)
    dbDf["tag"] = dbDf.apply(assignTag,axis=1)
    dbDf["tag"] = dbDf.apply(tagReview,axis=1)
    updateresult = dbobj.updateDataFrame(dbDf)
    print(updateresult)
    
    
    