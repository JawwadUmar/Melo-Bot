from playwright.async_api import Locator, Page, expect


async def openURL(page: Page, url: str, timeout = 120000):
    await page.goto(url, timeout=timeout)

async def clickElement(element: Locator, timeout = 120000):
    await element.wait_for(state="visible", timeout = timeout)
    await expect(element).to_be_enabled(timeout=timeout)
    element_name = await element.inner_text(timeout=timeout)
    print(f"🐙 Melo: Clicked `{element_name}` ...")

    await element.click(timeout=timeout)