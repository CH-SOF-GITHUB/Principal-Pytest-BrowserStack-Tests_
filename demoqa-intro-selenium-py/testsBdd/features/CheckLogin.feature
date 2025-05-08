# Created by chaker at 08/05/2025
Feature: Test DemoQA Login Functionality
  This Feature tests a login functionality of demoqa site web.

  @Sample1
  Scenario: Sample scenario of Login
    Given i open login page
    When i enter username value
    When i enter password value
    When i click in login button
    Then navigate to profile page and success login