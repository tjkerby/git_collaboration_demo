"""Small statistical helpers used in the pull request demonstrations."""

def data_range(values):
    return max(values) - min(values)

def average_or_none(values):
    return sum(values) / len(values)