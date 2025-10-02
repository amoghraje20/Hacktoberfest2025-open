def remove_duplicates(lst):
    """Remove duplicates while keeping original order."""
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

# Example
nums = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(nums))  # [1, 2, 3, 4, 5]
