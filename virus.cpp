#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

const int MAX_N = 1000;
int graph[MAX_N + 1][MAX_N + 1];
bool visited[MAX_N + 1];
int traversal_count = 0;

void DFS(int current_node, int n, int virus_node) 
{
visited[current_node] = true;
traversal_count++;

	if (current_node == virus_node) 
	{
	    printf("%d node traversed, computer %d is dangerous\n", traversal_count, virus_node);
	    return;
	}
	
	for (int i = 1; i <= n; i++) 
	{
	    if (graph[current_node][i] == 1 && !visited[i]) 
		{
	        DFS(i, n, virus_node);
	    }
	}
}

int main() 
{
int n, virus_node = 0;
cin >> n;

	for (int i = 1; i <= n; i++) 
	{
	    int parent, virus;
	    cin >> parent >> virus;
	
	    if (virus == 0) 
		{
	        virus_node = i;
	    }
	    graph[parent][i] = 1;
	}

DFS(0, n, virus_node);

return 0;
}
