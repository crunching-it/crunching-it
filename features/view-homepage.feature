Feature: View homepage
  In order to use the application
  As a user
  I need to view the homepage

  Scenario: Viewing the homepage
    When I visit "/"
    Then the page contains "Congratulations on your first Django-powered page."