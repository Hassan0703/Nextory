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
bash
python3 --version


2️⃣ Install Dependencies

        pip install -r requirements.txt


For Linux:


        sudo apt install python3-tk
    (tkinter is required for the GUI prompts.)


3️⃣ Generate a GitHub Personal Access Token (Classic)
    ⚠ Use a classic token, not a fine-grained token.

Steps:

1- Go to GitHub → Settings → Developer settings

2- Navigate to Personal access tokens → Tokens (classic)

3- Click Generate new token (classic)

3- Name it (e.g., Nextory Commit Agent)

4- Set expiration (e.g., 90 days, 1 year)

5- Under Select scopes, check:
    repo ✅ (full control of private repositories, including creation)

6- Click Generate token

7- Copy the token immediately — GitHub won’t show it again


▶️ Run Nextory

    python main.py

When prompted:

1- Paste your GitHub token

2- Enter repository name (e.g., MyRepo or username/MyRepo)

3- Enter branch name (default: main)

4- Enter commits/day (default: 3)

5- Click OK — setup complete


🐞 Troubleshooting
Wrong Token or Repository Name?
Edit the config file:

Linux/Mac:
* nano ~/.nextory_agent/config.json *

Windows:
C:\Users\<YourUser>\.nextory_agent\config.json

Remove:

"token": "your-old-token",
"repository": "old-repo-name"
Save & rerun:


python main.py
Commits Not Appearing?
Check GitHub → Commits tab in your repository

Ensure the script is still running — closing the terminal stops it

If using an expiring token, ensure it’s still valid

-------------------------------------------------------------------------------------------------

==================  🐧 Linux – systemd User Service (Ubuntu Run at Startup)  ==================

1️⃣ Create the service file

nano ~/.config/systemd/user/nextory.service

Paste this file same given below:


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


2️⃣ Enable and start the service
    systemctl --user enable nextory
    systemctl --user start nextory

3️⃣ Check service status
    systemctl --user status nextory

This shows whether the service is running and any recent logs.

4️⃣ View live logs
    journalctl --user -u nextory -f

Press Ctrl + C to exit.

5️⃣ Stop or restart the service
    systemctl --user stop nextory
    systemctl --user restart nextory


===========================  🪟 Windows – Run at Startup  ===========================

1️⃣ Create a .bat file
Open Notepad and paste:


       * @echo off
        cd /d "C:\path\to\Nextory"
        python main.py *

Save it as:
    C:\Nextory\start_nextory.bat
Replace C:\path\to\Nextory with your actual folder path.

2️⃣ Open Task Scheduler

Press Windows + R, type:

    taskschd.msc 
Press Enter.

3️⃣ Create a new task
Click Create Task (not "Basic Task").

Name: Nextory Auto Commit Agent.

Check Run whether user is logged on or not.

Go to Triggers → New → "At log on".

Go to Actions → New → Program/script:


    C:\Nextory\start_nextory.bat

4️⃣ Allow running even when closed
In Settings tab, check:

✅ Allow task to be run on demand

✅ Run task as soon as possible after a scheduled start is missed

✅ If the task fails, restart every: 1 minute, Attempt: 3 times

5️⃣ Check if running & view logs
In Task Scheduler → Task Status, see if it says "Running".

To see logs, add this to your .bat file before python main.py:


    echo Starting Nextory at %date% %time% >> nextory_log.txt
    python main.py >> nextory_log.txt 2>&1

This will log all output to nextory_log.txt in your folder.




---

## 👨‍💻 Developed By
**Hassan Ali**

## 🎯 Presented To
**Team Nextash**  
🚀 Innovative automation & productivity solutions  
📧 Developer Contact: hassan4185767@gmail.com  
📧 Team Contact: support@nextash.com  
🌐 Website: [https://nextash.com](https://nextash.com)