# Created by chaker at 10/05/2025
Feature: Navigate between pages of book store, login, profile
  Test of functionality to navigate between different pages: book store, login and profile

  Scenario: switch between book store, login, profile
    Given i open login page
    When i navigate to profile
    When i navigate to book store
    Then i logout with success