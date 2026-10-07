"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # Create a copy of the original list.
    result = lst.copy()

    # Each pass moves the largest remaining value toward the end.
    for i in range(len(result) - 1):

        # Track whether any swaps occurred during this pass.
        swapped = False

        # Compare adjacent elements.
        for j in range(len(result) - 1 - i):

            # Swap elements when they are out of order.
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True

        # Continue until the list is sorted.
        # This improves performance for data that is already sorted.
        if not swapped:
            break

    return result


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # A list with zero or one element is already sorted.
    if len(lst) <= 1:
        return lst.copy()

    # Divide the list into smaller halves.
    middle = len(lst) // 2
    left = lst[:middle]
    right = lst[middle:]

    # Sort each half recursively.
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # Merge the sorted halves together.
    # Return the sorted list.
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    result = []
    left_index = 0
    right_index = 0

    # Compare values from the left and right lists.
    while left_index < len(left) and right_index < len(right):

        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Append any remaining values.
    result.extend(left[left_index:])

    # Append any remaining values.
    result.extend(right[right_index:])

    # Return the merged sorted list.
    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    print("TODO: Create an unsorted dataset and test both sorting algorithms.")
    # Dataset #1 is popularity ratings for tv shows.
    dataset1 = [77, 91, 84, 76, 93, 55, 34, 80]

    print("Original dataset:", dataset1)

    bubble_result1 = bubble_sort(dataset1)
    merge_result1 = merge_sort(dataset1)

    print("Bubble Sort:", bubble_result1)
    print("Merge Sort:", merge_result1)

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    print("TODO: Create a second dataset and compare sorting results.")
    # Dataset #2 is another group of tv show ratings.
    # This dataset includes duplicate values to demonstrate
    # how sorting algorithms handle repeated ratings.
    dataset2 = [45, 82, 82, 61, 99, 73, 58, 73]

    print("Original dataset:", dataset2)

    bubble_result2 = bubble_sort(dataset2)
    merge_result2 = merge_sort(dataset2)

    print("Bubble Sort:", bubble_result2)
    print("Merge Sort:", merge_result2)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")
    # Edge Case 1: Empty list.
    # Both algorithms should return an empty list without errors.
    empty_list = []

    print("Empty list:")
    print("Bubble Sort:", bubble_sort(empty_list))
    print("Merge Sort:", merge_sort(empty_list))

    # Edge Case 2: Already sorted list.
    # Bubble Sort can stop early because no swaps are needed.
    # Merge Sort still divides and merges the list.
    sorted_list = [10, 20, 30, 40, 50]

    print("\nAlready sorted list:")
    print("Bubble Sort:", bubble_sort(sorted_list))
    print("Merge Sort:", merge_sort(sorted_list))

if __name__ == "__main__":
    main()