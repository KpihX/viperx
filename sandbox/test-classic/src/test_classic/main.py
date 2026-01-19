from test_classic import hello

from test_classic import SETTINGS


def main():
    hello()
    
    print(f"Project config loaded: {SETTINGS['project_name']}")
    

if __name__ == "__main__":
    main()