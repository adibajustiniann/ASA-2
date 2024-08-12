# input
N = int(input())
arr = list(map(int, input().split()))
K = int(input())

def subsetSum(arr, N, K):
    if(K == 1):
        return "Ya"
    if(N < K):
        return "Tidak"
    
    total = sum(arr)
    if(total % K != 0):
        return "Tidak"
    
    goalSum = total // K
    subset = [0] * K
    
    arr.sort(reverse=True)
    
    for i in range(K):
        subset[i] = arr[i]
        
    for i in range(K, N):
        j = 0
        while((j < K) and (subset[j]+arr[i] > goalSum)):
            j += 1
        if(j == K):
            return "Tidak"
        subset[j] += arr[i]
        
    return "Ya"

hasil = subsetSum(arr, N, K)
print(hasil)