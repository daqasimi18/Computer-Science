#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv){
    int r, c, i, n;
    int width, height;
    int maximum_gray;
    char magic_header[3];
    int total_of_matrix = argc-2;
    int temp;

    FILE* imagein = fopen(argv[1], "r");
    fscanf(imagein, "%s%d%d%d",magic_header, &height, &width, &maximum_gray);
    FILE* imageout = fopen(argv[argc-1], "w");

    int*** array = (int***) malloc(sizeof(int **)*total_of_matrix);
    for(c=0; c < argc-1; c++){
        array[c] = (int**)malloc( sizeof(int*)*height);
    }
    for(r=1; r<argc-1; r++){
        for(n=0; n<height; n++){
            array[r][n] = (int *)malloc( sizeof(int)*width);
        }
    }

    for(n=1; n < argc-1; n++){
        imagein = fopen(argv[n], "r");
        fscanf(imagein, "%s%d%d%d",magic_header, &height, &width, &maximum_gray);
        for(r=0; r< height; r++){
                for(c=0; c<width; c++){
                        fscanf(imagein, "%d", &array[n][r][c]);
            }
        }
    }
    for (r = 0; r<height; r++){
        for (c=0; c<width; c++){
                for (n=2; n<total_of_matrix+1; n++){
                        temp = array[n][r][c];
                        i= n-1;
        while(i>=1 && array[i][r][c] > temp){
                array[i+1][r][c] = array[i][r][c];
                i = i-1;
                }
        array[i+1][r][c] = temp;
            }
        }
    }
    fprintf(imageout, "%s\n", magic_header);  
    fprintf(imageout, "%d %d\n",height, width);   
    fprintf(imageout, "%d\n", maximum_gray);
    for (r = 0; r<height; r++){
        for (c=0; c<width; c++){
                fprintf(imageout,"%d ", array[total_of_matrix/2][r][c]);
        }
            fprintf(imageout, "\n");
    }
    fclose(imagein);
    fclose(imageout);
}



