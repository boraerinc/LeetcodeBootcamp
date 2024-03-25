# Week 2 Homework Problems

# 8. String to Integer (atoi)

def myAtoi(self, s: str) -> int:
    s = s.strip()
    if len(s) == 0:
        return 0
    i, val, sign = 0, 0, 1
    max_val = (2**31 - 1) // 10
    if s[0] in '+-':
        if s[0] == '-':
            sign = -1 
        else:
            sign = 1 
        i += 1
    while i < len(s) and s[i].isdigit():
        curr = int(s[i])
        if val > max_val or (val == max_val and curr > 7):
            if sign == 1:
                return 2**31 - 1
            else:
                return -2**31
        val = 10 * val + curr
        i += 1
    return sign * val

# 424. Longest Repeating Character Replacement

def characterReplacement(self, s: str, k: int) -> int:
    left = 0
    max_freq = 0
    freq = {}
    max_window_size = 0
    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1
        max_freq = max(max_freq, freq[s[right]])
        while (right - left + 1) - max_freq > k:
            freq[s[left]] -= 1
            left += 1
            max_freq = max(freq.values())
        max_window_size = max(max_window_size, right - left + 1)
    
    return max_window_size

# 336. Palindrome Pairs

def palindromePairs(self, words):
    dic = {}
    res = []
    for i, w in enumerate(words):
        dic[w[::-1]] = i
    
    for i, word in enumerate(words):
        for cut in range(len(word) + 1):
            pref, suf = word[:cut], word[cut:]
            if pref in dic and i != dic[pref] and suf == suf[::-1]:
                res.append([i, dic[pref]])
            if suf in dic and i != dic[suf] and pref == pref[::-1] and cut != 0:
                res.append([dic[suf], i])
    return res
