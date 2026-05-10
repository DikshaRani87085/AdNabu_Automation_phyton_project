# AdNabu Store Automation

Modular Selenium automation script to search for a product and add it to the cart.

## Features

✓ **No hardcoded sleeps** - Uses WebDriverWait with explicit expected conditions  
✓ **Modular design** - Separate page object classes (StorePage, SearchPage, ProductPage, CartPage)  
✓ **Readable code** - Clear class names and methods for maintainability  
✓ **Error handling** - Catches exceptions and saves screenshots for debugging  
✓ **Proper waits** - All interactions wait for elements to be ready (clickable, visible, present)

## Project Structure

```
AdNabuAutomation/
├── store_automation.py      # Main automation script
├── requirements.txt          # Python dependencies
└── README.md                # This file
```

## Setup Instructions

### 1. Create Virtual Environment

```powershell
cd D:\AdNabuAutomation
python -m venv venv
```

### 2. Activate Virtual Environment

```powershell
# On Windows PowerShell:
.\venv\Scripts\Activate.ps1

# If you get execution policy error, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Download ChromeDriver

The script requires ChromeDriver for Chrome browser automation.

**Option A: Automatic (recommended)**
- Selenium 4.6+ automatically downloads the correct ChromeDriver
- No additional setup needed

**Option B: Manual**
1. Download ChromeDriver from: https://chromedriver.chromium.org/
2. Version should match your Chrome version (`chrome://version/`)
3. Place in PATH or project folder

## Running the Script

```powershell
python store_automation.py
```

## How It Works

### Page Objects

**StorePage** (Base class)
- `visit(url)` - Navigate to store
- `unlock_store(password)` - Enter password to access store

**SearchPage** (Inherits from StorePage)
- `open_search()` - Open search dialog
- `search_product(name)` - Search for product by name
- `select_first_product()` - Click first search result

**ProductPage** (Inherits from StorePage)
- `get_product_name()` - Get product title
- `add_to_cart()` - Add product to cart with verification

**CartPage** (Inherits from StorePage)
- `open_cart()` - Open shopping cart
- `verify_product_in_cart(name)` - Verify product is in cart

### Automation Flow

1. **Unlock Store** → Enter password "AdNabuQA"
2. **Search** → Search for "snowboard" products
3. **Select** → Click first search result
4. **Add to Cart** → Add selected product to cart
5. **Verify** → Confirm product is in shopping cart

## Configuration

Edit these values in `store_automation.py` to customize:

```python
STORE_URL = "https://adnabu-store-assignment1.myshopify.com/"
STORE_PASSWORD = "AdNabuQA"
SEARCH_PRODUCT = "snowboard"  # Change search term here
```

## Headless Mode

To run without opening a browser window, uncomment this line in `store_automation.py`:

```python
chrome_options.add_argument("--headless")
```

## Wait Strategy

All interactions use explicit waits:
- **element_to_be_clickable()** - Element is visible and enabled
- **visibility_of_element_located()** - Element is visible in viewport
- **presence_of_element_located()** - Element exists in DOM

Timeout: **10 seconds** (adjustable via `WebDriverWait(driver, timeout=10)`)

## Troubleshooting

| Issue | Solution |
|-------|----------|
| ChromeDriver not found | Install via `pip install webdriver-manager` and use it |
| Element not found | Check selectors match current page HTML (might change) |
| Timeout errors | Increase wait timeout in `WebDriverWait` constructor |
| Password doesn't work | Verify `STORE_PASSWORD` matches actual password |

## Example Output

```
============================================================
ADNABU STORE AUTOMATION - SEARCH & ADD TO CART
============================================================

Navigated to https://adnabu-store-assignment1.myshopify.com/
Entered store password
Clicked Enter button
Store unlocked successfully

------------------------------------------------------------
STEP 1: Store unlocked ✓
------------------------------------------------------------

Opened search
Searched for: snowboard
Clicked first product from search results

------------------------------------------------------------
STEP 2: Product found ✓
------------------------------------------------------------

Clicked Add to cart for: The Collection Snowboard: Liquid
Product added to cart successfully!

------------------------------------------------------------
STEP 3: Product added to cart ✓
------------------------------------------------------------

Opened cart
✓ Verified: The Collection Snowboard: Liquid is in cart

============================================================
AUTOMATION COMPLETED SUCCESSFULLY ✓
============================================================
```

## Next Steps

To extend this automation:
- Add more test scenarios (checkout, payment)
- Use pytest for test framework
- Add logging instead of print statements
- Create fixtures for common setup/teardown
- Add cross-browser support

## Notes

- Store is Shopify-based (may have dynamic elements)
- Search results depend on available products
- Add to cart button state changes after adding (updates automatically)
