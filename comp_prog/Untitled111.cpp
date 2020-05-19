#include <cmath>
#include <iostream>
#include<cstdlib> 
using namespace std;

long long V;

long long min(long long a,long long b,long long c,long long d ){
 long long t1,t2;
 t1=fabs(a-c);
 t2=fabs(b-d);
 if(t1>t2)
 return (t2);
 return (t1);
}


long long minKey(long long key[], bool mstSet[])  
{   
    long long miny = INT_MAX, min_index;  
  
    for (long long v = 0; v < V; v++)  
        if (mstSet[v] == false && key[v] < miny)  
            miny = key[v], min_index = v;  
  
    return min_index;  
}   
void printMST(long long parent[], long long graph[10][10])  
{  
    cout<<"Edge \tWeight\n";  
    for (long long i = 1; i < V; i++)  
        cout<<parent[i]<<" - "<<i<<" \t"<<graph[i][parent[i]]<<" \n";  
}  
void primMST(long long graph[10][10])  
{    
    long long parent[V];   
    long long key[V];  
    bool mstSet[V];  
    for (long long i = 0; i < V; i++)  
        key[i] = INT_MAX, mstSet[i] = false;   
    key[0] = 0;  
    parent[0] = -1; 
    for (long long count = 0; count < V - 1; count++) 
    {    
        long long u = minKey(key, mstSet);  
        mstSet[u] = true;  
        for (long long v = 0; v < V; v++)  
  
            if (graph[u][v] && mstSet[v] == false && graph[u][v] < key[v])  
                parent[v] = u, key[v] = graph[u][v];  
    }  
    printMST(parent, graph);  
}

int main() {
    long long n, a[100],b[100],i,j,temp;
    cin>>V;
    for(long long i=0;i<V;i++){
    cin>>a[i];
	cin>>b[i];
    }
    long long graph[10][10];
    for(i=0;i<V;i++){
    for(j=0;i<V;j++)
    graph[i][j]=0;
    }
    for(i=0;i<V;i++){
        for(j=i+1;j<V;j++){
            temp = min(a[i],b[i],a[j],b[j]);
            graph[i][j]=temp;
            graph[j][i]=temp;
            }}
    primMST(graph);
    return 0;
}
