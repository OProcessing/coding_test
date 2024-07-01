#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char arr[100]={0,}, count=0;
    scanf("%s",arr);

    for (int i=0;i<100;i++) {
        if(arr[i]!=0) { 
            count++;
            if(arr[i]=='l'||arr[i]=='n') {
                if (arr[i+1]=='j') i++;
            }
            if(arr[i]=='d'&&arr[i+1]=='z'&&arr[i+2]=='=') {
                i+=2;
            }
            if (arr[i]=='d'||arr[i]=='c') {                
                if (arr[i+1]=='-') { 
                    i++;
                }
            }
            if (arr[i]=='c'||arr[i]=='z'||arr[i]=='s') {
                if (arr[i+1]=='=') {
                    i++;
                }
            }
        }
    }
    printf("%d",count);
    return 0;
}