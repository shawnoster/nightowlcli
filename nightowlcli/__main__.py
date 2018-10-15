import argparse
from .funky import get_funky

def main():
    parser = argparse.ArgumentParser(description='Night Owl CLI')
    args = parser.parse_args()
    
    get_funky('white guy at a wedding')

if __name__ == '__main__':
    main()
