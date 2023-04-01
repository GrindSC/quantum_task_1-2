import time

def calculate_sum(N):
    # To solve this problem in O(1) time complexity i use the Gauss summation formula as following:
    # N = 4
    # Sum = 1 + 2 + 3 + 4
    # Sum = N + (N-1) + (N-2) + (N-3)
    # 2*Sum = (N+1) + (N+1) + (N+1) + (N+1)
    # Sum = N*(N+1)/2
    return N*(N+1)//2

assert calculate_sum(1)==1
assert calculate_sum(3)==6
assert calculate_sum(10)==55
start=time.time()
for i in range(10000):
    calculate_sum(10**25)
print(time.time()-start)
    

