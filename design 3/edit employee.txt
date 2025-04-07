Feature: edit employee details
  As a Manager
  I want to update an employee's role or salary
  So that HR records are accurate

  Scenario: Update employee base salary
    Given I am logged in as Manager
    When I change the salary of "John" to €3,200
    Then their record should reflect the new amount
.