import requests

github_username = "SouvikNandi15"
github_token = "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"
pr_number = "" 
repository = "SouvikNandi15/PythAAt"

def merge_pull_request(pr_number, repository):
    url = f"https://api.github.com/repos/{repository}/pulls/{pr_number}/merge"
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.put(url, headers=headers)
    if response.status_code == 200:
        print("Pull request merged successfully!")
    else:
        print("Failed to merge pull request.")
        print("Error message:", response.json()["message"])



merge_pull_request(pr_number, repository)
