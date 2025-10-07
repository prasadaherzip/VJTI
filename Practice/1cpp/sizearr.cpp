#include<iostream>
#include<typeinfo>
using namespace std;

int main(){
    int arr[]={1,2,3,4,5,6,7,8,9};
    int n=sizeof(arr)/sizeof(arr[0]);      //size given in bytes
    cout<<n<<endl; //to find type of the data stored
    cout<<typeid(n).name()<<endl;
    return 0;

}

//to find the size of an array divide the 
//entire byte size of the array by the size of 1 element
