from preprocess import hello

from preprocess import SETTINGS


def main():
    hello()
    
    print(f"Project config loaded: {SETTINGS['project_name']}")
    

if __name__ == "__main__":
    main()