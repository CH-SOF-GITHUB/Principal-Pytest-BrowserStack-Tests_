TC003 Test with valid credentials:
("ch_demoqa", "Admin1234!"),
("BenSalehdemoqa", "Admin1234!"),
("TarekDemoQA", "Azerty1234!"),
("ali.tawfiki.01", "demoQA12345*")
FAILED test_demoqa_loginTC003.py::test_basic_demoqa_login_valid_credentials[chrome-ch_demoqa-Admin1234!] - Exception: Incomplete Test : Message: 
FAILED test_demoqa_loginTC003.py::test_basic_demoqa_login_valid_credentials[chrome-BenSalehdemoqa-Admin1234!] - urllib3.exceptions.ReadTimeoutError: HTTPConnectionPool(host='localhost', port=52666): Read timed out. (read timeout=120)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
TC004: Test login with invalid credentials:
("chdemoqa", "Admin1234!", "Invalid username or password!")
("BenSalehdemoqa", "A1234!", "Invalid username or password!"),
("TarekDemo", "Aze1234!", "Invalid username or password!"),
("TarekDemo", "", ""),
("", "A1234!", ""),
("", "", "")
test_fails_demoqa_loginTC004.py::test_basic_demoqa_login_invalid_credentials[chrome-chdemoqa-Admin1234!-Invalid username or password!] 
test_fails_demoqa_loginTC004.py::test_basic_demoqa_login_invalid_credentials[chrome---] 
test_fails_demoqa_loginTC004.py::test_basic_demoqa_login_invalid_credentials[firefox-chdemoqa-Admin1234!-Invalid username or password!] 
test_fails_demoqa_loginTC004.py::test_basic_demoqa_login_invalid_credentials[firefox---] 
test_fails_demoqa_loginTC004.py::test_basic_demoqa_login_invalid_credentials[edge-chdemoqa-Admin1234!-Invalid username or password!] 
test_fails_demoqa_loginTC004.py::test_basic_demoqa_login_invalid_credentials[edge---]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
test_fails_demoqa_loginTC004.py::test_basic_demoqa_login_invalid_credentials[chrome-chdemoqa-Admin1234!-Invalid username or password!] 
test_fails_demoqa_loginTC004.py::test_basic_demoqa_login_invalid_credentials[chrome-BenSalehdemoqa--] 
test_fails_demoqa_loginTC004.py::test_basic_demoqa_login_invalid_credentials[chrome---] 
test_fails_demoqa_loginTC004.py::test_basic_demoqa_login_invalid_credentials[firefox-chdemoqa-Admin1234!-Invalid username or password!] 
test_fails_demoqa_loginTC004.py::test_basic_demoqa_login_invalid_credentials[firefox-BenSalehdemoqa--] 
test_fails_demoqa_loginTC004.py::test_basic_demoqa_login_invalid_credentials[firefox---] 
test_fails_demoqa_loginTC004.py::test_basic_demoqa_login_invalid_credentials[edge-chdemoqa-Admin1234!-Invalid username or password!] 
test_fails_demoqa_loginTC004.py::test_basic_demoqa_login_invalid_credentials[edge-BenSalehdemoqa--] 
test_fails_demoqa_loginTC004.py::test_basic_demoqa_login_invalid_credentials[edge---] 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TC001 books: get list of books in profile
test_fetch_list_booksTC001.py::test_fetch_list__books[chrome] 

============================= 1 passed in 17.54s ==============================
BUG-PASS   [100%]
demoqa page opened with url: https://demoqa.com/login
Test Case STEPS:
STEP 1: username 'ch_demoqa' entered
STEP 2: password 'Admin1234!' entered
STEP 3: login button clicked !
------------- Loop through the 2 arrays of books to assert with expected title of book -------------
actual book: 'Git Pocket Guide' == expected book: 'Git Pocket Guide'
actual book: 'Learning JavaScript Design Patterns' == expected book: 'Learning JavaScript Design Patterns'
actual book: 'Designing Evolvable Web APIs with ASP.NET' == expected book: 'Designing Evolvable Web APIs with ASP.NET'
actual book: 'Speaking JavaScript' == expected book: 'Speaking JavaScript'
actual book: 'Programming JavaScript Applications' == expected book: 'Programming JavaScript Applications'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
