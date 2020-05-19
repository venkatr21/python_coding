#include<iostream>
using namespace std;
#define IN1 long long test; cin>>test;while(test--)
int main(){
	long long n;
	IN1
	{
		cin>>n;
		if ((n/2)%2){
			cout<<"NO";
		}else{
			cout<<"YES\n";
			long long sume=0;
			for (long long i=0;i<n/2;i++){
				cout<<(i+1)*2<<" ";
				sume+=(i+1)*2;
			}
			for (long long i=n/2;i<n-1;i++){
				cout<<(2*(i-n/2)+1)<<" ";
				sume -= (2*(i-n/2)+1);
			}
			cout<<sume<<"\n";
		}
	}
}
