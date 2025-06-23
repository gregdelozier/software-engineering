Feature: Inventors are properly credited in wikipedia

  Scenario: Edison is credited as an inventor of the light bulb
    Given we have gone to the wikipedia search page
     When we search for "light bulb"
     Then the resulting page should contain "Thomas Edison"

  Scenario: Sikorsky is credited as an inventor of the helicopter
    Given we have gone to the wikipedia search page
     When we search for "helicopter"
     Then the resulting page should contain "Sikorsky"

  Scenario Outline: Inventors credited with inventions
    Given we have gone to the wikipedia search page
     When we search for "<invention>"
     Then the resulting page should contain "<inventor>"
    
    Examples:  Aviation
    | inventor | invention | 
    | Sikorsky | helicopter |
    | Wright | airplane |

    Examples: Appliances
    | inventor | invention | 
    | Edison | light bulb | 
    | Bell | telephone | 

