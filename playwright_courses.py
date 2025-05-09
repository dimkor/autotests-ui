from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    registration_page = context.new_page()

    registration_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = registration_page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = registration_page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = registration_page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = registration_page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path="playwright/browser-state.json")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='playwright/browser-state.json')
    dashboard_page = context.new_page()

    dashboard_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_title = dashboard_page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    courses_empty_icon = dashboard_page.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_empty_icon).to_be_visible()

    courses_empty_title = dashboard_page.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_empty_title).to_be_visible()
    expect(courses_empty_title).to_have_text('There is no results')

    courses_empty_description = dashboard_page.get_by_test_id('courses-list-empty-view-description-text')
    expect(courses_empty_description).to_be_visible()
    expect(courses_empty_description).to_have_text('Results from the load test pipeline will be displayed here')
