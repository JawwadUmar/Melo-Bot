from playwright.async_api import (
    Page,
)

from app.bot.save_job_details import extractPageContent
from app.config.excluded_jobs import isExcludedJob
from app.config.skills import skillMatch


async def shouldApply(page: Page)->tuple[dict, bool]:
    job_data = await extractPageContent(page)
    job_title = job_data.get("job_title", "")
    company_name = job_data.get("company", "")

    if isExcludedJob(job_title, company_name):
        return job_data, False

    skills = job_data.get("skills", [])

    if skillMatch(skills):
        return job_data, True

    return job_data, False






