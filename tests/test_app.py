import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from app import activities, signup_for_activity, get_activities


def test_github_skills_activity_exists():
    activities_payload = get_activities()

    assert "GitHub Skills" in activities_payload

    activity = activities_payload["GitHub Skills"]
    assert "GitHub" in activity["description"]
    assert activity["max_participants"] > 0


def test_github_skills_activity_accepts_signups():
    email = "student@mergington.edu"
    activity_name = "GitHub Skills"

    if email in activities[activity_name]["participants"]:
        activities[activity_name]["participants"].remove(email)

    response = signup_for_activity(activity_name, email)

    assert response["message"] == f"Signed up {email} for {activity_name}"
    assert email in activities[activity_name]["participants"]
