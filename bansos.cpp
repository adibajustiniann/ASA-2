#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

string subsetSum(vector<int> arr, int N, int K) 
{
    if(K == 1)
	{
        return "Ya";
    }
    if(N < K)
	{
        return "Tidak";
    }
    
    int total = 0;
    for(int i = 0; i < N; i++)
	{
        total += arr[i];
    }
    if(total % K != 0)
	{
        return "Tidak";
    }
    
    int goalSum = total / K;
    vector<int> subset(K, 0);
    
    sort(arr.begin(), arr.end(), greater<int>());
    
    for(int i = 0; i < K; i++)
	{
        subset[i] = arr[i];
    }
        
    for(int i = K; i < N; i++)
	{
        int j = 0;
        while((j < K) && (subset[j]+arr[i] > goalSum))
		{
            j++;
        }
        if(j == K)
		{
            return "Tidak";
        }
        subset[j] += arr[i];
    }
        
    return "Ya";
}

int main() {
    int N, K;
    cin >> N;
    vector<int> arr(N);
    for(int i = 0; i < N; i++) 
	{
        cin >> arr[i];
    }
    cin >> K;
    
    string hasil = subsetSum(arr, N, K);
    cout << hasil << endl;
    
    return 0;
}
