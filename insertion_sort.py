def insertion_sort(arr):
    """
    Sorts an array in ascending order using the Insertion Sort algorithm.
    """
    # Traverse from 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


# Test the implementation
if __name__ == "__main__":
    sample_list = [12, 11, 13, 5, 6]
    print("Original list:", sample_list)
    sorted_list = insertion_sort(sample_list)
    print("Sorted list:  ", sorted_list)