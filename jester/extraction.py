from pathlib import Path
import json
from collections import defaultdict


FILES_TO_IGNORE = {
    'context.json',
    'layout.json',
}

DIRECTORIES_TO_IGNORE = {
    'bin',
}


def extract(filepath):
    filepath = Path(filepath).resolve()
    data = defaultdict(dict)

    for p in filepath.glob("*/*.json"):
        filename = p.name
        dirname = p.parts[-2]

        if (dirname in DIRECTORIES_TO_IGNORE) or (filename in FILES_TO_IGNORE):
            continue

        data[dirname][p.stem] = json.load(open(p))

    return data
