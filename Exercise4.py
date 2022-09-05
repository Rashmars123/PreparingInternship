def main():
    """Using the assert keyword with a message is an AssertionError is raised"""
    def max_min_diff(numbers):
        assert len(numbers) != 0, 'The numbers object cannot be empty. '
        return max(numbers) - min(numbers)

    max_min_diff([])


if __name__ == "__main__":
    main()
