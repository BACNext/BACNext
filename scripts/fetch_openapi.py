import httpx
import os

API_KEY = os.environ.get("APIFOX_API_KEY")

moduleIds = [7055935, 7056204, 7056214, 7073331, 7073289, 7073367]

moduleId_to_filename = {
    7055935: "main.json",
    7056204: "hyg.json",
    7056214: "passport.json",
    7073331: "live.json",
    7073289: "vc.json",
    7073367: "biligame.json",
}

for moduleId in moduleIds:
    response = httpx.post(
        "https://api.apifox.com/v1/projects/7776376/export-openapi?locale=zh-CN",
        headers={
            "X-Apifox-Api-Version": "2024-03-28",
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "scope": {
                "type": "ALL"
            },
            "options": {
                "addFoldersToTags": True
            },
            "oasVersion": "3.1",
            "exportFormat": "JSON",
            "moduleId": moduleId
        }
    )
    response.raise_for_status()
    error_occured = False
    try:
        with open(f"openapi/{moduleId_to_filename[moduleId]}", "w", encoding="utf-8") as f:
            f.write(response.text)
    except Exception as e:
        error_occured = True
        print(f"Failed to write file for moduleId {moduleId}: {e}")
    else:
        print(f"Successfully wrote file for moduleId {moduleId}")

if error_occured:
    exit(1)