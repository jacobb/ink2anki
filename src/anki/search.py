import re
from pathlib import Path
from typing import Union

from anki.cards import get_or_create_card_from_match, insert_card_into_md


def parse_file(file_path: Union[str, Path]):
    p = Path(file_path).absolute()
    with p.open() as f:
        full_markdown = f.read()

    pattern = r"^Q: (.+?)\nA: (.+?)(?:\n<!--ID: (\d+)-->)?(?=(\n\n|$))"
    matches = re.finditer(pattern, full_markdown, re.MULTILINE | re.DOTALL)
    offset = 0
    for match in matches:
        card = get_or_create_card_from_match(match)
        if not card.in_markdown:
            print(f"Card for {card} not in markdown, inserting")
            full_markdown, offset = insert_card_into_md(full_markdown, card, offset)
        else:
            print(f"Card for {card} already exists, skipping")

    if offset > 0:
        with p.open("w") as f:
            f.write(full_markdown)

def walk_files(notes_dir):
    notes_path = Path(notes_dir).absolute()
    for root, _, files in notes_path.walk():
        for file in files:
            parse_file(root / file)
