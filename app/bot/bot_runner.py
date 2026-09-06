import asyncio

from playwright.async_api import (
     BrowserContext,
     Page,
     async_playwright,
)

from app.bot.handle_job_apply import applyToJobs
from app.bot.handle_login import handleLogin
from app.config.setting import USER_DATA_DIRECTORY


async def run_bot():
     async with async_playwright() as p:
        context: BrowserContext = await p.chromium.launch_persistent_context(user_data_dir = USER_DATA_DIRECTORY, headless=False)
        page: Page = await context.new_page()
    
        await handleLogin(page)

        await applyToJobs(page)

        await asyncio.to_thread(input,"Browser is still open. Press Enter to close it...")
        await context.close()



