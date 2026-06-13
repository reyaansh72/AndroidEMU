# AndroidEMU 🚀

> **Run Android Virtual Devices without Android Studio — lightweight, isolated, and GPU-accelerated.**

AndroidEMU is a modular Python management framework that automates the full lifecycle of Android Virtual Devices (AVDs): installation, configuration, and execution. It uses only Google's core emulation binaries, skipping the 10–15 GB overhead of a full Android Studio installation.

---

## Why AndroidEMU?

Most Android emulation setups demand Android Studio — a heavy IDE that writes configuration files across your OS user profile and pulls in gigabytes of tooling you never use. AndroidEMU cuts straight to the binaries that matter, runs everything in a local sandbox, and hands you a running virtual device with a single command.

---

## Key Features

| Feature | What it does |
|---|---|
| **Standalone Deployment** | Uses only Google's core emulation binaries — no Android Studio required, saves 10–15 GB of storage |
| **Automated Environment Isolation** | Keeps all logs, `.ini` hardware templates, and virtual storage inside a local runtime sandbox — your OS user profile stays clean |
| **Dynamic Storage Allocator** | Programmatically creates and mounts expandable `userdata.img` virtual partition blocks when developer files are missing |
| **Hardware Acceleration Routing** | Injects environment variables that route the graphics pipeline directly to your GPU via DirectX 11 |
| **Deep Dependency Resolver** | Recursively scans for and loads missing native rendering libraries (`glib-2-vs11.dll`, `libGLESv2.dll`, etc.) into active shell memory at runtime |

---

## Tech Stack

- **Language:** Python 3.10+
- **Target OS:** Windows 10 / Windows 11 (64-bit)
- **Core Binaries:** Google Android Emulator Tools

No external `pip` packages required — built entirely on Python's standard library.

---

## Repository Structure

> ⚠️ You must clone or download the **entire repository**. The `toolkit/` directory is a mandatory dependency — the core script will not run without it.

```
AndroidEMU/
├── app.py                  # Core terminal interface and execution controller
├── .gitignore              # Prevents tracking of multi-gigabyte OS zips
└── toolkit/                # Internal automation helper libraries (REQUIRED)
    ├── ConsoleUtil.py      # Colorized terminal output wrapper
    ├── FileUtil.py         # Workspace validation and file checks
    └── ZipUtil.py          # Fast archive extraction pipeline
```

---

## Requirements

### Python

- **Version:** Python 3.10 or higher
- **Dependencies:** None — uses only standard library modules: `os`, `sys`, `subprocess`, `zipfile`, `shutil`, `pathlib`

### System

- **OS:** Windows 10 or Windows 11 (64-bit)
- **Hypervisor:** Virtual Machine Platform and Hyper-V must be enabled in *Windows Features*
- **GPU:** Any dedicated or integrated GPU with DirectX 11 support or higher

---

## Installation & Usage

**1. Clone the repository**

```powershell
git clone https://github.com/your-username/AndroidEMU.git
cd AndroidEMU
```

Or download the ZIP and extract it — just make sure the full folder structure is intact.

**2. Run the manager**

```powershell
python app.py
```

That's it. The framework handles everything from there.

---

## How It Works

AndroidEMU runs through a fully automated deployment pipeline on each launch:

1. **Engine Verification** — Scans your project root for the emulation runtime. If missing, pulls down official core assets automatically.
2. **Interactive Image Selection** — Prompts you to choose a target Android version: Android 10, 11, or 12.
3. **Configuration & Boot** — Downloads the matching system image, normalizes path separators in hardware profiles, registers the AVD configuration, maps execution environment variables, and launches the virtual device.

No manual SDK setup. No IDE. Just a running Android device.

---

## License

This project is open-source under the [MIT License](LICENSE).
