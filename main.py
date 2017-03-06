"""Array reversal program written by Taylor Flatt"""

def reverse(arr, start, end):
    """Reverses an array between two indices.

    Args:
        arr: The array to be reversed.
        start: The start index of the array.
        end: The end index of the array.
    Returns:
        None.
    Raises:
        ValueError: If start >= end.

    """

    if start >= end:
        ValueError("The start index must be less than the end index.")
    else:
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

def rotate(arr, n, p):
    """Rotates an array.

    Args:
        arr: The array to be rotated.
        n: The size of arr.
        p: The number of rotations to be performed.
    Returns:
        An array rotated p times.
    Raises:
        ValueError: If p > n.

    """
    if p > n:
        raise ValueError("The number of rotations must be less than"
                         " the size of the array.")
    else:
        reverse(arr, 0, p - 1)
        reverse(arr, p, n - 1)
        reverse(arr, 0, n - 1)
        return arr

def user_input():
    """User input method returns the array.

    Args:
        None.
    Returns:
        A tuple consisting of the array, size of the array, and number
        of rotations.
    Raises:
        None.

    """
    print("\nWelcome to the array reversal program! \n\nYou will be"
          " asked to enter your data shortly but please note that\n"
          "if you would like to do right-reversals, you must input"
          " a negative \nvalue. A positive value will perform a left-"
          "reversal.\n\nEnjoy!\n")

    n = int(input("Input the number of arr items: "))
    arr = []
    for i in range(0, n):
        arr.append(input("Element: "))
    p = int(input("Number of rotations: "))

    return(arr, n, p)

def mod_juggle(arr, n, p):
    """Iterates through the list and returns a rotated list.

    Args:
        arr: The array to be rotated.
        n: The size of arr.
        p: The number of rotations to be performed.
    Returns:
        An array rotated by p values.
    Raises:
        None.

    """
    n_arr = []
    for i in range(0, n):
        n_arr.insert((i + p) % n, arr[i])
    return n_arr

def main():
    """Calls functions which return a rotated array."""
    arr, n, p = user_input()

    if p > n:
        print(mod_juggle(arr, n, p))
    else:
        print(rotate(arr, n, p))

if __name__ == "__main__":
    main()
