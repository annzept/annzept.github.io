import glob
import re
import sys
from collections import defaultdict

query = sys.argv[1] if len(sys.argv) > 1 else ""
files = glob.glob(f"_posts/{query}*.md")

categories = defaultdict(lambda: defaultdict(float))

for file in files:
    with open(file, "r") as f:
        print(file)
        for line in f:
            category = re.findall(r"\[(\w*)\]", line)
            if len(category) == 0:
                continue
            print(line.strip())
            for match in re.findall(r"\w+\s*\d+[\.\-]?\d*\s*hour", line):
                print('\t' + match)
                what_did, how_long, _ = match.split(" ")
                if "-" in how_long:
                    init, end = re.findall(r"(\d+)\-(\d+)", how_long)[0]
                    how_long = float(init) + float(end)
                categories[category[0].lower()][what_did] += float(how_long)
days = len(files)
total_hours = 0
print(f"[Summary]: {days} days")
for cat, dids in categories.items():
    hours = sum([x for x in dids.values()])
    total_hours += hours
    print(f"[{cat}]: {hours} (avg: {hours/days:.2f})")
    detail = ", ".join([f"{k} {v}" for k, v in sorted(dids.items(), key=lambda x:x[1], reverse=True)])
    print(f"\t{detail}")
print(f"total: {total_hours} (avg: {total_hours/days:.2f})")