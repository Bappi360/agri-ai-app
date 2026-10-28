"""
Automatic GitHub Repository Creator & Pusher for AgriSathi AI
"""

import sys
import subprocess
import requests

def create_and_push(token: str, repo_name: str = "agri-ai-app"):
    token = token.strip()
    if not token:
        print("❌ Error: GitHub Token cannot be empty!")
        return False
        
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # 1. Verify User
    print("⏳ Verifying GitHub authentication...")
    user_res = requests.get("https://api.github.com/user", headers=headers)
    if user_res.status_code != 200:
        print(f"❌ GitHub Authentication Failed ({user_res.status_code}): {user_res.text}")
        return False
        
    user_data = user_res.json()
    username = user_data.get("login")
    print(f"✅ Authenticated as GitHub user: @{username}")
    
    # 2. Create Repository
    print(f"⏳ Creating repository '{repo_name}' on GitHub...")
    repo_payload = {
        "name": repo_name,
        "description": "AgriSathi AI (কৃষি সাথী এআই) - Smart Bilingual Agricultural Assistant for Crops, Diseases & Fertilizers",
        "private": False,
        "auto_init": False
    }
    
    repo_res = requests.post("https://api.github.com/user/repos", headers=headers, json=repo_payload)
    if repo_res.status_code == 201:
        print(f"✅ Repository successfully created: https://github.com/{username}/{repo_name}")
    elif repo_res.status_code == 422:
        print(f"ℹ️ Repository '{repo_name}' already exists. Continuing to push...")
    else:
        print(f"❌ Failed to create repository ({repo_res.status_code}): {repo_res.text}")
        return False
        
    # 3. Configure Git remote & push
    auth_remote_url = f"https://{token}@github.com/{username}/{repo_name}.git"
    public_repo_url = f"https://github.com/{username}/{repo_name}"
    
    print("⏳ Configuring Git remote...")
    subprocess.run(["git", "remote", "remove", "origin"], capture_output=True)
    add_remote = subprocess.run(["git", "remote", "add", "origin", auth_remote_url], capture_output=True, text=True)
    if add_remote.returncode != 0:
        print(f"Git remote error: {add_remote.stderr}")
        
    print("⏳ Pushing code to GitHub main branch...")
    push_res = subprocess.run(["git", "push", "-u", "origin", "main"], capture_output=True, text=True)
    
    # Clean up token from remote url for security
    subprocess.run(["git", "remote", "set-url", "origin", f"https://github.com/{username}/{repo_name}.git"], capture_output=True)
    
    if push_res.returncode == 0:
        print("\n🎉 SUCCESS! All code has been pushed to your GitHub!")
        print(f"🔗 Repository: {public_repo_url}")
        print(f"👉 Deploy to Streamlit Cloud: https://share.streamlit.io/deploy?repository={username}/{repo_name}&branch=main&mainModule=app.py")
        return True
    else:
        print(f"❌ Push failed:\n{push_res.stderr}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        token = sys.argv[1]
    else:
        token = input("Enter your GitHub Personal Access Token (ghp_...): ").strip()
    create_and_push(token)
