# 입력 [0,1,0,2,1,0,1,3,2,1,2,1]

# 출력 6
# 포인터? 파이썬에 포인터가 있었나 
def trap(self, height: List[int]) -> int:
    if not height:
        return 0
    
    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    
    while left < right:
        left_max, right_max