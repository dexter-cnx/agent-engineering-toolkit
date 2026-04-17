from typing import Any


def run(job: dict[str, Any]) -> dict[str, Any]:
  return {
      "jobId": job["jobId"],
      "status": "succeeded",
      "result": {"summary": "Example worker task complete"},
  }
