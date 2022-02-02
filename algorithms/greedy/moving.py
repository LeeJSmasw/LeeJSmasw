# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
from unittest import result

 #N이 왜필요 했을까...
def get_final_position(N, mat, moves):
       #필드만들기(mat가 필드다)
    pos = mat # 필요없는 작업이긴 내가 이해하기 쉽기 위해성
    x,y=0,0
    #현재위치 잡기
    for x_index in range(len(mat)):
        if 1 in pos[x_index]:
            x= x_index
        for y_index in range(len(mat)):
            if 1== pos[x_index][y_index]:
                y= y_index
    # print(x, y) # 현재 위치 확인
    
    #움직여보자 #어떻게 해당하는 열에 넣을 수 있을까..음
    move = {0:[-1,0],1:[+1,0],2:[0,-1],3:[0,1]}
    
    for i in moves: #N을 여기서 써야하나..?
        data_move= move.get(i)
        x = x+data_move[0]
        y = y+ data_move[1]
    
    try:
        result = pos[x][y]
        result = [x,y]
    except:
        result='밖으로 나갔습니다!'
    return result


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    N = 3
    mat = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ] 
    moves1 = [1, 1, 3]
    print(get_final_position(N, mat, moves1)) # [2, 1]
    
    moves2 = [1, 3, 3]
    print(get_final_position(N, mat, moves2)) # [1, 2]

    moves3 = [1, 3, 3,3,3,3,3]
    print(get_final_position(10, mat, moves1)) # [2, 1]
    
    moves4 = [1, 3, 3,3,3,3,3]
    print(get_final_position(N, mat, moves4)) # 밖으로 나갔습니다