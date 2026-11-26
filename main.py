import os

ENTRY = "Error 0xJAM: I printed 41,208 pages perfectly. One crooked sheet, one thump, and the jam is now logged under your name."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
