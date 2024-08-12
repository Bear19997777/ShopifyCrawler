import requests
from bs4 import BeautifulSoup
import time
import databaseOp as dbo
import json
def google_search(query, num_pages):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    urls = []
    for page in range(num_pages):
        url = f"https://www.google.com/search?q={query}&start={page*10}"
        response = requests.get(url, headers=headers)
        print("im response")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('a'):
                href = link.get('href')
                if 'url?esrc=s&q' in href:
                    actual_url = href.split('url?esrc=s&q')[1].split('&sa=U&url=')[1]
                    final_url = ""
                    for text in actual_url.split("/"):
                        if "." in text :
                            final_url+=text 
                            
                            break 
                        else: 
                            final_url+=text
                            final_url+="/"
                    urls.append(final_url)
                    
        time.sleep(1)  # 加上延遲以避免被Google封禁
    return urls


def getshopify_site(num_pages):
    websiteinfolist = [] 
    query = "site:myshopify.com"
    shopify_urls = google_search(query, num_pages)
    urllist = [] 
    for url in shopify_urls:
        if url not in urllist:
            tmpdict = {}
            tmpdict["url"] = url 
            urllist.append(url)
            websiteinfolist.append(tmpdict)
    jsonfilePath = "./tempdir/urljsonfile.json"
    with open(jsonfilePath,"w") as f : 
        json.dump(websiteinfolist,f)
    return jsonfilePath 

    



if __name__ == '__main__':
    getshopify_site(1)