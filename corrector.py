def convert_data(text):
    if text == "":
        return text
    elif "k" in text:
        return text.split("k", 1)[0].replace(".", "") + "00"
    elif "M" in text:
        return text.split("M", 1)[0].replace(".", "") + "00000"
    elif "B" in text:
        return text.split("B", 1)[0].replace(".", "") + "00000000"
    elif "T" in text:
        return text.split("T", 1)[0].replace(".", "") + "00000000000"
    elif "P" in text:
        return text.split("P", 1)[0].replace(".", "") + "00000000000000"
    else:
        return text.split(" ", 1)[0]


def convert_funds(text):
    if text == "":
        return text
    elif "k" in text:
        return text[4:].split("k", 1)[0].replace(".", "") + "00"
    elif "M" in text:
        return text[4:].split("M", 1)[0].replace(".", "") + "00000"
    elif "B" in text:
        return text[4:].split("B", 1)[0].replace(".", "") + "00000000"
    elif "T" in text[4:]:
        return text[4:].split("T", 1)[0].replace(".", "") + "00000000000"
    elif "P" in text:
        return text[4:].split("P", 1)[0].replace(".", "") + "00000000000000"
    else:
        return text[4:]


def convert_nums(text):
    text = text.split("\n", 1)[0]  # cuts off updates
    if "k" in text:
        return text.split("k", 1)[0].replace(".", "") + "00"
    elif "M" in text:
        return text.split("M", 1)[0].replace(".", "") + "00000"
    elif "B" in text:
        return text.split("B", 1)[0].replace(".", "") + "00000000"
    elif "T" in text:
        return text.split("T", 1)[0].replace(".", "") + "00000000000"
    elif "P" in text:
        return text.split("P", 1)[0].replace(".", "") + "00000000000000"
    else:
        return text
