# Created by chaker at 28/04/2025
Feature: Writing Our First Web UI Test
  Test cases are procedures that exercise behavior to verify goodness and identify badness.

  Scenario: duckduck go search test
    Given the duckduck go home page is displayed
    When the user searches for "panda"
    Then the search result title contains "panda"
    And the search result query is "panda"
    And the search result links pertain to "panda"