from pathlib import Path

from playwright.async_api import (
    Locator,
    Page,
)

from markdownify import markdownify as md
from app.config.setting import OUTPUT_FILE



async def extractAndSavePageContent(page: Page):
        print("🐙 Melo: Saving Job Details...")
        # -------------------------
        # 1. Function
        # -------------------------

        function =await page.locator("#job-description span[ng-repeat*='job_function_dict']").inner_text()

        function = function.strip()

        # -------------------------
        # 2. Skills
        # -------------------------

        skills = await page.locator(
            "#job-skills-description li[ng-repeat*='keyword']"
        ).all_inner_texts()

        skills = [skill.strip() for skill in skills]

        # -------------------------
        # 3. Job Description
        # -------------------------

        description = page.locator(
            "div.profile-content.job-description"
        )

        await description.wait_for()

        description_html = await description.inner_html()

        description_md = md(
            description_html,
            heading_style="ATX",
            bullets="-",
        ).strip()

        # -------------------------
        # 4. Build Markdown
        # -------------------------

        markdown = f"""# Job Description

## Function

{function}

## Skills

{", ".join(skills)}

## Description

{description_md}
"""

        # -------------------------
        # 5. Save
        # -------------------------

        Path(OUTPUT_FILE).write_text(
            markdown,
            encoding="utf-8",
        )