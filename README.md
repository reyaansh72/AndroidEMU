# AndroidEMU 🚀

A modular, standalone Python management framework designed to automate the installation, configuration, and execution of high-performance Android Virtual Devices (AVDs) without the resource overhead of Android Studio.

---

## 🛠️ Made With

📦 Developed using a minimal, high-efficiency stack:
* **Language:** Python 3.10+ 🐍
* **Target OS:** Windows 10 / 11 🪟
* **Core Binaries:** Google Android Emulator Tools 🤖

---

## ✨ Key Features

* 📦 **Standalone Deployment**: Eliminates the need for a full Android Studio installation, saving 10–15 GB of system storage by utilizing only the core Google emulation binaries.
* 🗂️ **Automated Environment Isolation**: Confines all workspace logs, `.ini` hardware templates, and virtual storage instances straight to a local runtime sandbox rather than polluting your global OS user profile.
* 💾 **Dynamic Storage Allocator**: Programmatically slices and mounts expandable `userdata.img` virtual partition blocks if existing developer files are missing.
* ⚡ **Hardware Acceleration Routing**: Injects specific environment variable blocks that automatically route graphics drawing pipelines directly to your native GPU via stable Windows DirectX 11.
* 🛠️ **Deep Dependency Resolver**: Recursively index-scans and appends nested system paths containing missing native rendering libraries (`glib-2-vs11.dll`, `libGLESv2.dll`, etc.) directly into active shell memory tables.

---

## 📂 System Architecture & Prerequisites

This program is modular and relies on internal library inter-communications. To run this software, you **must download the entire repository structure**, not just the individual core script.

Code output
File README.md successfully created.

```text
AndroidEMU/
├── app.py                  # Core terminal configuration interface and execution controller
├── .gitignore              # Structured UTF-8 system filter preventing tracking of multi-gigabyte OS zips
└── toolkit/                # Modular internal script automation helper libraries (MANDATORY REQUIREMENT)
    ├── ConsoleUtil.py      # Colorized production feedback output wrapper
    ├── FileUtil.py         # Local workspace validation check rules
    └── ZipUtil.py          # Fast file extraction pipeline
⚙️ Requirements
🐍 Python Dependencies
The framework is built using native Python standard libraries to keep deployment lightweight, meaning no external pip installations are required!

Python Version: Python 3.10 or higher.

Standard Modules Used: os, sys, subprocess, zipfile, shutil, pathlib.

🪟 System Dependencies
Operating System: Windows 10 or Windows 11 (64-bit).

Hypervisor: Virtual Machine Platform and Hyper-V layers must be enabled in the Windows Features control panel.

Graphics Hardware: Dedicated or integrated GPU supporting DirectX 11 or higher.

🚀 Installation & Execution
1. Deployment Steps
Clone or download this complete repository layout to your local machine as a structured folder.

Open your Command Prompt or PowerShell window inside the root directory:

PowerShell
cd path/to/AndroidEMU
Launch the environment manager by executing the primary script wrapper:

PowerShell
python app.py
2. 🔄 Automated Lifecycle Process
Once launched, the software manages the complete deployment pipeline sequentially:

🔍 Engine Verification: Inspects your project root for the emulation runtime layer and automatically pulls down official core assets if missing.

📱 Interactive Selection: Prompts you with an absolute terminal interface to select your preferred target image version (Android 10, 11, or 12).

⚡ Configuration & Boot: Downloads matching architectures, automatically fixes forward/backward string slash rules for text profiles, registers local AVD configurations, and maps out execution variables before opening the running visual device framework on your screen.

📝 License
This project is open-source software licensed under the terms of the MIT License. See the attached LICENSE file for complete text details.
