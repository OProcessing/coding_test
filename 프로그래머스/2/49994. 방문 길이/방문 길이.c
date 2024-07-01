#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
int answer = 0;
long long pose[21][21];
int x =10, y=10;

int judge (int a,int b) {
    if (pose[x+a][y+b] == 0) {
        pose[x+a][y+b] = 1;
        answer++;
    }
    x+=2*a;
    y+=2*b;
}

int transfer(char c) { //이동함수
    if( c =='L') { 
        if (x>1) judge(-1,0);
    }
    else if( c =='R') { 
        if (x<19) judge(1,0);
    }
    else if( c =='U') { 
        if (y<19) judge(0,1);
    }
    else if( c =='D') { 
        if (y>1) judge(0,-1);
    }
    return 0;
}

int solution(const char* dirs) {
    int len = strlen(dirs);
    int arr[len];
    for (int i=0;i<=len;i++){    //문자열 배열 변경
        arr[i]= *(dirs + i);
    }
    for (int i=0;i<=20;i++){      //2차원 배열 생성 함수
        for (int j=0;j<=20;j++){
            pose[i][j] = 0;
        }
    }
    for (int i=0;i<=len;i++){    //이동함수
        transfer(arr[i]);
    }
    return answer;
}