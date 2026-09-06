from datetime import datetime
from pathlib import Path

from playwright.async_api import Error, Page

from app.config.setting import OUTPUT_FILE


async def _safe_inner_text(locator, default: str = "N/A", timeout: int = 4000) -> str:
    try:
        await locator.wait_for(state="visible", timeout=timeout)
        text = await locator.inner_text()
        return text.strip() if text else default
    except Error:
        return default




async def extractPageContent(page: Page) -> dict:
    print("🐙 Melo: Extracting Job Details...")
    try:
        await page.locator(".profile-heading").wait_for(state="visible", timeout=10000)
    except Error:
        print("⚠️ Melo: Job modal profile heading not visible yet.")

    
    job_title = await _safe_inner_text(page.locator(".profile-heading .profile-info h1"))
    company = await _safe_inner_text(page.locator(".profile-heading .company-name"))
    location = await _safe_inner_text(page.locator(".profile-heading .job-locations > span:first-child"))
    experience = await _safe_inner_text(page.locator(".profile-heading .job-locations .experience"))
    recruiter = await _safe_inner_text(page.locator(".profile-heading .rec-name"))
    designation = await _safe_inner_text(page.locator(".profile-heading .designation"))
    summary = await _safe_inner_text(page.locator("#job-description span[ng-repeat*='job_function_dict']"))
    description = await _safe_inner_text(page.locator("div.profile-content.job-description"))

    
    try:
        skills_locator = page.locator("#job-skills-description li[ng-repeat*='keyword']")
        skills = await skills_locator.all_inner_texts()
        skills = [skill.strip() for skill in skills if skill and skill.strip()]
    except Error:
        skills = []

    return {
        "job_title": job_title,
        "company": company,
        "location": location,
        "experience": experience,
        "recruiter": recruiter,
        "designation": designation,
        "summary": summary,
        "skills": skills,
        "description": description
    }



def save_to_markup_file(job_data: dict):
    
    """
    Append a job to the Markdown file.

    Jobs are grouped by application date:

    ### 2026-08-18

    ## Senior Software Engineer

    ...

    ---

    ## Another Job

    ...
    """

    job_title = job_data.get("job_title", "")
    company = job_data.get("company", "")
    location = job_data.get("location", "")
    experience = job_data.get("experience", "")
    recruiter = job_data.get("recruiter", "")
    designation = job_data.get("designation", "")
    summary = job_data.get("summary", "")
    skills = job_data.get("skills", [])
    description = job_data.get("description", "")

    output_file = Path(OUTPUT_FILE)

    # Make sure the parent directory exists
    output_file.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    # Current date
    today = datetime.now().astimezone().date().isoformat()

    # -----------------------------
    # Clean values
    # -----------------------------

    job_title = job_title.strip()
    company = company.strip()
    location = location.strip()
    experience = experience.strip()
    recruiter = recruiter.strip()
    designation = " ".join(designation.split())
    summary = " ".join(summary.split())

    # Remove accidental empty skills
    skills = [
        skill.strip()
        for skill in skills
        if skill and skill.strip()
    ]

    # -----------------------------
    # Build job Markdown
    # -----------------------------

    job_markdown = f"""## {job_title}

**Company:** {company}  
**Location:** {location}  
**Experience:** {experience}  

### Recruiter

**Name:** {recruiter}  
**Designation:** {designation}

### Function

{summary}

### Skills

{", ".join(skills)}

### Job Description

{description}

"""

    # -----------------------------
    # Read existing file
    # -----------------------------

    if output_file.exists():
        existing_content = output_file.read_text(
            encoding="utf-8"
        )
    else:
        existing_content = ""

    # -----------------------------
    # Check whether today's
    # date section exists
    # -----------------------------

    date_heading = f"### {today}"

    if date_heading in existing_content:
        # Date already exists.
        #
        # Append the job at the end of the
        # existing date section.
        updated_content = (
            existing_content.rstrip()
            + "\n\n"
            + job_markdown
            + "\n---\n"
        )

    else:
        # Date doesn't exist yet.
        #
        # Add a new date section.
        if existing_content.strip():
            updated_content = (
                existing_content.rstrip()
                + "\n\n"
                + date_heading
                + "\n\n"
                + job_markdown
                + "\n---\n"
            )
        else:
            updated_content = (
                "# Job Applications\n\n"
                + date_heading
                + "\n\n"
                + job_markdown
                + "\n---\n"
            )

    # -----------------------------
    # Write back to file
    # -----------------------------

    output_file.write_text(
        updated_content,
        encoding="utf-8",
    )

    print(
        f"✅ Melo: Job details appended to {output_file}"
    )