#include<iostream>
using namespace std;

void findMissing(int arr[],int size){
    int sum=0;
    int n= size+1; //n changed from number elements to +1 considering the missing number
    int e = n*(n+1)/2;      //summation of target total numbers
    for(int a=0;a<size;a++){
        sum = sum + arr[a];
    }
    int val = e - sum;      //subraction of actual difference (output)
    cout<<"Missing number is "<<val;
    return;
}

int main(){
    int arr[]={1,2,3,5,4,8,6};
    int size = sizeof(arr)/sizeof(arr[0]);
    findMissing(arr,size);
    return 0;
}