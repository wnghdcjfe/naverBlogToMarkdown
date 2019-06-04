# 백준 5557번 1학년 #DP ★ 

https://www.acmicpc.net/problem/5557

## 주안점 

1. 전형적인 다이나믹 프로그래밍​왜 이렇게 오늘 하루종일 부진할까 생각했는데 알고보니 지금까지 푼 문제가 14문제다. 하루에 2문제도 못풀어서 끙끙대던 나를 생각하니 기쁘다. ​​​​​​​​​​​​​

## 구조 

dp[index][sum] ​

## 코드 
```

#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;  
typedef long long ll; 
ll a[101], dp[101][21], n; 
ll go(int index, int sum){
    if(sum < 0 || sum > 20) return 0; 
    if(dp[index][sum] != -1) return dp[index][sum];  
    if(index == n - 2){
        if(sum == a[n - 1])return 1; 
        else return 0; 
    }
    ll &ret = dp[index][sum];
    ret = 0; 
    ret +=  go(index + 1, sum + a[index + 1]); 
    ret +=  go(index + 1, sum - a[index + 1]); 
    return ret;  
}
int main(){  
    scanf("%lld", &n); 
    for(int i = 0; i < n; i++){
        scanf("%lld", a + i); 
    } 
    fill(&dp[0][0], &dp[0][0] + 101 * 21, -1);
    printf("%lld\n", go(0, a[0])); 
    return 0;
} 

```

탑바텀으로 풀 수 있고

```

    d[0][a[0]] = 1;
    for (int i = 1; i < n; i++) {
        for (int j = 0; j <= 20; j++) {
            if (j - a[i] >= 0) {
                d[i][j] += d[i-1][j-a[i]];
            }

```

바텀업으로도 이런식으로 풀 수 있다. 

