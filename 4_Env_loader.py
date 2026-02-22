import os

APP_NAME = os.getenv("APP_NAME", "My Application")
VERSION = os.getenv("VERSION", "1.0.0")
DEBUG = os.getenv("DEBUG", "False")

DEBUG = DEBUG.lower() == "true"

def print_config():
    print("=" * 40)
    print("SYSTEM CONFIGURATION")
    print("=" * 40)
    print(f"App name: {APP_NAME}")
    print(f"Version: {VERSION}")
    print(f"Debug Mode: {DEBUG}")
    print("=" * 40)

def main():
    print_config()

if __name__ == "__main__":
    main()