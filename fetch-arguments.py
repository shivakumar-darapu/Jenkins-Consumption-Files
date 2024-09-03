import sys

def main():
    if len(sys.argv) > 1:
        argument = sys.argv[1]
        print(f"Argument received: {argument}")
    else:
        print("No argument provided.")

if __name__ == "__main__":
    main()
