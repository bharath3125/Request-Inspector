def check_signature(text):
    text = text.lower()

    rules = ["select", "union", "drop", "<script>", "or 1=1", "--"]

    for r in rules:
        if r in text:
            return "malicious", 0.9

    return "clean", 0.1
