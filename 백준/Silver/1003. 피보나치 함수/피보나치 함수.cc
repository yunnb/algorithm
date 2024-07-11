#include <iostream>
using namespace std;

int main() {
    int t, n;
    cin >> t;

    int cnt[41][2] = {0, };
    cnt[0][0] = 1;
    cnt[0][1] = 0;
    cnt[1][0] = 0;
    cnt[1][1] = 1;
    for(int i=0; i<t; i++) {
        cin >> n;
        for(int j=2; j < n+1; j++) {
            cnt[j][0] = cnt[j-1][0] + cnt[j-2][0];
            cnt[j][1] = cnt[j-1][1] +  cnt[j-2][1];
        }
        cout << cnt[n][0] << " " << cnt[n][1] << endl;
    }




}