import shopify 
import os
import binascii 
import shopify.session 
import shopify_siteParse as ssp
import getShopifySite  as gss
import remove_overlap
import websiteScreenShot as wss
import josonfileSave_0704
import databaseOp as dbo
start = False 
flag = "" 

userinput = str(input("1. get site 2. remove overlap 3. site parse 4. screen shot 5.shopify "))

executedict = {"1":1,"2":2,"3":3,"4":4,"5":5}

class ShopifyAuto:
    
    def __init__(self,websiteInfoFile):
        self.websiteInfoFile = websiteInfoFile
    def __repr__(self):
        return "<shopify opject>"
    def __str__(self):
        return "shoppify object>"
    
    def updateolder(self): 
        pass 
    
    def login(self):
        shopify_token = os.environ.get("shopify_token",False)
        shopify_APIkey = os.environ.get("shopify_key",False)
        shopify_secrectKey = os.environ.get("shopify_secretKey",False)

        if not (shopify_token and shopify_APIkey and shopify_secrectKey):return False 
        
        shop_url = "d2143d-af"
        api_version = "2024-04"
        session = shopify.Session(shop_url, api_version, shopify_token)
        shopify.ShopifyResource.activate_session(session)
        shop = shopify.Shop.current()
        if not shop:
            return False 
        return True 
    
    def createProduct(self):
        
        webInfoDict = self.dataParse(self.websiteInfoFile)
        
        for sitename in webInfoDict:
            print(sitename)
            product = shopify.Product()
            product.title = sitename
            product.body_html = f"""<strong>{webInfoDict[sitename]["description"]}</strong> 
            <br>
            <strong>Price Range:{webInfoDict[sitename]["price_range"]}</strong>
            <br>
            <a href="{webInfoDict[sitename]["url"]}" target="_blank">Ｖisit {sitename}</a>"""

            new_variant = shopify.Variant()
            new_variant.price = "1.00"
            new_variant.sku = f"{sitename}"
            
            with open(webInfoDict[sitename]["imgPath"],"rb") as image_file:
                image_data = image_file.read()
            
            new_image = shopify.Image()
            new_image.product_id = product.id
            new_image.attach_image(image_data,filename= f"{sitename}.jpg")
            product.images = [new_image] 
            product.variants = [new_variant]

            if product.save():
                
                print("新產品創建成功")
                product_id = product.id

                # 設置價格區間
                price_range = webInfoDict[sitename]["price_range"]
                metafield = shopify.Metafield({
                    'namespace': 'global',
                    'key': 'price_range',
                    'value': price_range,
                    'value_type': 'string'
                })
                product.add_metafield(metafield)
                
                # 保存產品以更新價格區間標示
                if product.save():
                    print("價格區間標示更新成功")
                else:
                    print("價格區間標示更新失敗")

            else:
                print("產品上架失敗")
    
    def printPorduct(self):
        products = shopify.Product.find()
        for product in products: 
            print(f"product title:{product.title},product ID : {product.id}")
    
    def logout(self):
        shopify.ShopifyResource.clear_session()
    def deleteProductAll(self):
        products = shopify.Product.find()
        for product in products:
            try:
                product = shopify.Product.find(product.id)
                product.destroy()
                print(f"產品ID {product} 已成功下架")
            except Exception as e:
                print(f"出錯了: {e}")
    def deletetitleProduct(self):
        webInfoDict = self.dataParse(self.websiteInfoFile)
        
        for sitename in webInfoDict:
            products = shopify.Product.find(title=sitename)

            if products:
                for product in products:
                    destory_result = product.destroy()
                    print(destory_result)
                    if destory_result:
                        print(f"商品 '{product.title}' 刪除成功")
                    else:
                        print(f"商品 '{product.title}' 刪除失敗")
            else:
                print(f"未找到標題為 '{sitename}' 的商品")
        
            
    def downloadNewproduct(self,webtextInfoFile):
        jsonpath = gss.getshopify_site(1)
        wss.save_picture(jsonfilePath=jsonpath)
        wss.remove_empty_dir()
        jsonpath = wss.wirte_screenshot_success_url()
        ssp.ParseSiteInfo(jsonpath)
        dboObj = dbo.ShopifyDatabase()
        jsondf = dboObj.readJsonFile(jsonpath)
        newdf = dboObj.deleteExistsData(jsondf)
        dboObj.AddNewData(newdf)
        
        

            
        
    def UnitTest(self):
        pass 
 
 
if __name__ == "__main__":
 
        # josonfileSave_0704.

        
    

    
    if start :
        shopapp = ShopifyAuto("/Users/zhuangjunrong/Documents/Project/shopify/database/websites_info_0704.json")
        shopapp.login()   
        # shopapp.deletetitleProduct()
        shopapp.createProduct()
        # shopapp.printPorduct()
        # shopapp.deleteProductAll()
        # shopapp.logout()