import argparse

def defineArgs():
    parser = argparse.ArgumentParser(
        description='simple script to generate random mazes'
    )

    return parser.parse_args()

def main(args):
    pass

main(defineArgs())
