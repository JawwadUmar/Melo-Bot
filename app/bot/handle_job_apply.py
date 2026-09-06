from playwright.async_api import (
    Error,
    Locator,
    Page,
)

from app.bot.apply_decision import shouldApply
from app.bot.save_job_details import save_to_markup_file
from app.config.setting import JOBLINK
from app.utils.human import human_delay
from app.utils.page_actions import clickElement, openURL


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
            job_data, shouldApplyToJob = await shouldApply(page)
            if (shouldApplyToJob):
                applyButtonElement: Locator = page.get_by_role("button", name="Apply", exact=False).locator("visible=true").first
                save_to_markup_file(job_data)
                await clickElement(applyButtonElement)
                job_count += 1
                print(f"✅ Melo: Applied to job #{job_count}!")
            else:
                ignoreButtonElement: Locator = page.get_by_role("button", name="Not Interested", exact=False).locator("visible=true").first
                await clickElement(ignoreButtonElement)
                print(f"✅ Melo: Skipped job #{job_count}!")
            

            await human_delay(2, 4)
        except Error as e:
            print(f"ℹ️ Melo: Completed or loop stopped: {e}")
            break


    
