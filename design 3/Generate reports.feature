Feature: View payroll reports
  As an Admin
  I want to view a report of all payroll activity
  So that I can assess company payroll expenses

  Scenario: Generate monthly report
    Given I am logged in as Admin
    And payroll entries exist for April 2025
    When I view the April report
    Then I should see all entries and total salary paid
.