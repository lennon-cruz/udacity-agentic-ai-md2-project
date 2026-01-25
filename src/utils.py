"""Logging utility to export agent results to artifacts."""

from pathlib import Path
from datetime import datetime


ARTIFACTS_DIR = Path(__file__).resolve().parent.parent / "artifacts"


def export_log(script_name: str, result: str) -> Path:
    """
    Write an agent result to a log file in root/artifacts.

    Log format: date/time, script name, then the result (usually agent response).

    Args:
        script_name: Name of the script that produced the result (e.g. "action_planning_agent").
        result: The output to log (typically the agent response as string).

    Returns:
        Path to the written log file.
    """
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = f"{ts} | {script_name}"
    separator = "-" * 60
    content = f"{header}\n{separator}\n{result}\n\n"
    log_file = ARTIFACTS_DIR / f"{script_name}.log"
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(content)
    return log_file
