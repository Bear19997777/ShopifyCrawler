import databaseOp as dbo 
import requests
from bs4 import BeautifulSoup
import html_text
from deep_translator import GoogleTranslator
# 定義要獲取的URL


def extractWebsiteText():
    dbobj = dbo.ShopifyDatabase("./database/database.xlsx")
    dbDf = dbobj.GetDatabase()
    urls = dbDf["url"]
    for url in urls : 
        print(url)
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
        
        print(text)
    return text


if __name__ == "__main__":
    text = extractWebsiteText()
    
    