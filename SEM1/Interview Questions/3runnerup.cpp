#include<iostream>
using namespace std;

int findSecondLargest(int arr[], int size){

    if(size<2){     //if array less than 2 elements return -1
        return -1;
    }
    int largest = arr[0];   //assume 1st element largest
    for(int a=1;a<size;a++){    //to comapres all other elements to 1st element
        if(arr[a]>largest){
            largest = arr[a];
        }
    }
    int second = -1;
    for(int i=0;i<size;i++){
        if(arr[i]!=largest && arr[i]>second){
            second = arr[i];
        }
    }
    return second;
}

int main(){
    int arr[]={12,35,1,10,12,1};
    int size = sizeof(arr)/sizeof(arr[0]);
    int result = findSecondLargest(arr,size); //store the returned val of fucntion to result
    cout<<"Second largest element is "<<result<<endl;
    return 0;
}