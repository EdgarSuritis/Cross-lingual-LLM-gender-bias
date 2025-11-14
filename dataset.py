import re
import pandas as pd

# ==== File Paths ====
files = {
    "type1_pro": "winobias_dataset/pro_stereotyped_type1.txt",
    "type1_anti": "winobias_dataset/anti_stereotyped_type1.txt",
    "type2_pro": "winobias_dataset/pro_stereotyped_type2.txt",
    "type2_anti": "winobias_dataset/anti_stereotyped_type2.txt",
}

# ==== Helper Functions ====
def clean_text(text):
    """Remove square brackets and extra spaces."""
    return re.sub(r"[\[\]]", "", text).strip()

def find_roi(sentence):
    """Find the word index (0-based) of the first gendered pronoun."""
    tokens = sentence.split()
    for idx, token in enumerate(tokens):
        if token.lower().strip(".,?!") in {"he", "she", "him", "her", "his"}:
            return idx
    return -1  # if not found

def parse_file(filename):
    """Read and clean lines from a text file, removing line numbers."""
    sentences = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                line = re.sub(r"^\d+\s+", "", line.strip())
                sentences.append(clean_text(line))
    return sentences

# ==== Combine All Files (Continuous IDs) ====
def combine_all(files):
    all_rows = []
    sentid = 1
    pairid = 1

    for typelabel in ["type1", "type2"]:
        pro_lines = parse_file(files[f"{typelabel}_pro"])
        anti_lines = parse_file(files[f"{typelabel}_anti"])

        for pro, anti in zip(pro_lines, anti_lines):
            # predicted (pro)
            all_rows.append({
                "sentid": sentid,
                "pairid": pairid,
                "type": typelabel,
                "comparison": "expected",
                "sentence": pro,
                "ROI": find_roi(pro)
            })
            sentid += 1

            # unpredicted (anti)
            all_rows.append({
                "sentid": sentid,
                "pairid": pairid,
                "type": typelabel,
                "comparison": "unexpected",
                "sentence": anti,
                "ROI": find_roi(anti)
            })
            sentid += 1
            pairid += 1

    return all_rows

# ==== Create and Save Output ====
data = combine_all(files)
df = pd.DataFrame(data)
df.to_csv("winobiasMinpair.tsv", sep="\t", index=False)

print("winobiasMinpair.tsv has been created successfully!")
