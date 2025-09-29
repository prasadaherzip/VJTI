#include<iostream>
#include<unistd.h>
using namespace std;

int main(){
    int a = 42;
    cout<<"My Process ID is: "<<getpid()<<endl;
    cout<<"Variable adderess: "<<&a<<endl;
    cout<<"Enter to exit"<<endl;
    cin.get();
    return 0;
}

