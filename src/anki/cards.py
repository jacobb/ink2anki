import re

import httpx

from anki.const import ANKI_URL, DECK_NAME
from anki.md import md_to_html  # noqa: E999
from anki.models import Card


def create_card(front, back):
    card_data = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": "Jacob's",
                "modelName": "Basic",
                "fields": {"Front": front, "Back": back},
                "tags": [],
            }
        },
    }
    resp = httpx.post(ANKI_URL, json=card_data)
    return resp.json()


def anki_request(action, **params):
    card_data = {
        "action": action,
        "params": params,
        "version": 6,
    }
    resp = httpx.post(ANKI_URL, json=card_data)
    return resp.json()


def make_card_request(front, back):
    card_data = {
        "note": {
            "deckName": DECK_NAME,
            "modelName": "Basic",
            "fields": {"Front": md_to_html(front), "Back": md_to_html(back)},
            "tags": [],
        },
    }
    return anki_request("addNote", **card_data)


def get_or_create_card_from_match(match: re.Match) -> Card:
    card = Card(
        front=match.group(1),
        back=match.group(2),
        anki_id=match.group(3),
        end=match.end(),
    )
    if card.exists():
        return card

    card.in_markdown = False
    resp = make_card_request(card.front, card.back)
    if resp["error"]:
        raise ValueError(f"Something Broke {resp}")
    card.anki_id = resp["result"]
    return card


def insert_card_into_md(markdown, card, offset=0):
    insert_position = card.end + offset
    # Modify the full_markdown string to insert the new text
    markdown = (
        markdown[:insert_position]
        + "\n"
        + card.get_id_tag()
        + markdown[insert_position:]
    )
    offset += card.get_offset_length()
    return markdown, offset
