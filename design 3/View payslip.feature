Feature: View payslip
  As an Employee
  I want to view my payslip
  So that I can confirm my salary for a given month

  Scenario: View available payslip
    Given I am logged in as Employee
    And a payslip for March 2025 exists
    When I go to the Payslip page
    Then I should see my full salary breakdown.
