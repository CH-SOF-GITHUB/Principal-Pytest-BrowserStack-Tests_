✅ Why it's a great choice
- Contains a login form for UI testing with Selenium.
- Book list is dynamically loaded — ideal for element location and interaction.
- --------------------------------------------------------------------------------- -
+ Offers a REST API for:
- Authentication
- Retrieving book data
- Adding/deleting user accounts
- Provides real JSON responses for API testing.
- No signup or token needed for basic browsing.

📦 Suggested Tests
🔹 UI Tests with Selenium + Pytest
+ Login page 
  ° Test valid/invalid credentials
  ° Test empty fields
+ Book list
  ° Verify books are displayed
  ° Click a book and check details
+ Navigation 
  ° Test switching between pages (Book Store, Login, Profile)

🔹 API Tests with Pytest + requests
+ GET /Books
- Verify response status 200 
- Check the number of books returned 
- POST /Account/v1/GenerateToken 
- Verify valid token creation 
- Test with invalid credentials
+ POST /Account/v1/User 
- Register a new user
- Handle duplicate users
- Authorized GET
+ Try retrieving user info with and without token

⚙️ Tools & Stack
- Python 3.9+
- Pytest
- Selenium (for UI tests)
- Requests (for API tests)
- Allure (for reporting) (optional)

Would you like me to generate a sample folder structure and test files (test_ui_login.py, test_api_books.py) to get you started?