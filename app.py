import os
import subprocess
from toolkit import FileUtil
from toolkit import ZipUtil
from toolkit import ConsoleUtil

def exists(path):
    return os.path.exists(path)

# Variable Setup
androidkit = "emulator"
dlemulator = "https://dl.google.com/android/repository/emulator-windows-6885378.zip"

if exists(androidkit):
    print()
else:
    os.system(f"curl -L -o Emu.zip {dlemulator}")
    ZipUtil.unzip("Emu.zip")
    ConsoleUtil.slow_print("Installed Emulator!")

ANDROID_VERSIONS = {
    "1": {
        "name": "Android 7.0 (API 24) - Nougat",
        "url": "https://dl.google.com/android/repository/sys-img/android/x86_64-24_r08.zip",
        "folder": "android-24"
    },
    "2": {
        "name": "Android 8.0 (API 26) - Oreo",
        "url": "https://dl.google.com/android/repository/sys-img/android/x86_64-26_r01.zip",
        "folder": "android-26"
    },
    "3": {
        "name": "Android 9.0 (API 28) - Pie",
        "url": "https://dl.google.com/android/repository/sys-img/android/x86_64-28_r04.zip",
        "folder": "android-28"
    },
    "4": {
        "name": "Android 10 (API 29) - Q",
        "url": "https://dl.google.com/android/repository/sys-img/android/x86_64-29_r07.zip",
        "folder": "android-29"
    },
    "5": {
        "name": "Android 11 (API 30) - R",
        "url": "https://dl.google.com/android/repository/sys-img/google_apis/x86_64-30_r11.zip",
        "folder": "android-30"
    },
    "6": {
        "name": "Android 12 (API 31) - S",
        "url": "https://dl.google.com/android/repository/sys-img/android/x86_64-31_r03.zip",
        "folder": "android-31"
    }
}

ConsoleUtil.clear

ConsoleUtil.slow_print("\n==================================")
ConsoleUtil.slow_print("Welcome To My Android Emulator!")
ConsoleUtil.slow_print("==================================")
ConsoleUtil.green_print("Available Android Versions:")
for key, value in ANDROID_VERSIONS.items():
    ConsoleUtil.cyan_print(f"[{key}] {value['name']}")

# 1. Handle Selection Logic
choice = input("\nSelect Android Version (1-3): ").strip()
if choice not in ANDROID_VERSIONS:
    ConsoleUtil.red_print("Invalid choice! Defaulting to Android 10.")
    choice = "1"

selected = ANDROID_VERSIONS[choice]
sys_img_zip = f"{selected['folder']}.zip"
sys_img_dir = os.path.abspath(selected['folder'])

# 2. Automatically Download and Unzip the System Images
if exists(sys_img_dir):
    ConsoleUtil.green_print(f"\n{selected['name']} is already downloaded!")
else:
    ConsoleUtil.cyan_print(f"\nDownloading {selected['name']}... This may take a few minutes.")
    os.system(f"curl -L -o {sys_img_zip} {selected['url']}")
    ConsoleUtil.cyan_print("Extracting system files...")
    ZipUtil.unzip(sys_img_zip, sys_img_dir)
    ConsoleUtil.cyan_print("Extraction complete!")

# 3. Dynamic Auto-Path Resolution Engine
# Google images unpack into a sub-folder tree like: /x86_64/ or /android-<api>/x86_64/
# This loop scans the extracted path to find where the files actually landed.
target_root = sys_img_dir
for root, dirs, files in os.walk(sys_img_dir):
    if "system.img" in files:
        target_root = root
        break

# Map out configuration paths automatically using the discovered location
system = os.path.join(target_root, "system.img")
boot = os.path.join(target_root, "boot.img")
vendor = os.path.join(target_root, "vendor.img")
ramdisk = os.path.join(target_root, "ramdisk.img")
kernel = os.path.join(target_root, "kernel-ranchu")

# Note: Keymaps ship built-in with the primary engine download zip file
keymaps = os.path.join(os.path.abspath(androidkit), "emulator", "qt", "sys", "keymaps")
if not os.path.exists(keymaps):
    keymaps = os.path.join(os.path.abspath(androidkit), "qt", "sys", "keymaps")

# Quick Safety Validation Check
if not os.path.exists(system):
    ConsoleUtil.red_print(f"Error: Could not locate critical image structure inside {sys_img_dir}")
    exit(1)

# --- Runtime Execution Setup ---

# Inject System Environmental Context Variables
os.environ["ANDROID_EMULATOR_HOME"] = os.path.abspath("emu_home")
os.environ["ANDROID_SDK_ROOT"] = os.path.abspath(androidkit)
os.environ["QT_QTPA_PLATFORM"] = "windows"

# Generate local instance workspace storage
workspace_dir = os.path.abspath("emu_home")
if not os.path.exists(workspace_dir):
    os.makedirs(workspace_dir)

# Target the master desktop execution wrapper framework
# 1. Try the "emulator/emulator.exe" relative path, then get its absolute path
emulator_exe = os.path.abspath(os.path.join("emulator", "emulator.exe"))

# 2. If that doesn't exist, fallback to just "emulator.exe" in the current directory
if not os.path.exists(emulator_exe):
    emulator_exe = os.path.abspath("emulator.exe")

# --- Dynamic AVD Registration Engine ---
avd_name = f"MyCustomAVD_{choice}"

# Force the profile files into your project's local directory override
avd_root_dir = os.path.abspath(os.path.join("emu_home", "avd"))

# Create the local avd folder structure if missing
if not os.path.exists(avd_root_dir):
    os.makedirs(avd_root_dir)

