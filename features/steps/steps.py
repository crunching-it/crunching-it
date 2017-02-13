from behave import step
import pexpect


@step('I run "{command}"')
def step_impl(context, command):
    """
    :type context: behave.runner.Context
    """
    context.child = pexpect.spawn(command, encoding='utf-8')


@step('I see "{output}"')
def step_impl(context, output):
    """
    :type context: behave.runner.Context
    """
    context.child.expect(output)
