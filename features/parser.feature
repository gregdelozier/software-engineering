Feature: the parser processes strings into numbers

Scenario Outline: process single digits
   Given  we have a parser library imported
    When  we parse "<string>"
    Then  the returned value is <value>

  Examples: Single digits
    | string | value |
    | 1      | 1     |
    | 9      | 9     |
    | 0      | 0     |
    
    
Scenario: process single digits
   Given  we have a parser library imported
    When  we parse "1"
    Then  the returned value is 1 

Scenario: process single digits
   Given  we have a parser library imported
    When  we parse "9"
    Then  the returned value is 9 

Scenario: process single digits
   Given  we have a parser library imported
    When  we parse "0"
    Then  the returned value is 0 

Scenario: process multiple digits
   Given  we have a parser library imported
    When  we parse "19"
    Then  the returned value is 19 

Scenario: process negative numbers
   Given  we have a parser library imported
    When  we parse "-19"
    Then  the returned value is -19 
