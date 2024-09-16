import re
def normalize_name(name: str) -> str:
    # Use a regular expression to remove unwanted characters
    return re.sub(r'[ \-\'.’%:]', '', name.lower())