# 1. Generate the master .ini pointer file inside your local folder override
ini_file_path = os.path.join(avd_root_dir, f"{avd_name}.ini")
actual_avd_path = os.path.join(avd_root_dir, f"{avd_name}.avd").replace("\\", "/")
ini_content = f"""avd.ini.encoding=UTF-8
path={actual_avd_path}
"""

with open(ini_file_path, "w", encoding="utf-8") as f:
    f.write(ini_content)

# 2. Generate the inner hardware config directory and config.ini file
actual_avd_dir = os.path.join(avd_root_dir, f"{avd_name}.avd")
if not os.path.exists(actual_avd_dir):
    os.makedirs(actual_avd_dir)

config_file_path = os.path.join(actual_avd_dir, "config.ini")
config_content = f"""avd.ini.encoding=UTF-8
hw.cpu.arch=x86_64
hw.ramSize=2048
image.sysdir.1={target_root.replace("\\", "/")}
tag.id=default
tag.display=Default
skin.dynamic=yes
showDeviceFrame=yes
"""

with open(config_file_path, "w", encoding="utf-8") as f:
    f.write(config_content)

ConsoleUtil.green_print(f"Registered Virtual Device profile locally: {avd_name}")


# --- SDK Validation Environment Fixes (CRITICAL STRUCTURAL FIXES) ---

# CRITICAL FIX 1: emulator.exe demands an empty 'platform-tools' folder next to the 'emulator' directory!
platform_tools_dir = os.path.abspath("platform-tools")
if not os.path.exists(platform_tools_dir):
    os.makedirs(platform_tools_dir)

# CRITICAL FIX 2: emulator.exe demands an empty 'platforms' folder next to it!
platforms_dir = os.path.abspath("platforms")
if not os.path.exists(platforms_dir):
    os.makedirs(platforms_dir)

# Map out environment context relative to your actual 'Android EMU' layout
os.environ["ANDROID_SDK_ROOT"] = os.path.abspath(".")
os.environ["ANDROID_HOME"] = os.path.abspath(".")
os.environ["ANDROID_EMULATOR_HOME"] = os.path.abspath("emu_home")
os.environ["ANDROID_AVD_HOME"] = os.path.abspath(os.path.join("emu_home", "avd"))
os.environ["QT_QTPA_PLATFORM"] = "windows"

# Target the master desktop execution framework directly inside its folder
emulator_exe = os.path.abspath(os.path.join("emulator", "emulator.exe"))


# --- Inject Core DLL Paths directly into Windows Environment Memory ---
emulator_root = os.path.abspath("emulator")
all_dll_paths = []

for root, dirs, files in os.walk(emulator_root):
    if any(file.lower().endswith('.dll') for file in files):
        all_dll_paths.append(root)

os.environ["PATH"] = ";".join(all_dll_paths) + ";" + os.environ.get("PATH", "")


# --- Userdata Workspace Engine ---
workspace_dir = os.path.abspath("emu_home")
if not os.path.exists(workspace_dir):
    os.makedirs(workspace_dir)

userdata_img_path = os.path.join(workspace_dir, "userdata.img")

# Programmatically generate a blank, expandable 2GB disk image if it's missing
if not os.path.exists(userdata_img_path):
    ConsoleUtil.blue_print("Generating fresh user storage space (userdata.img)...")
    qemu_img_exe = os.path.abspath(os.path.join("emulator", "qemu-img.exe"))
    
    if not os.path.exists(qemu_img_exe):
        qemu_img_exe = os.path.abspath(os.path.join("emulator", "qemu", "windows-x86_64", "qemu-img.exe"))
        
    try:
        subprocess.run([qemu_img_exe, "create", "-f", "raw", userdata_img_path, "2G"], check=True, stdout=subprocess.DEVNULL)
        ConsoleUtil.green_print("Successfully created userdata.img allocation!")
    except Exception as create_err:
        ConsoleUtil.red_print(f"Warning: Automatic disk generation failed ({create_err}).")


# --- Build Standard Native Google Android Hardware Instruction Arguments ---
launch_args = [
    emulator_exe,
    "-avd", avd_name,                  
    "-sysdir", target_root,
    "-system", system,
    "-vendor", vendor,
    "-ramdisk", ramdisk,
    "-kernel", kernel,
    "-data", userdata_img_path,        
    "-memory", "2048",                                    
    "-no-snapshot-load",
    
    # PRODUCTION RESIZING AND DISPLAY FIXES:
    "-gpu", "angle_indirect",          # Uses Windows DirectX 11 for hardware-stable scaling
    "-scale", "0.50",                  # Safely launches at 50% scale to fit your monitor layout
    "-feature", "AllowDynamicSkinScaling" # Native Google flag to unlock mouse edge dragging
]

ConsoleUtil.green_print("\n--- Launching Android Virtual Device via Master Engine ---")
try:
    # Running via native ANGLE DirectX clears the UpdateLayeredWindowIndirect rendering loop glitch
    process = subprocess.Popen(launch_args, stdout=None, stderr=None, text=True)
    ConsoleUtil.green_print("Master emulation pipeline initialized.")
    ConsoleUtil.green_print("Checking engine process stability (5 seconds)...")
    
    return_code = process.wait(timeout=5)
    ConsoleUtil.red_print(f"\n[CRASH DETECTED] Engine exited early with exit code: {return_code}")
    ConsoleUtil.red_print("If a Vulkan or driver error occurs, verify your Windows DirectX installations.")

except subprocess.TimeoutExpired:
    ConsoleUtil.green_print("\n[SUCCESS] Android core is running stably in the background!")
    ConsoleUtil.green_print("The graphical window is now active.")
    ConsoleUtil.green_print("-> You can now hover your mouse over the corners to click and stretch the window!")
except Exception as e:
    ConsoleUtil.red_print(f"Failed to execute the boot binary. Error: {e}")
