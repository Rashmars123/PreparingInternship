
def main():
    """
    Modify the implementation of the max_min_diff() function. By using the assert statement inside this function,
    add the ability to check the length of the numbers' argument before returning the result. If the length of the
    numbers object is 0 raise the AssertionError without any message. Otherwise, return the correct result.\n
    In response call max_min_diff() function passing an empty list.

    :return: none
    """
    def max_min_diff(numbers):
        assert len(numbers) != 0
        return max(numbers) - min(numbers)

    max_min_diff([])


if __name__ == "__main__":
    main()