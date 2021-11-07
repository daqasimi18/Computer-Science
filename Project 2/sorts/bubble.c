#include<stdio.h>
int main(){
	int i, c, d, swap, position, root;
	int bubble_steps=0;//, insertion_steps, selection_steps, heap_steps, merge_steps, quick_steps;
	int n = 10;
	int array[10] = {1, 5, 4, 8, 2, 4, 6, 1, 3, 5};
//BUBBLE SORT
	for(c=0; c<n-1; c++){
		//bubble_steps ++;
		for(d=0; d<n-c-1; d++){
			if(array[d] > array[d+1]){
				swap = array[d];
				array[d] = array[d+1];
				array[d+1] = swap;
				bubble_steps ++;
			}
		}
	}
	printf("Bubble Sorted array\n");
	for(c=0; c<n; c++)
		printf("%d\n", array[c]);
	printf("It takes %d steps to sort Bubble Sort\n", bubble_steps);
}