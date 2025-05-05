from pytest_bdd import scenario, given, when, then


@given("I'm an author user")
def step_impl():
    raise NotImplementedError(u'STEP: Given I\'m an author user')


@given("I have an article")
def step_impl():
    raise NotImplementedError(u'STEP: And I have an article')


@when("I go to the article page")
def step_impl():
    raise NotImplementedError(u'STEP: When I go to the article page')


@given("I press the publish button")
def step_impl():
    raise NotImplementedError(u'STEP: And I press the publish button')


@then("I should not see the error message")
def step_impl():
    raise NotImplementedError(u'STEP: Then I should not see the error message')


@given("the article should be published")
def step_impl():
    raise NotImplementedError(u'STEP: And the article should be published')