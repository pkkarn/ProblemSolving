def longestsubstring(s: str) -> int:
    # set sub length equal to 0 initially
    long_sub_length = 0;

    # if string is not empty
    if len(s) != 0:
        # i to track and loop throught each element and to get index
        i = 0;
        # to record element whenever we see it first
        lookup = {}
        # count of substring whenever we would see that first we will record it 
        sub_string_count = 0;

        while i < len(s):
            # if current char is avaialble in string then reset substring count and lookup
            if s[i] in lookup:
                i = lookup[s[i]] + 1 # get index of that first occurence and set i = i + 1
                sub_string_count=0
                lookup = {}

                lookup[s[i]] = i
                sub_string_count = 1
                long_sub_length = max(long_sub_length, sub_string_count)
            else:
                # else add that in lookup
                lookup[s[i]] = i
                # update its length
                sub_string_count+=1
                # and set to longest if you think its longer than last substring
                long_sub_length = max(long_sub_length, sub_string_count)
            i+=1

    
    return long_sub_length



# Optimized solution
def lengthOfLongestSubstring(self, s: str) -> int:
    long_sub_length = 0 # sub length would be 0
    lookup = {} # to store lookup
    start = 0 # first pointer

    # i would be second pointer, : Sliding Window pattern
    for i in range(len(s)):
        if s[i] in lookup: # if seen in lookup
            start = max(start, lookup[s[i]] + 1) # update start pointer if element is seen and bigger than old seen element
        lookup[s[i]] = i
        long_sub_length = max(long_sub_length, i - start + 1)
    
    return long_sub_length

print(longestsubstring('abcabcbb'))
print(longestsubstring('bbbbb'))
print(longestsubstring('pwwkew'))
print(longestsubstring('dvdf'))


# One issue can be: You are trying to count from the place where you check is not available but chances are that
# there might be cases when right before the first lookup you have to check #dvcsdf
# if item exsit there then know theri place instead of stroing True in lookup store their index, and right it just after
# that index