from selenium.webdriver import Firefox


def before_all(context):
    context.browser = Firefox()
    context.base_url = 'http://localhost:8000'


def after_all(context):
    context.browser.quit()
    context.browser = None
