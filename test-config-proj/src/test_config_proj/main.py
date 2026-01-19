from test_config_proj import hello

from test_config_proj import SETTINGS


def main():
    hello()
    
    print(f"Project config loaded: {SETTINGS['project_name']}")
    

if __name__ == "__main__":
    main()