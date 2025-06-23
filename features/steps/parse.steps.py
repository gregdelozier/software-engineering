from parse2 import parse

@given('we have a string "{s}"')
def step_impl(context,s):
    context.s = s


@when(u'when we call the parse function with that string')
def step_impl(context):
    context.result = parse(context.s)


@then(u'we should get a {n}')
def step_impl(context,n):
    assert context.result == float(n)
