import databaseOp as dbo 
import requests
from bs4 import BeautifulSoup
import html_text
# 定義要獲取的URL


def extractWebsiteText():
    dbobj = dbo.ShopifyDatabase()
    dbDf = dbobj.GetDatabase()
    print(dbDf)
    urls = dbDf["url"]
    print(urls)
    for url in urls : 
        print(url)
        # 發送HTTP GET請求
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            # 打印解析後的HTML
            print(soup.prettify())
        else:
            print(f"Failed to retrieve the URL: {response.status_code}")
        
        extract = html_text.extract_text(soup.prettify(),guess_layout=False)
        print(extract)
    return extract

    