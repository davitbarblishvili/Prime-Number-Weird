def weird_prime(n):
    answer = True
    count = 2
    while count < n:
        answer = [False,True][math.ceil
                              (math.fabs(math.sin(n%count)))]
        count = [count + 1, n][~answer]
    return answer
    
    
  [j for j in range(1,50) if weird_prime(j)]   
