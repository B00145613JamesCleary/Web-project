Feature: generate payslip
  As a Manager
  I want to generate a payslip from payroll data
  So that employees can view their earnings

  Scenario: Generate payslip after payroll data
    Given I have logged a payroll entry for "John Doe"
    When I generate the payslip
    Then the payslip PDF should be created
    And it should include hours, bonuses, and total pay
.