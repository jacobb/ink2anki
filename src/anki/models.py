from typing import Optional

from attrs import define


@define
class Card:
    front: str
    back: str
    end: int
    anki_id: Optional[int]
    in_markdown: bool = True

    def exists(self):
        return self.anki_id is not None

    def get_id_tag(self):
        return f"<!--ID: {self.anki_id}-->"

    def get_offset_length(self):
        return len(self.get_id_tag()) + 1

    def __str__(self):
        if self.anki_id:
            return self.anki_id
        print(self.front[:32])
