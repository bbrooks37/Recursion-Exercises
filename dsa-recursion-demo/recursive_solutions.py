# Product of Nums
def product(nums):
    if not nums:
        return 1
    return nums[0] * product(nums[1:])

# Longest Word
def longest(words):
    if not words:
        return 0
    return max(len(words[0]), longest(words[1:]))

# Every Other Character
def everyOther(s):
    if not s:
        return ''
    return s[0] + everyOther(s[2:])

# Is Palindrome?
def isPalindrome(s):
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return isPalindrome(s[1:-1])

# Find Index
def findIndex(arr, target, index=0):
    if index == len(arr):
        return -1
    if arr[index] == target:
        return index
    return findIndex(arr, target, index + 1)

# Reverse String
def revString(s):
    if not s:
        return ''
    return s[-1] + revString(s[:-1])

# Gather Strings
def gatherStrings(obj):
    strings = []

    def _gather(o):
        if isinstance(o, dict):
            for value in o.values():
                _gather(value)
        elif isinstance(o, str):
            strings.append(o)

    _gather(obj)
    return strings

# Balanced Brackets
def is_balanced(s):
    if not s:
        return True

    def remove_pair(s, open_br, close_br):
        index = s.find(open_br + close_br)
        if index == -1:
            return s
        return s[:index] + s[index + 2:]

    pairs = ['()', '{}', '[]']
    for pair in pairs:
        s = remove_pair(s, pair[0], pair[1])
        if is_balanced(s):
            return True

    return False

# Further Study: Binary Search
def binarySearch(arr, value, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == value:
        return mid
    elif arr[mid] > value:
        return binarySearch(arr, value, low, mid - 1)
    else:
        return binarySearch(arr, value, mid + 1, high)

# Test Cases
if __name__ == "__main__":
    print("Product of Nums:")
    print(product([2, 3, 4]))  # Output: 24
    
    print("\nLongest Word:")
    print(longest(["hello", "hi", "hola"]))  # Output: 5
    
    print("\nEvery Other Character:")
    print(everyOther("hello"))  # Output: "hlo"
    
    print("\nIs Palindrome?")
    print(isPalindrome("tacocat"))  # Output: True
    print(isPalindrome("tacodog"))  # Output: False
    
    print("\nFind Index:")
    animals = ["duck", "cat", "pony"]
    print(findIndex(animals, "cat"))  # Output: 1
    print(findIndex(animals, "porcupine"))  # Output: -1
    
    print("\nReverse String:")
    print(revString("porcupine"))  # Output: "enipucrop"
    
    print("\nGather Strings:")
    nestedObj = {
        "firstName": "Lester",
        "favoriteNumber": 22,
        "moreData": {
            "lastName": "Testowitz"
        },
        "funFacts": {
            "moreStuff": {
                "anotherNumber": 100,
                "deeplyNestedString": {
                    "almostThere": {
                        "success": "you made it!"
                    }
                }
            },
            "favoriteString": "nice!"
        }
    }
    print(gatherStrings(nestedObj))  # Output: ["Lester", "Testowitz", "you made it!", "nice!"]
    
    print("\nBalanced Brackets:")
    print(is_balanced("(){}[]"))  # Output: True
    print(is_balanced("{[()]}"))  # Output: True
    print(is_balanced("{[(])}"))  # Output: False
    print(is_balanced("{{[[(())]]}}"))  # Output: True
    
    print("\nBinary Search:")
    print(binarySearch([1, 2, 3, 4], 1))  # Output: 0
    print(binarySearch([1, 2, 3, 4], 3))  # Output: 2
    print(binarySearch([1, 2, 3, 4], 5))  # Output: -1
