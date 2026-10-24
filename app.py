import argparse
from colorama import Fore, init

def main():
    init(autoreset=True)
    p = argparse.ArgumentParser(description="Tiny greeter used to test README verification.")
    p.add_argument("--name", required=True, help="Who to greet")
    p.add_argument("--times", type=int, default=1, help="How many times to greet")
    a = p.parse_args()
    for _ in range(a.times):
        print(Fore.GREEN + f"Hello, {a.name}!")

if __name__ == "__main__":
    main()
