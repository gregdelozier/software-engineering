@given(u'we want to run a test')
def step_impl(context):
    print("I guess we want to run a test..")

@when(u'we run a test')
def step_impl(context):
    print("We are running the test")
    context.activity = "running the test"

@then(u'we will have a result')
def step_impl(context):
    print("We have a result; we succeeded in " + context.activity)

@when(u'we sing the happy birthday song')
def step_impl(context):
    print("We are singing the song")
    context.activity = "singing the song"

