# 이코테(부품찾기) 어제문제 다시해보기 p.197

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
M = int(input())
target_list = list(map(int,input().split()))
nums.sort()

def search(start,end,target):
    if start==end:
        if nums[start]==target:
            print('yes')
        else:
            print('no')
        return
    mid = (start+end)//2
    if nums[mid]<target:
        search(mid+1,end,target)
    else:
        search(start,mid,target)
    
for target in target_list:
    search(0,N-1,target)
