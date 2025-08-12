
# color_mapping.py
MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

def color_pair_to_string(major, minor):
    return f'{major} {minor}'

def get_color_from_pair_number(pair_number):
    zero_based_pair_number = pair_number - 1
    major_index = zero_based_pair_number // len(MINOR_COLORS)
    minor_index = zero_based_pair_number % len(MINOR_COLORS)
    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]

def get_pair_number_from_color(major, minor):
    return MAJOR_COLORS.index(major) * len(MINOR_COLORS) + MINOR_COLORS.index(minor) + 1

def print_manual():
    for pair_number in range(1, len(MAJOR_COLORS) * len(MINOR_COLORS) + 1):
        major, minor = get_color_from_pair_number(pair_number)
        print(f"Pair {pair_number:2d}: {color_pair_to_string(major, minor)}")

# Test Functions
def test():
    assert get_color_from_pair_number(4) == ('White', 'Brown')
    assert get_pair_number_from_color('Black', 'Orange') == 12
    print("Tests passed!")

# Entry point
if __name__ == "__main__":
    test()
    print_manual()
