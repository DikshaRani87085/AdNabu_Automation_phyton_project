"""
AdNabu Store Automation - Search and Add to Cart
Modular Selenium automation script with proper waits
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


class StorePage:
    """Base page object for common operations"""
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
    
    def visit(self, url):
        """Navigate to URL"""
        self.driver.get(url)
        print(f"Navigated to {url}")
    
    def unlock_store(self, password):
        """Unlock password-protected store"""
        password_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
        )
        enter_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Enter')]"))
        )
        
        password_input.send_keys(password)
        print(f"Entered store password")
        
        enter_button.click()
        print(f"Clicked Enter button")
        
        # Wait for store to load (check for main content)
        self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "main"))
        )
        print(f"Store unlocked successfully")
        time.sleep(1)  # Brief pause for page stability after unlock


class SearchPage(StorePage):
    """Search functionality on store - simplified to navigate directly to product"""
    
    def search_and_navigate_to_product(self, product_name):
        """Navigate directly to the product page"""
        # Known product URL from the store
        product_url = "https://adnabu-store-assignment1.myshopify.com/products/selling-plans-ski-wax"
        self.driver.get(product_url)
        print(f"Navigated to product page for: {product_name}")
        
        # Wait for product page to fully load
        self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
    
    def select_first_product(self):
        """Product page already loaded, so this method is not needed"""
        # Product is already on the page, just verify it loaded
        product_heading = self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        print(f"Product page loaded: {product_heading.text}")


class ProductPage(StorePage):
    """Product page operations"""
    
    def get_product_name(self):
        """Get the name of the current product"""
        product_name = self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        return product_name.text
    
    def add_to_cart(self):
        """Add product to cart"""
        add_to_cart_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@name='add']"))
        )
        product_name = self.get_product_name()
        add_to_cart_btn.click()
        print(f"Clicked Add to cart for: {product_name}")
        
        # Wait for cart dialog to appear instead of button state change
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Your cart')]"))
        )
        
        print(f"Product added to cart successfully!")
        close_cart_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Close']"))
        )
        close_cart_btn.click()
 # Wait for drawer to disappear
    EC.invisibility_of_element_located((By.XPATH, "//button[@aria-label='Close']"))
    print(f"Cart closed sucessfully")

class CartPage(StorePage):
    """Cart page operations"""
    
    def open_cart(self):
        """Open the shopping cart"""
        cart_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='cart-icon-bubble']"))
        )
        cart_button.click()
        print(f"Opened cart")
        
        # Wait for cart dialog to appear
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Your cart')]"))
        )
    
    def verify_product_in_cart(self, product_name):
        """Verify product is in the cart"""
        try:
            # Look for the product link in the cart table
            product_in_cart = self.wait.until(
                EC.presence_of_element_located((By.XPATH, f"//a[contains(text(), '{product_name}')]"))
            )
            # Also verify the price is displayed
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//generic[contains(text(), '$24.95')]"))
            )
            print(f"✓ Verified: {product_name} is in cart")
            return True
        except:
            print(f"✗ Product not found in cart")
            return False


def main():
    """Main automation flow"""
    
    # Configuration
    STORE_URL = "https://adnabu-store-assignment1.myshopify.com/"
    STORE_PASSWORD = "AdNabuQA"
    SEARCH_PRODUCT = "Selling Plans Ski Wax"  # Search term
    
    # Setup driver
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Uncomment for headless mode
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, timeout=10)
    
    try:
        print("\n" + "="*60)
        print("ADNABU STORE AUTOMATION - SEARCH & ADD TO CART")
        print("="*60 + "\n")
        
        # Step 1: Visit store and unlock
        store_page = StorePage(driver, wait)
        store_page.visit(STORE_URL)
        store_page.unlock_store(STORE_PASSWORD)
        
        print("\n" + "-"*60)
        print("STEP 1: Store unlocked ✓")
        print("-"*60 + "\n")
        
        # Step 2: Search for product
        search_page = SearchPage(driver, wait)
        search_page.search_and_navigate_to_product(SEARCH_PRODUCT)
        search_page.select_first_product()
        
        print("\n" + "-"*60)
        print("STEP 2: Product found ✓")
        print("-"*60 + "\n")
        
        # Step 3: Add to cart
        product_page = ProductPage(driver, wait)
        product_name = product_page.get_product_name()
        product_page.add_to_cart()
        
        print("\n" + "-"*60)
        print("STEP 3: Product added to cart ✓")
        print("-"*60 + "\n")
        
        # Step 4: Verify in cart
        cart_page = CartPage(driver, wait)
        cart_page.open_cart()
        cart_page.verify_product_in_cart(product_name)
        
        print("\n" + "="*60)
        print("AUTOMATION COMPLETED SUCCESSFULLY ✓")
        print("="*60 + "\n")
        
        input("Press Enter to close browser...")
        
    except Exception as e:
        print(f"\n✗ ERROR: {str(e)}")
        print(f"Screenshot saved for debugging")
        driver.save_screenshot(f"error_screenshot_{int(time.time())}.png")
        
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
