# DFS 집 단지 찾아서 몇단지인지 입력하고 갯수출력하기
# 포인트
# 이중for문을 통해 '1'이나오고&& 아직 방문을 안한거였을때 => 그래프탐색을 시작
# => 이때 재귀함수를 호출할거다


# 그래프저장(그림) int[][]
# 방문여부 : bool[][]
# 결과값 int[]

import sys
input=sys.stdin.readline
N=int(input())

map = [list(map(int,input().strip())) for _ in range(N)]
chk = [[False]*N for _ in range(N)]
result=[]
each=0
dy=[0,1,0,-1]       # 옆에부분 거의 외워서 사용하기 4방향검사
dx=[1,0,-1,0]


def dfs(y,x):
    global each
    each +=1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny < N and 0 <=nx<N:
            if map[ny][nx]==1 and chk[ny][nx]==False:
                chk[ny][nx]=True
                # 모든조건이 충족하면 재귀
                dfs(ny,nx)
        
        
        
for j in range(N):
    for i in range(N):
        if map[j][i]==1 and chk[j][i]==False:
            chk[j][i]=True
            each=0  #초기화
            dfs(j,i)
            result.append(each)
            # 그래프에 1이고 아직 방문한적이없다면(False)
            # 방문했다고 표시를 해줘야한다.
            # dfs로 크기 구하기
            # 구한 크기를 결과 리스트에 넣기
            
            
        

result.sort()
print(len(result))
for i in result:
    print(i)
