sample check login: enter as username 'ch_demoqa' and password 'Admin1234!' to verify navigate to profile page with cross browser tests
step_defs\sample_check_login.py::test_sample_scenario_of_login[chrome] <- env\Lib\site-packages\pytest_bdd\scenario.py 
step_defs\sample_check_login.py::test_sample_scenario_of_login[firefox] <- env\Lib\site-packages\pytest_bdd\scenario.py 
step_defs\sample_check_login.py::test_sample_scenario_of_login[edge] <- env\Lib\site-packages\pytest_bdd\scenario.py 

================== 3 passed, 2 warnings in 77.85s (0:01:17) ===================
------------------- TEST : 'test_sample_scenario_of_login[chrome]' is running -------------------
PASSED [ 33%]
STEP 1: demoqa login page opened
STEP 2: username value entered
STEP 3: password value entered
STEP 4: login button clicked
Result: Login and navigate to profile page passed

------------------- TEST : 'test_sample_scenario_of_login[firefox]' is running -------------------
PASSED [ 66%]
STEP 1: demoqa login page opened
STEP 2: username value entered
STEP 3: password value entered
STEP 4: login button clicked
Result: Login and navigate to profile page passed

------------------- TEST : 'test_sample_scenario_of_login[edge]' is running -------------------
PASSED [100%]
STEP 1: demoqa login page opened
STEP 2: username value entered
STEP 3: password value entered
STEP 4: login button clicked
Result: Login and navigate to profile page passed
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
Test Scenario Outline: 
check_login_outline.py::test_test_outline_login[chrome-ch_demoqa-Admin1234!-success] <- env\Lib\site-packages\pytest_bdd\scenario.py 
check_login_outline.py::test_test_outline_login[chrome-chdemoqa-Admin1234!-fail] <- env\Lib\site-packages\pytest_bdd\scenario.py 
check_login_outline.py::test_test_outline_login[chrome-BenSalehdemoqa-Admin1234!-success] <- env\Lib\site-packages\pytest_bdd\scenario.py 

=================== 1 failed, 2 passed in 75.81s (0:01:15) ====================

------------------- TEST : 'test_test_outline_login[chrome-ch_demoqa-Admin1234!-success]' is running -------------------
PASSED [ 33%]
STEP 1: demoqa login page opened

STEP 2: username value entered

STEP 3: password value entered

STEP 4: login button clicked

RESULT: Status Login success

------------------- TEST : 'test_test_outline_login[chrome-chdemoqa-Admin1234!-fail]' is running -------------------
FAILED [ 66%]
STEP 1: demoqa login page opened
STEP 2: username value entered
STEP 3: password value entered
STEP 4: login button clicked

env\Lib\site-packages\pytest_bdd\scenario.py:295 (test_test_outline_login[chrome-chdemoqa-Admin1234!-fail])
fixturefunc = <function step_impl at 0x00000168517DF420>
request = <FixtureRequest for <Function test_test_outline_login[chrome-chdemoqa-Admin1234!-fail]>>
kwargs = {'driver': <selenium.webdriver.chrome.webdriver.WebDriver (session="0cbaa47a116852138f96d155e381793e")>, 'status': 'fail', 'username': 'chdemoqa'}

    def call_fixture_func(
        fixturefunc: _FixtureFunc[FixtureValue], request: FixtureRequest, kwargs
    ) -> FixtureValue:
        if is_generator(fixturefunc):
            fixturefunc = cast(
                Callable[..., Generator[FixtureValue, None, None]], fixturefunc
            )
            generator = fixturefunc(**kwargs)
            try:
                fixture_result = next(generator)
            except StopIteration:
                raise ValueError(f"{request.fixturename} did not yield a value") from None
            finalizer = functools.partial(_teardown_yield_fixture, fixturefunc, generator)
            request.addfinalizer(finalizer)
        else:
            fixturefunc = cast(Callable[..., FixtureValue], fixturefunc)
>           fixture_result = fixturefunc(**kwargs)

..\..\..\env\Lib\site-packages\_pytest\fixtures.py:898: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

driver = <selenium.webdriver.chrome.webdriver.WebDriver (session="0cbaa47a116852138f96d155e381793e")>
status = 'fail', username = 'chdemoqa'

    @then(parse('i verify the {status} login with {username}'))
    @then("i verify the <status> login with <username>")
    def step_impl(driver, status, username):
        # wait for 5 s for load page response
        time.sleep(5)
        try:
            if driver.current_url == "https://demoqa.com/profile" and username in driver.page_source and find(driver).text == username:
                print(f"RESULT: Status Login {status}")
            else:
>               pytest.fail(f"RESULT: Status Login {status}")
E               Failed: RESULT: Status Login fail

check_login_outline.py:68: Failed
------------------- TEST : 'test_test_outline_login[chrome-BenSalehdemoqa-Admin1234!-success]' is running -------------------
PASSED [100%]
STEP 1: demoqa login page opened
STEP 2: username value entered
STEP 3: password value entered
STEP 4: login button clicked
RESULT: Status Login success
