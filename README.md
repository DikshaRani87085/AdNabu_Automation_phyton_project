# AdNabu Store Automation

Modular Selenium automation script to search for a product and add it to the cart.

---

# Features

* ✅ No hardcoded sleeps — Uses `WebDriverWait` with explicit expected conditions
* ✅ Modular design — Separate page object classes (`StorePage`, `SearchPage`, `ProductPage`, `CartPage`)
* ✅ Readable code — Clear class names and methods for maintainability
* ✅ Error handling — Catches exceptions and saves screenshots for debugging
* ✅ Proper waits — All interactions wait for elements to be ready

---

# Project Structure

```bash
AdNabuAutomation/
├── store_automation.py
├── requirements.txt
└── README.md
```

---

# Setup Instructions

## 1. Create Virtual Environment

```bash
cd D:\AdNabuAutomation
python -m venv venv
```

---

## 2. Activate Virtual Environment

### Windows PowerShell

```bash
.\venv\Scripts\Activate.ps1
```

### If execution policy error occurs

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Download ChromeDriver

## Option A — Automatic (Recommended)

Selenium 4.6+ automatically downloads the correct ChromeDriver.

No additional setup required.

---

## Option B — Manual

Download ChromeDriver from:

https://chromedriver.chromium.org/

* ChromeDriver version should match your Chrome browser version
* Place ChromeDriver in PATH or project folder

---

# Running the Script

```bash
python store_automation.py
```

---

# Automation Flow

1. Unlock Store using password
2. Search for product
3. Open product page
4. Add product to cart
5. Close cart drawer
6. Open cart again from cart icon
7. Verify product exists in cart

---

# Page Objects

## StorePage

* `visit(url)` → Navigate to store
* `unlock_store(password)` → Unlock password protected store

---

## SearchPage

* `search_and_navigate_to_product(name)` → Open product page

---

## ProductPage

* `get_product_name()` → Get product title
* `add_to_cart()` → Add product to cart

---

## CartPage

* `close_cart_drawer()` → Close cart drawer
* `open_cart()` → Open cart from cart icon
* `verify_product_in_cart(name)` → Verify product exists in cart

---

# Configuration

Update values in `store_automation.py`

```python
STORE_URL = "https://adnabu-store-assignment1.myshopify.com/"
STORE_PASSWORD = "AdNabuQA"
SEARCH_PRODUCT = "Selling Plans Ski Wax"
```

---

# Headless Mode

To run browser in background mode:

```python
chrome_options.add_argument("--headless")
```

---

# Wait Strategy

Uses Explicit Waits:

* `element_to_be_clickable()`
* `visibility_of_element_located()`
* `presence_of_element_located()`
* `invisibility_of_element_located()`

Default timeout:

```python
WebDriverWait(driver, 10)
```

---

# Troubleshooting

| Issue                  | Solution                                     |
| ---------------------- | -------------------------------------------- |
| ChromeDriver not found | Update Selenium or install webdriver-manager |
| TimeoutException       | Increase WebDriverWait timeout               |
| Element not found      | Verify XPath/CSS selector                    |
| Cart not opening       | Verify cart drawer selectors                 |
| Password issue         | Verify correct store password                |

---

# Example Output

```text
============================================================
ADNABU STORE AUTOMATION - SEARCH & ADD TO CART
============================================================

STEP 1: Store unlocked ✓
STEP 2: Product found ✓
STEP 3: Product added to cart ✓
STEP 4: Product verified in cart ✓

============================================================
AUTOMATION COMPLETED SUCCESSFULLY ✓
============================================================
```

---

# Future Improvements

* Add pytest framework
* Add logging
* Add HTML reports
* Add cross-browser support
* Add data-driven testing
* Add CI/CD pipeline

---

# Tech Stack

* Python
* Selenium WebDriver
* ChromeDriver
* Explicit Waits
* Page Object Model (POM)

---

# Author

Diksha Rani
