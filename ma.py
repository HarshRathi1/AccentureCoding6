'''def ProductSmallestPair(sum, arr)
The function accepts an integers sum and an integer array arr of size n. Implement the function to find the pair, (arr[j], arr[k]) where j!=k, Such that arr[j] and arr[k] are the least two elements of array (arr[j] + arr[k] <= sum) and return the product of element of this pair
NOTE
Return -1 if array is empty or if n<2
Return 0, if no such pairs found
All computed values lie within integer range
Example
Input
sum:9
Arr:5 2 4 3 9 7 1
Output
2
Explanation
Pair of least two element is (2, 1) 2 + 1 = 3 < 9, Product of (2, 1) 2*1 = 2. Thus, output is 2'''
sum=int(input())
arr=list(int(i) for i in input().split())
def ProductSmallestPair(sum,arr):
    n=len(arr)
    if n<2:
        return -1
    for j in sorted(arr):
        for k in sorted(arr):
            if j!=k and j+k<=sum:
                return j*k
        else:
            return 0
print(ProductSmallestPair(sum,arr))