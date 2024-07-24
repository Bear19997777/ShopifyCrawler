import unittest 
import main 

class ShopAppUnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.shopifyapp = main.ShopifyAuto()
    def test_apilogin(self):
        self.assertTrue(self.shopifyapp.login())
        
    def test_create_product(self):
        self.assertTrue(self.shopifyapp.createProduct())
        
        
        
        
        
    

if __name__=="__main__":
    unittest.main()
    
    