#include<iostream>
#include<unistd.h>
using namespace std;

int main(){
    if(fork()>0)
sleep(100);
}

