# test STELLAR_BURGER site (https://stellarburgers.nomoreparties.site/). The coll_fill function helps you create a test collector and fill it with the books you need for the test from dictionary.
# locators.py contains a list of locators used in tests.
  # Registration form(test_registration.py class TestRegistration)
      test_registration_valid_account
      test_registration_pass_less_than_6

  # Parametrized test contains 4 Different ways to Enter(test_enter.py class TestEnter)
      test_enter_by_any_button
	  
  # Personal cabinet (test_personal_cab.py class TestPersonalCab)
    # Enter by existing account and click the button 'Personal cabinet'
      test_click_personal_cab
	  
  # Personal cabinet click to constructor(test_personal_cab_to_constructor.py class TestPersonalCabToConstructor)
    # Enter by existing account and click the button 'Personal cabinet' then click the button 'constructor'
      test_personal_cab_to_constructor_click
    # Enter by existing account and click the button 'Personal cabinet' then click the button 'logo'
      test_personal_cab_to_logo_click

  # Personal cabinet exit(test_exit_from_account.py class TestExitFromAccount)
    # Enter by existing account and click the button 'Personal cabinet' then click the button 'exit'
      test_exit_from_account
	  
  # Main page(constructor)(test_constructor_section_transitions.py class TestConstructorSectionTransitions)
    # Enter by existing account and click the button 'Personal cabinet' then click the button 'constructor'
    # with default section "BULKI" then click section "SOUSY"
      test_constructor_select_sousy
    # with default section "BULKI" then click section "NACHINKI"
      test_constructor_select_nachinki
    # with default section "BULKI" then click section "NACHINKI" and then click section "BULKI"
      test_constructor_select_bulki
	  
	  
	  
	  	

