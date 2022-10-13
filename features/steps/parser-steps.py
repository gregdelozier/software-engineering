from parser import parse

@given(u'we have a parser library imported')
def step_impl(context):
    pass

@when(u'we parse "{number}"')
def step_impl(context, number):
    context.value = parse(number)

@then(u'the returned value is {number}')
def step_impl(context, number):
    assert context.value == int(number)

