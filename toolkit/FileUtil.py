import os
import json
import shutil
import asyncio
import time
from datetime import datetime

class FileUtils:
    """
    FULL FILE SYSTEM UTILITY FRAMEWORK
    Supports sync + async file operations, JSON, folders, backups, etc.
    """

    # ─────────────────────────────
    # BASIC LOGGING
    # ─────────────────────────────
    @staticmethod
    def log(msg, level="INFO"):
        print(f"[{level}] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {msg}")

    # ─────────────────────────────
    # PATH UTILITIES
    # ─────────────────────────────
    @staticmethod
    def exists(path):
        return os.path.exists(path)

    @staticmethod
    def is_file(path):
        return os.path.isfile(path)

    @staticmethod
    def is_dir(path):
        return os.path.isdir(path)

    @staticmethod
    def join(*parts):
        return os.path.join(*parts)

    # ─────────────────────────────
    # FILE CORE OPS
    # ─────────────────────────────
    @staticmethod
    def read_file(path, encoding="utf-8"):
        try:
            with open(path, "r", encoding=encoding) as f:
                return f.read()
        except Exception as e:
            FileUtils.log(f"Read failed: {e}", "ERROR")
            return None

    @staticmethod
    def write_file(path, content, encoding="utf-8"):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding=encoding) as f:
                f.write(str(content))
            return True
        except Exception as e:
            FileUtils.log(f"Write failed: {e}", "ERROR")
            return False

    @staticmethod
    def append_file(path, content, encoding="utf-8"):
        try:
            with open(path, "a", encoding=encoding) as f:
                f.write(str(content))
            return True
        except Exception as e:
            FileUtils.log(f"Append failed: {e}", "ERROR")
            return False

    @staticmethod
    def create_file(path, content=""):
        if FileUtils.exists(path):
            FileUtils.log("File already exists", "INFO")
            return False
        return FileUtils.write_file(path, content)

    @staticmethod
    def delete_file(path):
        try:
            if FileUtils.exists(path):
                os.remove(path)
                return True
            return False
        except Exception as e:
            FileUtils.log(f"Delete failed: {e}", "ERROR")
            return False

    # ─────────────────────────────
    # FOLDER OPS
    # ─────────────────────────────
    @staticmethod
    def create_folder(path):
        try:
            os.makedirs(path, exist_ok=True)
            return True
        except Exception as e:
            FileUtils.log(f"Folder create failed: {e}", "ERROR")
            return False

    @staticmethod
    def delete_folder(path):
        try:
            shutil.rmtree(path)
            return True
        except Exception as e:
            FileUtils.log(f"Folder delete failed: {e}", "ERROR")
            return False

    @staticmethod
    def list_dir(path):
        try:
            return os.listdir(path)
        except Exception as e:
            FileUtils.log(f"List dir failed: {e}", "ERROR")
            return []

    @staticmethod
    def tree(path, indent=""):
        """Print directory tree"""
        try:
            items = os.listdir(path)
            for item in items:
                full = os.path.join(path, item)
                print(indent + "├── " + item)
                if os.path.isdir(full):
                    FileUtils.tree(full, indent + "│   ")
        except Exception as e:
            FileUtils.log(f"Tree error: {e}", "ERROR")

    # ─────────────────────────────
    # JSON SUPPORT
    # ─────────────────────────────
    @staticmethod
    def read_json(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            FileUtils.log(f"JSON read failed: {e}", "ERROR")
            return None

    @staticmethod
    def write_json(path, data, indent=4):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=indent)
            return True
        except Exception as e:
            FileUtils.log(f"JSON write failed: {e}", "ERROR")
            return False

    # ─────────────────────────────
    # BACKUP SYSTEM
    # ─────────────────────────────
    @staticmethod
    def backup_file(path, backup_dir="backup"):
        try:
            if not FileUtils.exists(path):
                return False
            FileUtils.create_folder(backup_dir)
            name = os.path.basename(path)
            backup_path = os.path.join(backup_dir, f"{name}.bak")
            shutil.copy2(path, backup_path)
            return backup_path
        except Exception as e:
            FileUtils.log(f"Backup failed: {e}", "ERROR")
            return None

    # ─────────────────────────────
    # FILE WATCHER (simple polling)
    # ─────────────────────────────
    @staticmethod
    def watch_file(path, callback, interval=2):
        """
        Watches file changes using polling
        callback(old_content, new_content)
        """
        try:
            last = FileUtils.read_file(path)
            while True:
                time.sleep(interval)
                current = FileUtils.read_file(path)
                if current != last:
                    callback(last, current)
                    last = current
        except Exception as e:
            FileUtils.log(f"Watcher error: {e}", "ERROR")

    # ─────────────────────────────
    # ASYNC VERSION
    # ─────────────────────────────
    @staticmethod
    async def aread_file(path, encoding="utf-8"):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, FileUtils.read_file, path, encoding)

    @staticmethod
    async def awrite_file(path, content, encoding="utf-8"):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, FileUtils.write_file, path, content, encoding)

    # ─────────────────────────────
    # FILE INFO
    # ─────────────────────────────
    @staticmethod
    def info(path):
        try:
            stats = os.stat(path)
            return {
                "size": stats.st_size,
                "modified": datetime.fromtimestamp(stats.st_mtime),
                "created": datetime.fromtimestamp(stats.st_ctime),
                "is_file": os.path.isfile(path),
                "is_dir": os.path.isdir(path),
            }
        except Exception as e:
            FileUtils.log(f"Info failed: {e}", "ERROR")
            return None