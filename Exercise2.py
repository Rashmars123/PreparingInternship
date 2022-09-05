
def main():
    """Assert the is_canada variable using the assert statement.\n
        Expected Action: Raising AssertionError
    """

    countries = ['POL', 'ENG', 'GER', 'USA', 'ITA']
    is_canada = 'CAN' in countries

    assert is_canada


if __name__ == "__main__":
    main()