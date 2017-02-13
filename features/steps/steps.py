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


@step('I visit "{path}"')
def step_impl(context, path):
    """
    :type context: behave.runner.Context
    """
    context.browser.get(context.base_url + path)
    print(context.browser.current_url)


@step('the page contains "{text}"')
def step_impl(context, text):
    """
    :type context: behave.runner.Context
    """
    assert text in context.browser.page_source