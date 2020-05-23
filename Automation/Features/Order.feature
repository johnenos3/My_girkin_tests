Feature: Verify creating first order

  Background:
    Given User open browser, enter URL and go to the app

  @smoke
  Scenario: Creating first order by new user
    When User enter new email in E-mail field of SOF
    And  User select type of paper in Type of Paper field of SOF
    And  User select deadline in Deadline field of SOF
    Then User see checkbox of Terms agreement and click on it


  @regression
  Scenario: Creating first order by existed user
    When User enter email in E-mail field of SOF
    And  User select type of paper in Type of Paper field of SOF
    And  User select deadline in Deadline field of SOF
    And  User click Continue button to submit SOF
    Then User see login pop-up with active Password field
    When User enter password in Password field of login pop-up
    And  User click Login button
    Then User should be on new order page of customer cabinet