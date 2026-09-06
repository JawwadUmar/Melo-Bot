from playwright.async_api import (
    Locator,
    Page,
)

from app.bot.save_job_details import extractAndSavePageContent
from app.config.setting import JOBLINK
from app.utils.page_actions import clickElement, openURL
from app.utils.human import human_delay


async def applyToJobs(page: Page):
    current_url = page.url

    if current_url != JOBLINK:
        current_url = JOBLINK
        await openURL(page, current_url)

    print("🐙 Melo: Looking for jobs...")
    viewButtonElement: Locator = page.get_by_role("button", name="View", exact=False).locator("visible=true").first
    await clickElement(viewButtonElement)

    job_count = 0
    while True:
        try:
            await extractAndSavePageContent(page)
            job_count += 1

            applyButtonElement: Locator = page.get_by_role("button", name="Apply", exact=False).locator("visible=true").first
            await clickElement(applyButtonElement)
            print(f"✅ Melo: Applied to job #{job_count}!")

            await human_delay(2, 4)
        except Exception as e:
            print(f"ℹ️ Melo: Completed or loop stopped: {e}")
            break


    
