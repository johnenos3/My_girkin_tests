from behave import *
from selenium.webdriver import Chrome


@given(u'User open browser, enter URL and go to the app')
def step_impl(context):
    path = "C:\\CodeRepository\\Automation\\drivers\\chromedriver.exe"
    context.driver = Chrome(executable_path=path)
    context.driver.get('https://essayshark.com/')


@when(u'User enter new email in E-mail field of SOF')
def step_impl(context):
    context.driver.find_element_by_name('email').send_keys('test4324325435435546546@mailinator.com')


@when(u'User select type of paper in Type of Paper field of SOF')
def step_impl(context):
    context.driver.find_element_by_name('paper_type').click()
    context.driver.find_element_by_xpath('//*[@id="id_esof_paper_type"]/option[2]').click()


@when(u'User select deadline in Deadline field of SOF')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="dd_sof_deadline_date"]/span[1]/button').click()
    context.driver.find_element_by_class_name('dp_today').click()


@then(u'User see checkbox of Terms agreement and click on it')
def step_impl(context):
    assert context.driver.find_element_by_id('gdpr-checkbox-custom-policy').is_displayed()
    context.driver.find_element_by_id('gdpr-checkbox-policy').click()


# @then(u'User should be registered successfully and be on new order page of customer cabinet')
# def step_impl(context):
#
#
# @when(u'User enter email in E-mail field of SOF')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When User enter email in E-mail field of SOF')


# @then(u'User see login pop-up with active Password field')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then User see login pop-up with active Password field')
#
#
# @when(u'User enter password in Password field of login pop-up')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When User enter password in Password field of login pop-up')
#
#
# @when(u'User click Login button')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When User click Login button')
#
#
# @then(u'User should be on new order page of customer cabinet')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then User should be on new order page of customer cabinet')
