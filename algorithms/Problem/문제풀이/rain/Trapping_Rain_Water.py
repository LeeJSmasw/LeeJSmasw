# 입력 [0,1,0,2,1,0,1,3,2,1,2,1]

# 출력 6
# 포인터? 파이썬에 포인터가 있었나 
def trap(self, height: List[int]) -> int: 
    # -> 리턴값이 int 임을 보여주기 위한거임 근데 이건 그렇다고 쳐도 위에 이건 뭐지 
    
    if not height:
        return 0
    
    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    
    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)
        
        if left_max <= right_max:
            volume += left_max - height[left]
            left +=1
        else:
            volume += right_max -height[right]
            right -=1
            
        
    return volume 