 

1. Naive Matching (원시적인 매칭) - 

2. Automata Algorithm (오토마타를 이용한 매칭) - 

3. Rabin-Karp Algorithm (라빈-카프 알고리즘) - 

4. Knuth-Morris-Pratt(KMP) Algorithm (KMP알고리즘) - 

5. Boyer-Moore Algorithm (보이어-무어 알고리즘) -







Naive Matching (원시적인 매칭)
txt[0...n-1] text와 pat[0...m-1] pattern이 주어질 때 txt를 하나씩 접근하여 pat와 일치하는지 확인하는 것이다. 

 

 Navie Matching 알고리즘이다. 

# Searching algorithm 
def search(pat, txt): 
    M = len(pat) 
    N = len(txt) 

    # A loop to slide pat[] one by one */ 
    for i in range(N - M + 1): 
        j = 0
          
        # For current index i, check  
        # for pattern match */ 
        while(j < M): 
            if (txt[i + j] != pat[j]): 
                break
            j += 1
      
        if (j == M):  
            print("Pattern found at index ", i) 



참고자료:

http://nlp.jbnu.ac.kr/AL/ch10.pdf

https://www.geeksforgeeks.org/naive-algorithm-for-pattern-searching/