import sys

def main():
    if len(sys.argv) > 1:
        argument = sys.argv[1]
        print(f"Argument received: {argument}")
        sys.exit(0)
    else:
        print("No argument provided.")
        sys.exit(1)

if __name__ == "__main__":
    main()
