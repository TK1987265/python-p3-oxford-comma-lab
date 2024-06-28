def oxford_comma(items):
    if len(items) == 0:
        return ""
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return " and ".join(items)
    else:
        # Join all but the last item with commas, then add ", and " before the last item
        return ", ".join(items[:-1]) + ", and " + items[-1]

# Example usage:
if __name__ == "__main__":
    print(oxford_comma(["fiddleheads", "okra", "kohlrabi"]))
    print(oxford_comma(["apple", "orange"]))
    print(oxford_comma(["banana"]))
    print(oxford_comma([]))





def test_oxford_comma_multiple():
    assert oxford_comma(["fiddleheads", "okra", "kohlrabi"]) == "fiddleheads, okra, and kohlrabi"

def test_oxford_comma_two():
    assert oxford_comma(["apple", "orange"]) == "apple and orange"

def test_oxford_comma_one():
    assert oxford_comma(["banana"]) == "banana"

def test_oxford_comma_none():
    assert oxford_comma([]) == ""

