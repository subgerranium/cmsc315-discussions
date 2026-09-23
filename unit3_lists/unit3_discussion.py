"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Insert the value at the specified index. Any existing elements at or after this index are
    # shifted one position to the right. The time required depends on where the insertion happens:
    # If it's at the end: O(1) amortized, since no elements need to be shifted.
    # If it's at the beginning or in the middle: O(n), since the following elements must be shifted.
    lst.insert(index, value)
    return lst


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Check that the index is valid before trying to remove anything. This helps keep an invalid
    # index from causing an IndexError and stopping the program. If the index doesn't exist, return
    # None instead of trying.
    if index < 0 or index >= len(lst):
        return None

    # Remove and return the item at the given index.
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # A linear search checks each item in the list from left to right. We have to check the items
    # one by one because a Python list doesn't use a hash table or sorted order to find values
    # instantly. In the worst case scenario, we need to check every item, which takes O(n) time.
    try:
        return lst.index(value)
    except ValueError:
        return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")

    # Create a list containing several values.
    playlist = ["Twinkle,Twinkle", "ABC", "Wheels on the Bus"]

    # Display the original list.
    print(f"Original Playlist: {playlist}")

    # Test insertion at - beginning, middle, end.
    # Beginning (index 0) - shifts all existing elements right (O(n)).
    insert_at(playlist, 0, "Intro")
    print(f"After insertion (beginning): {playlist}")

    # Middle (index 2) - shifts elements from index 2 right (O(n)).
    insert_at(playlist, 2, "Interlude")
    print(f"After insertion (middle): {playlist}")

    # End (append/end index) - O(1) amortized, no shifting needed.
    insert_at(playlist, len(playlist), "Outro")
    print(f"After insertion (end): {playlist}")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")

    # Delete an item from beginning, middle, and end.
    removed_beg = delete_at(playlist, 0)
    print(f"Removed from beginning: '{removed_beg}' -> Updated list: {playlist}")

    mid_idx = len(playlist) // 2
    removed_mid = delete_at(playlist, mid_idx)
    print(f"Removed from middle (idx {mid_idx}): '{removed_mid}' -> Updated list: {playlist}")

    removed_end = delete_at(playlist, len(playlist) - 1)
    print(f"Removed from end: '{removed_end}' -> Updated list: {playlist}")


    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    # Sample data of inventory list
    inventory = ["shirt", "pants", "shoes"]

    # Search for a value that exists
    target_existing = "pants"
    idx_found = search_value(inventory, target_existing)
    print(f"Search for existing value '{target_existing}': Found at index {idx_found}")

    # Search for a value that does not exist
    target_missing = "belt"
    idx_missing = search_value(inventory, target_missing)
    print(f"Search for missing value '{target_missing}': Result {idx_missing}")


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")

    # Edge Case 1: Delete using an invalid index
    invalid_del = delete_at(inventory, 99)
    print(f"Delete index (99): returned {invalid_del} ")

    # Edge Case 2: Delete from an empty list
    empty_list = []
    del_empty = delete_at(empty_list, 0)
    search_empty = search_value(empty_list, "test")
    print(f"Delete from empty list: returned {del_empty}")
    print(f"Search in empty list: returned {search_empty}")


if __name__ == "__main__":
    main()