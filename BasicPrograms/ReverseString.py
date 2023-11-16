# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.


def reverseString(s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    left, right = 0, len(s) - 1

    while left < right:
        # Swap characters at the left and right indices
        s[left], s[right] = s[right], s[left]

        # Move indices towards the center
        left += 1
        right -= 1


arr = ["H", "e", "l", "l", "o"]
reverseString(arr)

print(arr)
