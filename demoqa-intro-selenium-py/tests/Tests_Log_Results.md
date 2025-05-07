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
("", "", "")
test_fails_demoqa_loginTC004.py::test_basic_demoqa_login_invalid_credentials[chrome-chdemoqa-Admin1234!-Invalid username or password!] 
test_fails_demoqa_loginTC004.py::test_basic_demoqa_login_invalid_credentials[chrome---] 
test_fails_demoqa_loginTC004.py::test_basic_demoqa_login_invalid_credentials[firefox-chdemoqa-Admin1234!-Invalid username or password!] 
test_fails_demoqa_loginTC004.py::test_basic_demoqa_login_invalid_credentials[firefox---] 
test_fails_demoqa_loginTC004.py::test_basic_demoqa_login_invalid_credentials[edge-chdemoqa-Admin1234!-Invalid username or password!] 
test_fails_demoqa_loginTC004.py::test_basic_demoqa_login_invalid_credentials[edge---] 