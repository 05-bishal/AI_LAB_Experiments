"""
Script to create the AI_LAB_Experiments GitHub repository and push code automatically.
"""
import sys
import os
import requests
import dulwich.porcelain as p

REPO_NAME = "AI_LAB_Experiments"
DESCRIPTION = "AI Lab Experiments (Experiments 1-10) with source code and outputs"

def create_and_push(username, token):
    repo_path = os.path.dirname(os.path.abspath(__file__))
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    
    print(f"Checking / creating repository '{REPO_NAME}' for user '{username}'...")
    create_url = "https://api.github.com/user/repos"
    payload = {
        "name": REPO_NAME,
        "description": DESCRIPTION,
        "private": False,
        "auto_init": False
    }
    
    res = requests.post(create_url, headers=headers, json=payload)
    if res.status_code == 201:
        print(f"Successfully created repository: https://github.com/{username}/{REPO_NAME}")
    elif res.status_code == 422:
        print(f"Repository '{REPO_NAME}' already exists on GitHub. Proceeding to push updates...")
    else:
        print(f"GitHub API Error ({res.status_code}): {res.text}")
        return False
        
    auth_remote = f"https://{username}:{token}@github.com/{username}/{REPO_NAME}.git"
    print(f"Pushing code to GitHub ({REPO_NAME})...")
    
    try:
        p.push(repo_path, auth_remote, refspecs="refs/heads/main")
        print("\nSUCCESS! Successfully pushed branch 'main' to GitHub!")
        print(f"Your repository is live at: https://github.com/{username}/{REPO_NAME}")
        return True
    except Exception as e:
        print(f"Push to 'main' encountered: {e}")
        try:
            print("Trying push from 'master:main'...")
            p.push(repo_path, auth_remote, refspecs="refs/heads/master:refs/heads/main")
            print("\nSUCCESS! Successfully pushed to GitHub!")
            print(f"Your repository is live at: https://github.com/{username}/{REPO_NAME}")
            return True
        except Exception as e2:
            print(f"Push failed: {e2}")
            return False

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        user = sys.argv[1].strip()
        tok = sys.argv[2].strip()
        create_and_push(user, tok)
    else:
        user = input("GitHub Username: ").strip()
        tok = input("GitHub Personal Access Token: ").strip()
        if user and tok:
            create_and_push(user, tok)
