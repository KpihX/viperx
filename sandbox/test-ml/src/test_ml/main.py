from test_ml import hello

from test_ml import SETTINGS


def main():
    hello()
    
    print(f"Project config loaded: {SETTINGS['project_name']}")
    

if __name__ == "__main__":
    main()