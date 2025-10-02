#include<iostream>
using namespace std;

//function that calculates all the stuff

void findSubarray(int arr[], int n, int target){     //arr,n,target are parameters
        for(int i=0;i<n;i++){   //n gets size of array
            int sum=0;   //store the subarray addition
            for(int j=i;j<n;j++){ //loop for the 2nd number
                sum += arr[j];

                if(sum==target){
                cout<<"Output : ["<<i+1<<", "<<j+1<<"]"<<endl;
                return;
                }
            }
        }
    cout<<"Output :[-1]";
}

int main(){
    int arr[5]={1,2,3,7,5};
    int target = 12;
    int n= sizeof(arr)/sizeof(arr[0]);
    findSubarray(arr,n,target);
    return 0;
}