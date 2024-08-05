#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int main() {
    int N;
    int class[1000]={0,};
    scanf("%d",&N);
    for (int i=0;i<N;i++) {
        double sum=0, avr=0, ext = 0;
        scanf("%d", &class[0]);
        for (int j=1;j<=class[0];j++){
            scanf("%d", &class[j]);
            sum+=class[j];
        }
        avr = sum/class[0];
        for(int j=1;j<=class[0];j++) {
            if (class[j]>avr) { 
                ext++;
            }
        }
        double rate = ext*100/class[0];
        printf("%.3f%%\n",rate);
    }
    return 0;
}