# Minimum Size Subarray Sum

def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    left, total = 0, 0
    result = float("inf")

    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            # (right - left + 1 equals lenth of current subarray)
            result = min(right - left + 1, result)
            # subtract number at left pointer
            total -= nums[left]
            # move left pointer to right one
            left += 1

    return 0 if result == float("inf") else result

# Fruit Into Baskets

def totalFruits(self, fruits: List[int]) -> int:
    # initialize hashmap for fruits in baskets
    count = collections.defaultdict(int)
    left, total, result = 0, 0, 0

    for right in range(len(fruits)):
        count[fruits[right]] += 1
        total += 1

        # shrink window if more than 2 types of fruits
        while (len(count) > 2):
            # getting leftmost fruit and removing from basket
            f = fruits[left]
            count[f] -= 1
            total -=1
            left += 1

            # remove the basket if fruit type count becomes 0
            if not count[f]:
                count.pop(f)

        result = max(result, total)
    
    return result 

# Longest Substring Without Repeating Characters

def lengthOfLongestSubstring(self, s: str) -> int:
    charSet = set()
    left, result = 0, 0

    for right in range(len(s)):

        # if character in set, update window by sliding to the right
        # and removing left from set
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1

        charSet.add(s[right])

        result = max(result, right - left + 1)

    return result


