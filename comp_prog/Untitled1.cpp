#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int isSubstring(string s1, string s2) 
{ 
    int M = s1.length(); 
    int N = s2.length(); 
    for (int i = 0; i <= N - M; i++) { 
        int j; 
        for (j = 0; j < M; j++) 
            if (s2[i + j] != s1[j]) 
                break; 
  
        if (j == M) 
            return i; 
    } 
  
    return -1; 
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    long long test,n,f[1000],b[1000],mini,first,last,counter=0;
    int flag=0;
    cin>>test;
    string s,t,a="",s1="",s2="";
    char ele;
    for(long long i=0;i<test;i++){
        cin>>n;
        cin>>s;
        cin>>t;
        for(long long i=0;i<n;i++){
            cin>>f[i];
        }
        for(long long i=0;i<n;i++){
            cin>>b[i];
        }
        counter = 0;
        a="";
        s1="";
        s2="";
        reverse(s.begin(),s.end());
        a="";
        mini=0;
        while (s.length()>0){
            ele = s[s.length()-1];
            s.pop_back();
            first = f[counter];
            last = b[counter];
            s1= ele+a;
            s2= a+ele;
            if(isSubstring(s1,t)!=-1 && isSubstring(s2,t)!=-1){
                if(first<=last){
                mini+=first;
                    s=s1;
                }
                else{
                mini+=last;
                    a=s2;
                }
            }
            else if(isSubstring(s1,t)!=-1){
                mini+=first;
                a=s1;
            }
            else if(isSubstring(s2,t)!=-1){
                mini+=last;
                a=s2;
            }
            else{
            flag = -1;
            break;
            }
        }
        if(flag==-1){
        cout<<"cannot be formed";
        }
        else{
        cout<<mini;
        }
    }
    return 0;
}
