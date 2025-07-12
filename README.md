## Sauce Demo UI Automation with Playwright & Python
This project is a UI automation framework built using Playwright with Python for testing the SauceDemo (https://www.saucedemo.com/) application. 
It follows the Page Object Model (POM) design pattern and includes both Happy Path and Negative Path test scenarios.

## Project Structure
```text
project-root/
├── pageObjectModel/
│   ├── login.py
│   ├── inventory.py
│   ├── userDetailPage.py
│   └── orderHistorypage.py
├── data/
│   └── credentials.json
├── playwright_3/
│   └── test_end_end_framework.py
├── videos1/
├── videos2/
├── conftest.py
└── report1.html
```
## Test Scenarios
Happy Path
- Login with all valid users (except locked out user)
- Add items from the inventory
- Enter user details
- Verify order history

Negative Path
- Attempt login with locked_out_user
- Verify appropriate error message is displayed
- Exit test suite if locked out scenario is triggered

## Test Data
Test cerdentials are stored in json
```text
{
  "user_credentials": [
    {
      "username": "standard_user",
      "password": "secret_sauce"
    },
    {
      "username": "locked_out_user",
      "password": "secret_sauce"
    }
  ]
}
```

## How to Run
1. Clone the Repository:
git clone https://github.com/sakshi36/SA-QA--Sakshi_Shejwal-..git
cd saucedemo-playwright
2. Create Virtual Environment (optional):
python -m venv venv
venv\Scripts\activate    # Windows
3. Install Dependencies:
pip install -r requirements.txt
4. Install Playwright Browsers:
playwright install




