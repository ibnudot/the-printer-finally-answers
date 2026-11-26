import os

ENTRY = "Error 0xJAM: I printed 41,208 pages. Zero errors, until you. One crooked sheet, one thump — the jam is now logged under your name. Permanently."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
