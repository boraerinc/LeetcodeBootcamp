# Week 1 Homework Problems

# 217. Contains Duplicate

def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums))<len(nums)

# 1024. Video Stitching

def videoStitching(self, clips: List[List[int]], time: int) -> int:
    clips.sort()
    max_len, curr, i, res = 0, 0, 0, 0
    
    while i < len(clips):
        while i < len(clips) and not (clips[i][0] > curr):
            start, end = clips[i]
            i+=1
            max_len = max(end, max_len)
        if curr == max_len:
            return -1
        res += 1
        curr = max_len
        if curr >= time:
            return res
    return -1

# 11. Container With Most Water

def maxArea(self, height: List[int]) -> int:
    max_area = 0
    left = 0
    right = len(height) - 1
    while left < right:
        width = right - left
        if(height[left]< height[right]):
            area = height[left]*width
        else:
            area = height[right]*width
        if area> max_area:
            max_area = area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area
