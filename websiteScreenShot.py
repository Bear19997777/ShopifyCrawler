from playwright.sync_api import sync_playwright
import os 
import datetime as dt 
import json 
from types import * 
def capture_screenshot(url, picture_path, timeout=60000):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        try:
            page.goto(url, wait_until='networkidle', timeout=timeout)
            
            # # 等待特定的元素出現
            # page.wait_for_selector("css_selector_of_the_element", timeout=timeout)
            
            # 確保所有內容都已加載
            page.evaluate("() => { window.scrollBy(0, document.body.scrollHeight); }")
            
            page.wait_for_timeout(3000)
            
            page.evaluate("() => { window.scrollTo(0, 0); }")
            
            page.screenshot(path=picture_path, full_page=False)  # 使用full_page參數截取整個頁面
            print("截圖成功")
        except Exception as e:
            print(f"截圖失敗: {e}")
        finally:
            browser.close()
def save_picture(*,jsonfilePath:str):



    count = 0 

    with open(jsonfilePath, "r") as file :
        websiteInfo = json.load(file)
        for entry  in websiteInfo:
            url = entry["url"]
            if not os.path.isdir("screenshot") : os.mkdir("screenshot")
            count += 1
            websitename = str(url.split("//")[1].split(".myshopify")[0]).replace(".","_")
            assert type(websitename ) != type(str),"websitename parse Fail"
            if not os.path.isdir(f"./screenshot/{websitename}"): os.mkdir(f"./screenshot/{websitename}")
            picturepath = os.path.join(f"./screenshot/{websitename}",f"{count}.png")
            if not os.path.exists(picturepath):
                capture_screenshot(url, picturepath)
                print(f'Screenshot saved to {picturepath}')
    return jsonfilePath
                
def remove_empty_dir():
    for dir in os.listdir("./screenshot"):
        path = os.path.join("./screenshot",dir)
        if len(os.listdir(path))>=1:
            pass 
        else: 
            try :
                os.rmdir(path)
                print(path)
                print("移除成功")
                
            except Exception as e: 
                print(e)
                print("移除失敗")            

def wirte_screenshot_success_url():
    websiteInfolist = []
    jsonpath = r"./tempdir/urljsonfile.json"
    with open(jsonpath,"w") as f: 
        for dir in os.listdir("./screenshot"):
            tmpdict = {}
            url = f"https://{dir}.myshopify.com"
            tmpdict["url"] = url
            websiteInfolist.append(tmpdict)
        json.dump(websiteInfolist,f)
    return jsonpath
    
            
        
if __name__ == "__main__":
    save_picture(jsonfilePath="./tempdir/urljsonfile.json")
    remove_empty_dir()
    wirte_screenshot_success_url()