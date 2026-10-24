"""
Helper script to push this repository to GitHub without needing git.exe installed.
Usage:
    python push_to_github.py <GITHUB_REPO_URL>
Example:
    python push_to_github.py https://github.com/username/ai-lab-experiments.git
"""
import sys
import os
import dulwich.porcelain as p

def push_to_remote(remote_url):
    repo_path = os.path.dirname(os.path.abspath(__file__))
    print(f"Repository: {repo_path}")
    print(f"Target GitHub URL: {remote_url}")

    # Set remote
    try:
        p.remote_add(repo_path, "origin", remote_url)
        print("Added remote 'origin'.")
    except Exception:
        print("Remote 'origin' already exists, continuing...")

    # Push to main
    try:
        print("Pushing commits to remote repository...")
        p.push(repo_path, "origin", "refs/heads/master:refs/heads/main")
        print("\nSUCCESS! Your repository has been pushed to GitHub.")
    except Exception as e:
        print(f"\nPush notice: {e}")
        print("If GitHub requires authentication, you can also push using GitHub CLI, Git Bash, or by uploading the folder directly on github.com.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        push_to_remote(sys.argv[1])
    else:
        url = input("Enter your GitHub repository URL (e.g. https://github.com/your-username/ai-lab.git): ").strip()
        if url:
            push_to_remote(url)
