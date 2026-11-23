import os

LINE = "My useless superpower: I can unfreeze my phone by glare alone — the battery just tenses up."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
