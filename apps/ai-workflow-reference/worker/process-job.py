"""Reference-only worker entrypoint for AI-heavy async jobs.

AI provider calls belong here, behind adapters and retry boundaries.
"""

def process_job(job_envelope: dict) -> dict:
    return {
        "jobId": job_envelope["jobId"],
        "status": "succeeded",
        "summary": "Reference worker processed the job.",
    }
