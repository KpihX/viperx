from core_lib import hello

from core_lib import SETTINGS


def main():
    hello()
    
    print(f"Project config loaded: {SETTINGS['project_name']}")
    

if __name__ == "__main__":
    main()