# Given an array of strings strs, 
# group the anagrams together. 
# You can return the answer in any order.

# An Anagram is a word or phrase formed
# by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# you can use only immutable type as a key in hash map.
# string and tuple are immutable types in python while list is not.
def groupAnagrams(strs):
    # first thought : using dictionary
    final_result = []
    hash_idx = set()
    for i, str in enumerate(strs):
        if i in hash_idx:
            continue
        chars = set(str)
        result = []
        for j, str2 in enumerate(strs):
            chars2 = set(str2)
            if chars2 != chars:
                continue
            else:
                hash_idx.add(j)
                result.append(str2)
        final_result.append(result)
strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)