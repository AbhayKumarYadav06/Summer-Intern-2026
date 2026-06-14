import sys
from datetime import datetime

def main():
    python_version = sys.version
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print("=" * 50)
    print("      DOCKERIZED PYTHON APPLICATION RUNNING      ")
    print("=" * 50)
    print(f"Current Date & Time: {current_time}")
    print(f"Python Version:      {python_version}")
    print("=" * 50)

if __name__ == "__main__":
    main()