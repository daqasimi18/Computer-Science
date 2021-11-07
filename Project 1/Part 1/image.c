#include <stdio.h> 
  
int main(int argc, char** argv){
    int i, j;
    char magic_header[3]; 
    int rows, cols;
    int maximum_gray;
    int width, height; 

    FILE* imagein = fopen(argv[1], "r");
    FILE* imageout = fopen(argv[2], "w");
    FILE* Imageout = fopen(argv[3], "w");
    

    fscanf(imagein,"%s%d%d%d ",magic_header,&width,&height,&maximum_gray);
    int array[width][height];
    for (rows=0; rows<height; rows++){
        for (cols=0; cols < width; cols++)
        {    
            fscanf(imagein,"%d", &array[rows][cols]);
        }
    }
    //NEGATIVE PGM
    fprintf(imageout, "%s\n", magic_header);  
    fprintf(imageout, "%d %d\n",width,height);  
    fprintf(imageout, "%d\n", maximum_gray-150);  
    for (i = 0; i < height; i++) { 
        for (j = 0; j < width; j++) { 
            fprintf(imageout, "%d ",array[i][j]); 
        } 
        fprintf(imageout, "\n"); 
    }
    //Rotate 90 degrees clockwise
    fprintf(Imageout, "%s\n", magic_header);  
    fprintf(Imageout, "%d %d\n",width,height);   
    fprintf(Imageout, "%d\n", maximum_gray);   
    for (i = 0; i < height; i++) { 
        for (j = 0; j < width; j++) { 
            fprintf(Imageout, "%d ", array[height-j-1][i]); 
        } 
        fprintf(Imageout, "\n"); 
    } 
    fclose(imageout);  
    fclose(Imageout);
}

