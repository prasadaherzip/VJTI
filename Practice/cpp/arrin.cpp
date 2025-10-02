#include<iostream>
using namespace std;

int main(){
    int arr[5];

    cout<<"Enter the numbers for the array "<<endl;
    for(int a=0;a<5;a++){
        cin>>arr[a];
    }
    cout<<"What you entered "<<endl;
    for(int i=0;i<5;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    return 0;
}