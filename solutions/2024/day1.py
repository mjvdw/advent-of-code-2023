from aocd import get_data

data = get_data(year=2024, day=1)


def part_a(data):
    # your code here..
    return 1


def part_b(data):
    # more code here..
    return 2


test_data = """\
some example test data
"""


if __name__ == "__main__":
    assert part_a(test_data) == "expected test result a"
    assert part_b(test_data) == "expected test result b"
    print(part_a(data))
    print(part_b(data))
