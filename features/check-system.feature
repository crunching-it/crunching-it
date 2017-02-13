Feature: Check system
  In order to deploy confidently
  As a developer
  I need to know that there are no system errors

  Scenario: No arguments
    When I run "python manage.py check"
    Then I see "System check identified no issues"
