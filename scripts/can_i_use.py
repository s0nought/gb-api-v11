import sys

INPUT_FILE = sys.argv[1]
OUTPUT_FILE = sys.argv[2]

import json

with open(INPUT_FILE, mode = "rt", encoding = "UTF-8") as f:
    fc = json.load(f)

# models

models = list(fc.keys())
models.sort()

# endpoints

endpoints = set()

for item in fc.values():
    endpoints.update(item)

endpoints = list(endpoints)
endpoints.sort()

# availability map

availability_map = dict()

for endpoint in endpoints:
    availability = dict()

    for model in models:

        if endpoint in fc[model]:
            x = True
        else:
            x = False

        availability.update({f"{model}": x})

    availability_map.update({f"{endpoint}": availability})

# result (Markdown)

header = f"|API endpoint|{'|'.join(models)}|"

sub_header = f"|:-|{':-:|' * len(models)}"

body = ""

for endpoint, availability in availability_map.items():
    row = f"|{endpoint}|"

    for x in availability.values():
        if x:
            row += r"✔|"
        else:
            row += r"✘|"

    body += row + "\n"

result = f"""{header}
{sub_header}
{body}
"""

with open(OUTPUT_FILE, mode = "wt", encoding = "UTF-8") as f:
    f.write(result)

print("Done.")
