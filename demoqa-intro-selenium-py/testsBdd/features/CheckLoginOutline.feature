# Created by chaker at 09/05/2025
Feature: Test the login functionality in demoqa web site
  This feature tests the login functionality with scenario outline

  Scenario Outline: Test Outline Login
    Given i open login page
    When i enter username value <username>
    When i enter password value <password>
    When i click in login button
    Then i verify the <status> login with <username>
    Examples:
      | username  | password   | status  |
      | ch_demoqa | Admin1234! | success |
      | chdemoqa  | Admin1234! | fail    |
      #| BenSalehdemoqa | Admin1234! | success |