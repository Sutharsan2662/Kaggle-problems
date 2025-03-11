def flames(name_1, name_2):
    name_1 = name_1.lower().replace(" ", "")
    name_2 = name_2.lower().replace(" ", "")

    if not name_1.isalpha() or not name_2.isalpha():
        return "Error: Names must be alphabetic."
    if not name_1 or not name_2:
        return "Error: Names cannot be empty."

    # Convert the names to lists
    name_1 = list(name_1)
    name_2 = list(name_2)

    # Removing identical letters
    i = 0
    while i < len(name_1):
        j = 0
        while j < len(name_2):
            if name_1[i] == name_2[j]:
                name_1.pop(i)
                name_2.pop(j)
                if i > 0:
                    i -= 1
                break
            j += 1
        else:
            i += 1

    # FLAMES game
    count = len(name_1) + len(name_2)
    flames = ["friends", "lover", "Affection", "Marriage", "enemy", "sister"]
    print(count)

    if count == 0:
        return "Error: All characters are the same, FLAMES cannot be performed."
    if count == 1:
        return flames[5]

    current_index = 0
    while len(flames) > 1:
        next_index = (current_index + count - 1) % len(flames)
        flames.pop(next_index)
        current_index = next_index % len(flames)

    return flames[0]

if __name__ == "__main__":
    while True:
        name1 = input("Enter the first name (or 'q' to quit): ")
        if name1.lower() == 'q':
            break
        name2 = input("Enter the second name (or 'q' to quit): ")
        if name2.lower() == 'q':
            break
        result = flames(name1, name2) #consistent function name
        print(result)
        if "Error" not in result:
            print(f"The relationship is: {result}")