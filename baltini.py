import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    page.get_by_label("Search", exact=True).fill("Nordstrom Rack")
    page.get_by_role("link", name="Nordstrom Rack: Shop Clothes").click()
    page.get_by_role("link", name="View All Top 100 Deals").click()
    page.goto("https://www.nordstromrack.com/shop/top-100-deals?origin=recs-hp-top-100-deals-rack")

    with open('saving_nord.html', 'w',encoding='utf-8') as f:
        f.write(page.content())

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
