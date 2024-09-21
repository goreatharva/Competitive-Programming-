#include <stdio.h>
#include <string.h>

char solveAccessCardValidity(int N, int X, char S[]) {
    int swipes = 0;
    for (int i = 0; i < N; i++) {
        if (S[i] == '0') {
            if (swipes == 0) {
                return 'N'; 
            }
            swipes--;
        } else {
            swipes = X; 
        }
    }
    return (swipes >= 0) ? 'Y' : 'N'; 
}

int main() {
    int T, N, X;
    scanf("%d", &T);
    while (T--) {
        scanf("%d %d", &N, &X);
        char S[N+1];
        scanf("%s", S);
        char result = solveAccessCardValidity(N, X, S);
        if (result == 'Y') {
            printf("YES\n");
        } else {
            printf("NO\n");
        }
    }
    return 0;
}
