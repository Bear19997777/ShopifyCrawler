import databaseOp as dbo 
import requests
from bs4 import BeautifulSoup
import html_text
from deep_translator import GoogleTranslator
from llama_index.llms.ollama import Ollama
import pandas as pd 
# 定義要獲取的URL


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
    return result

def assignDescription(row:pd.DataFrame):
    url = row["url"]
    text = extractWebsiteText(url=url)
    result = summerize(text)
    print(url)
    print(f"result:{result}")
    return result


if __name__ == "__main__":
    dbobj = dbo.ShopifyDatabase("./database/database.xlsx")
    dbDf = dbobj.GetDatabase()
    # urls = dbDf["url"]
    dbDf["description"] = dbDf.apply(assignDescription,axis=1)
    updateresult = dbobj.updateDataFrame(dbDf)
    print(updateresult)
    
    
    