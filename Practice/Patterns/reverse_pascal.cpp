#include<iostream>
using namespace std;

int main(){
    int l,b,c,d;
    cout<<"enter no of lines"<<endl;
    cin>>l;
    for(int i=l;i>=0;i--){              //rows
    
        for(int j=1;j<=i;j++){          //columns
           cout<<" ";
        }
        for (int k=i;k<=l;k++){
            for(b=1;b<l;b++)
            {
                cout<<b;
            }
        }
        cout<<endl;
    }
    
    return 0;
}