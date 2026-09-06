from playwright.async_api import Locator, Page
from playwright.async_api import TimeoutError as PlaywrightTimeoutError

from app.config.setting import EMAIL, PASSWORD
from app.utils.human import human_delay, human_typing


async def handleLogin(page: Page):
    print("🐙 Melo: Handling Login...")

    await page.goto("https://www.instahyre.com/login")
    await page.wait_for_load_state("domcontentloaded")

    # If session is active, Instahyre automatically redirects to candidate feed
    if "/candidate/" in page.url:
        print("✅ Melo: Already logged in (session restored)!")
        return

    emailElement: Locator = page.get_by_label("Email", exact=True).locator("visible=true").first
    passwordElement: Locator = page.get_by_label("Password", exact=True).locator("visible=true").first
    submitButtonElement: Locator = page.get_by_role("button", name="Login", exact=True).locator("visible=true").first

    await emailElement.click()
    await human_typing(emailElement, EMAIL)

    await passwordElement.click()
    await human_typing(passwordElement, PASSWORD)

    await submitButtonElement.click()

    print("🐙 Melo: Waiting for login to complete (please solve 2FA if prompted)...")

    try:
        # Wait up to 2 minutes for the URL to change to the Instahyre feed, confirming login is successful
        await page.wait_for_url("**/candidate/**", timeout=120000)
        print("✅ Melo: Login confirmed!")
    except PlaywrightTimeoutError:
        print("⚠️ Melo: Login timed out or failed. Check the browser.")

    await page.wait_for_load_state("load")
    await human_delay()




