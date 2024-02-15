import markdown


def md_to_html(md):
    return markdown.markdown(
        md,
        extensions=["fenced_code", "sane_lists", "nl2br", "md_in_html", "codehilite"],
    )
