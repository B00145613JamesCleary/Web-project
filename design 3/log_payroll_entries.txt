Feature: Log payroll entries
  As a Manager
  I want to enter payroll data for an employee
  So that the system can calculate their salary

  Scenario: Add valid payroll entry
    Given I am logged in as Manager
    And John Doe exists in the employee database
    When I log 40 hours and €50 bonus for John for March
    Then the payroll entry should be saved
    And John's salary should reflect the update
