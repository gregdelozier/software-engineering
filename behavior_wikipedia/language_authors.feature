Feature: language authors cited on wikipedia pages

  Scenario: search for Python, we find reference to Guido
     Given we are browsing wikipedia home page
      When we search for "Python (the programming language)"
      Then we will see a reference to "Guido"

  Scenario: search for C++, we find reference to Bjarne Stroustrup
     Given we are browsing wikipedia home page
      When we search for "C++"
      Then we will see a reference to "Bjarne Stroustrup"

  Scenario: search for Pascal, we find reference to Niklaus Wirth
     Given we are browsing wikipedia home page
      When we search for "Pascal (the programming language)"
      Then we will see a reference to "Niklaus Wirth"
