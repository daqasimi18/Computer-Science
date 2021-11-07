#include<stdio.h>

void mergesort(int array[],int i,int j);
void merge(int array[],int i1,int j1,int i2,int j2);
void quicksort(int array[10],int first,int last);
int main(){
	int i, c, d, swap, position, root;
	int bubble_steps=0;
	int insertion_steps = 0;
	int selection_steps = 0;
	int heap_steps = 0;
	int merge_steps = 0;
	int quick_steps = 0;
	int n = 10;
	int array[10] = {1, 5, 4, 8, 2, 4, 6, 1, 3, 5};
//BUBBLE SORT
	for(c=0; c<n-1; c++){
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

//INSERTION SORT
	for(c=1; c<n; c++){
		swap = array[c];
		d = c-1;
		while((swap<array[d]) && (d>=0)){
			array[d+1] = array[d];
			d = d-1;
			insertion_steps ++;
		}
		array[d+1] = swap;
		insertion_steps ++;
	}
	printf("Insertion sorted array\n");
	for(c=0; c<n; c++)
		printf("%d\n", array[c]);
	printf("It takes %d steps to sort Insertion Sort\n", insertion_steps);

//SELECTION SORT
	for(c = 0; c<n-1; c++){
		position = c;

		for(d=c+1; d<n; d++){
			printf("%dis the value of d\n",d );
			if(array[position] > array[d])
			position = d;
			selection_steps ++;
			printf("%dIs the position\n", position);
			if(position != c){
				swap = array[c];
				array[c] = array[position];
				array[position] = swap;
				printf("%dthis is swap\n", swap);
			}
		}
	}
	printf("Selection sorted array\n");
	for(c=0; c<n; c++)
		printf("%d\n", array[c]);
	printf("It takes %d steps to sort Selection Sort\n", selection_steps);
//HEAP SORT
   	for (i = 1; i < n; i++){
       c = i;
       do
       {
           root = (c - 1) / 2;            
           if (array[root] < array[c])   
           {                                  
               swap = array[root];      
               array[root] = array[c];     
               array[c] = swap;
               heap_steps ++;
           }
           c = root;
       } while (c != 0);
   }
   for (i = 0; i < n; i++)        
   for (d = n - 1; d >= 0; d--)
   {
       swap = array[0];
       array[0] = array[d];   
       array[d] = swap;
       root = 0;
       heap_steps ++;
       do
       {
           c = 2 * root + 1;    
           if ((array[c] < array[c + 1]) && c < d-1)
               c++;
           if (array[root]<array[c] && c<d)    
           {
               swap = array[root];
               array[root] = array[c];
               array[c] = swap;
               heap_steps ++;
           }
           root = c;
       } while (c < d);
   }
   printf("Heap sorted array\n");
   for (i = 0; i < n; i++)
      printf("%d\n", array[i]);
   printf("It takes %d steps to sort Heap sort\n", heap_steps);

//MERGE SORT
	mergesort(array,0,n-1);
	
	printf("Merge sorted array\n");
	for(i=0;i<n;i++)
		printf("%d\n",array[i]);

    printf("Quick sorted array");
    quicksort(array,0,n-1);
    for(i=0;i<n;i++)
      printf("%d\n",array[i]);
		
	return 0;
}
void mergesort(int a[],int i,int j)
{
	int mid;
		
	if(i<j)
	{
		mid=(i+j)/2;
		mergesort(a,i,mid);		//left recursion
		mergesort(a,mid+1,j);	//right recursion
		merge(a,i,mid,mid+1,j);	//merging of two sorted sub-arrays
	}
}
 
void merge(int array[],int i1,int j1,int i2,int j2)
{
	int temp[50];	
	int i,j,k;
	i=i1;	
	j=i2;	
	k=0;
	
	while(i<=j1 && j<=j2)	
	{
		if(array[i]<array[j])
			temp[k++]=array[i++];
		else
			temp[k++]=array[j++];
	}
	while(i<=j1)
		temp[k++]=array[i++];
		
	while(j<=j2)
		temp[k++]=array[j++];
	for(i=i1,j=0;i<=j2;i++,j++)
		array[i]=temp[j];
}

//QUICK SORT
void quicksort(int array[],int first,int last)
{
   int i, j, pivot, temp;
   int number[10];
   int n = 10;
   if(first<last){
      pivot=first;
      i=first;
      j=last;

      while(i<j){
         while(number[i]<=number[pivot]&&i<last)
            i++;
         while(number[j]>number[pivot])
            j--;
         if(i<j){
            temp=number[i];
            number[i]=number[j];
            number[j]=temp;
         }
      }

      temp=number[pivot];
      number[pivot]=number[j];
      number[j]=temp;
      printf("%d is the pivot\n", pivot);
      quicksort(number,first,j-1);
      quicksort(number,j+1,last);
  }

}



























