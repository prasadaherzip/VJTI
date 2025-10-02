#include<iostream>
#include<algorithm>
#include<math.h>

using namespace std;

int main(){
    int a[6] = {1,5,6,6,9,10};
    int n = sizeof(a)/sizeof(a[0]);
    int k = 7;
    sort(a, a+n);
    int maxv=0, minv=0;
    int ans = a[n-1]-a[0];
    int lar = a[n-1]-k, sml = a[0]+k;

    for(int i=0;i<n-1;i++){
        minv = min(sml, a[i+1] - k);
        maxv = max(lar, a[i] + k);
        if(minv<0) continue;
        ans = min(ans, maxv-minv);
    }

    cout << ans<<endl;
    return 0;
}