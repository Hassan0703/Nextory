# 🚀 Nextory – Auto Commit Agent (Prototype)

**Nextory** is an automated GitHub commit scheduler that creates or uses a private repository and makes small, harmless edits to `features.txt` at random times every day — keeping your GitHub contribution graph active.

---

## ✨ Features
- 📂 **Auto-create GitHub repository** (if it doesn’t exist)  
- ⏰ **Schedules 3 random commits per day** (default, configurable)  
- 📝 **Appends small content** to `features.txt` and pushes changes automatically  
- 🔒 **Securely stores** your GitHub Personal Access Token (PAT) in the OS keyring  
- 🖥 **Runs in the background** while `main.py` is active  

---

## ⚙ How It Works
When you run `main.py`, a GUI popup will:

1. 👋 Welcome you  
2. 🔑 Ask for your GitHub Personal Access Token  
3. 📦 Ask for the repository name (owner/repo format; if no owner, it creates under your account)  
4. 🌿 Ask for the branch name (default: `main`)  
5. 📆 Ask for number of commits per day (default: 3)  

**Then:**
- ✅ Creates the repo if it doesn’t exist  
- 📄 Uploads `features.txt` if missing  
- 🎯 Schedules commits at random times today  
- ✍ Adds harmless lines to `features.txt` and pushes commits  
- 🔄 Keeps running until you stop the script  

---

## 🛠 Setup Instructions

### 1️⃣ Install Python
Requires **Python 3.8+**.  
Check your version:
```bash
python3 --version
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
For Linux:

bash
Copy
Edit
sudo apt install python3-tk
tkinter is required for the GUI prompts.

3️⃣ Generate a GitHub Personal Access Token (Classic)
⚠ Use a classic token, not a fine-grained token.

Steps:

Go to GitHub → Settings → Developer settings

Navigate to Personal access tokens → Tokens (classic)

Click Generate new token (classic)

Name it (e.g., Nextory Commit Agent)

Set expiration (e.g., 90 days, 1 year)

Under Select scopes, check:

repo ✅ (full control of private repositories, including creation)

Click Generate token

Copy the token immediately — GitHub won’t show it again

▶️ Run Nextory
bash
Copy
Edit
python main.py
When prompted:

Paste your GitHub token

Enter repository name (e.g., MyRepo or username/MyRepo)

Enter branch name (default: main)

Enter commits/day (default: 3)

Click OK — setup complete

🐞 Troubleshooting
Wrong Token or Repository Name?
Edit the config file:

Linux/Mac:

bash
Copy
Edit
nano ~/.nextory_agent/config.json
Windows:

arduino
Copy
Edit
C:\Users\<YourUser>\.nextory_agent\config.json
Remove:

json
Copy
Edit
"token": "your-old-token",
"repository": "old-repo-name"
Save & rerun:

bash
Copy
Edit
python main.py
Commits Not Appearing?
Check GitHub → Commits tab in your repository

Ensure the script is still running — closing the terminal stops it

If using an expiring token, ensure it’s still valid

🐧 Linux – systemd User Service (Ubuntu Run at Startup)
1️⃣ Create the service file
bash
Copy
Edit
nano ~/.config/systemd/user/nextory.service
Paste:

ini
Copy
Edit
[Unit]
Description=Nextory Auto Commit Agent
After=network.target

[Service]
ExecStart=/usr/bin/env python3 /home/hassan/separate_folder/Nextory/main.py
WorkingDirectory=/home/hassan/separate_folder/Nextory
Restart=always
User=hassan
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=default.target
⚠ Replace /home/hassan/separate_folder/Nextory with your actual folder path.
User=hassan should match your Linux username.

2️⃣ Enable and Start the Service
bash
Copy
Edit
systemctl --user enable nextory
systemctl --user start nextory
3️⃣ Check Service Status
bash
Copy
Edit
systemctl --user status nextory
4️⃣ View Live Logs
bash
Copy
Edit
journalctl --user -u nextory -f
Press Ctrl + C to exit.

5️⃣ Stop or Restart the Service
bash
Copy
Edit
systemctl --user stop nextory
systemctl --user restart nextory
🪟 Windows – Run at Startup
1️⃣ Create a .bat File
Open Notepad and paste:

bat
Copy
Edit
@echo off
cd /d "C:\path\to\Nextory"
python main.py
Save as:

makefile
Copy
Edit
C:\Nextory\start_nextory.bat
Replace C:\path\to\Nextory with your actual folder path.

2️⃣ Open Task Scheduler
Press Windows + R, type:

Copy
Edit
taskschd.msc
Press Enter.

3️⃣ Create a New Task
Name: Nextory Auto Commit Agent

Check Run whether user is logged on or not

Go to Triggers → New → At log on

Go to Actions → New → Program/script:

makefile
Copy
Edit
C:\Nextory\start_nextory.bat
4️⃣ Allow Running Even When Closed
In Settings tab, check:

✅ Allow task to be run on demand

✅ Run task as soon as possible after a scheduled start is missed

✅ If the task fails, restart every: 1 minute, Attempt: 3 times

5️⃣ Check If Running & View Logs
Add to your .bat file before python main.py:

bat
Copy
Edit
echo Starting Nextory at %date% %time% >> nextory_log.txt
python main.py >> nextory_log.txt 2>&1
This logs all output to nextory_log.txt in your folder.

👨‍💻 Developed By
Hassan Ali

🎯 Presented To
Team Nextash
🚀 Innovative automation & productivity solutions
📧 Developer Contact: hassan4185767@gmail.com
📧 Team Contact: support@nextash.com
🌐 Website: https://nextash.com

