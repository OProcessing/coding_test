#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int main() {
    int count[26]={0,}, num=0, Max=0, answer;
    char input[1000000];
    scanf("%s", &input);
    int len = strlen(input);



    for (int i=0;i<len;i++){
        if(input[i]<='Z') {  //capital
            num = input[i] - 'A';
        }
        else if(input[i]>='a') {
            num = input[i] - 'a';
        }
        count[num]++;
    }

    for(int i=0;i<26;i++) {
        if(count[i]>Max) {
            Max = count[i];
            answer = 'A' + i;
        }
        else if (count[i]==Max) {
            answer = '?';
        }
    }
    printf("%c", answer);
    
    return 0;
}