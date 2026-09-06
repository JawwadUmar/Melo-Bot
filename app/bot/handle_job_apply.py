from playwright.async_api import (
    Locator,
    Page,
)

from app.config.setting import JOBLINK
from app.bot.save_job_details import extractAndSavePageContent


async def applyToJobs(page: Page):
    current_url = page.url

    if current_url != JOBLINK:
        current_url = JOBLINK
        await page.goto(current_url)

    viewButtonElement: Locator = page.get_by_role("button", name="View", exact=False).locator("visible=true").first
    await viewButtonElement.wait_for(state="visible", timeout=60000)
    await viewButtonElement.click()
    await extractAndSavePageContent(page)

    
