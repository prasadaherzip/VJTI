#include<iostream>
#include<unistd.h>
using namespace std;

int main(){
    fork();
    cout<<"This is process with pid "<<getpid()<<endl;
    return 0;
}