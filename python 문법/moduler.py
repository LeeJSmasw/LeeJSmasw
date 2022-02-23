# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    result=''
    for i in range(len(word)):
        data = ord(word[i])
        index= (data+n)%123
        # print(index)
        
        if index<65:
            if data+n <97:
                data_c = index+65
                data_r = chr(data_c)
                result = result + data_r
            elif data+n >=97:
                data_c=index+97
                data_r = chr(data_c)
                result = result + data_r
        elif index>=65:
            data_r = chr(index)
            result = result + data_r
    return result


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(caesar('apple', 5))
    # fuuqj
    print(caesar('Python', 10))
    # Zidryx


