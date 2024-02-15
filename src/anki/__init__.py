from anki.const import NOTES_DIR
from anki.search import walk_files


def ink2anki():
    walk_files(NOTES_DIR)
