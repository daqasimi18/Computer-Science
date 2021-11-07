//Name: Darab Ali Qasimi, Date: Nov 1 2020 10:20, Collaborator: Is written by myself with the help of TAs and Sofia and with collaboration of Ted Jacquet on merge and quick sort
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <sys/time.h>
#include <time.h>
#include "mysterysorts.h"
int time_category(int sort){
  int i, j, l, m;
  int n = 1024;
  int a[n];
  int o = 2048;
  int b[o];
  int p = 4096;
  int c[p];
  int q = 8192;
  int d[q];
  srand(time(0));
  for(i=0; i<n; i++){
  	a[i] = rand()%1000;
  }
  struct timeval start, finish;
  gettimeofday(&start, 0);
  mysterySort(a, n, sort, -1);
  gettimeofday(&finish, 0);
  double elapse = (finish.tv_sec - start.tv_sec)*1000000 + finish.tv_usec - start.tv_usec;
  for(j=0; j<o; j++){
  	b[j] = rand()%1000;
  }
  struct timeval start_a, finish_a;
  gettimeofday(&start_a, 0);
  mysterySort(b, o, sort, -1);
  gettimeofday(&finish_a, 0);
  double elapse_a = (finish_a.tv_sec - start_a.tv_sec)*1000000 + finish_a.tv_usec - start_a.tv_usec;
  for(l=0; l<p; l++){
  	c[l] = rand()%1000;
  }
  struct timeval start_b, finish_b;
  gettimeofday(&start_b, 0);
  mysterySort(c, p, sort, -1);
  gettimeofday(&finish_b, 0);
  double elapse_b = (finish_b.tv_sec - start_b.tv_sec)*1000000 + finish_b.tv_usec - start_b.tv_usec;
  for(m=0; m<q; m++){
  	d[m] = rand()%1000;
  }
  struct timeval start_c, finish_c;
  gettimeofday(&start_c, 0);
  mysterySort(d, q, sort, -1);
  gettimeofday(&finish_c, 0);
  double elapse_c = (finish_c.tv_sec - start_c.tv_sec)*1000000 + finish_c.tv_usec - start_c.tv_usec;
  int derivative_a = ((elapse_a - elapse)/(o-n));
  int derivative_b = ((elapse_b - elapse_a)/(p-o));
  int derivative_c = ((elapse_c - elapse_c)/(q-p));
  int log_a = derivative_b - derivative_a;
  int log_b = derivative_c - derivative_b;
  if(log_a < 1 && log_b <1){
  	return 0;
  } else{
  	return 1;
  }
  return 0;
  //PASS PASS PASS
}
bool bubble_and_heap_behavior(int array[], int maxsteps, int n, int last_element){
   for(int i=0; i<n-maxsteps; i++){
       if(last_element < array[i]){
         return false;
       }
   }
   return true;
}
bool selectionsort_behavior(int array[], int maxsteps, int n, int smallest){
    for(int i=0; i<n-maxsteps; i++){
        if(smallest > array[i]){
            return false;
        }
    }
    return true;
}
bool insertion_sort(int array[], int maxsteps, int n){
    int sorted;
    for(int i=0; i<n-maxsteps; i++){
        if(array[i] < array[i+1]){
            sorted = 1;
        }
        if(array[i] < array[i+1] && sorted==1){
            return true;
        } if(array[i] > array[i+1] && sorted != 1){
            return false;
        } 
    }
    return true;
}
char* classify(int sort) {
  int sorts = time_category(sort);
  int maxsteps = 50;
  int n = 8192;
  int my_array[n];
  srand (time(0));
  for( int i = 0; i < n; i++ ){ 
    my_array[i] = rand()%1000;
  } 
  //BUBBLE SORT and HEAPSORT
  bool bubble_bool;
  mysterySort(my_array, n, sort, maxsteps);
  bubble_bool = bubble_and_heap_behavior(my_array, maxsteps, n, my_array[n-maxsteps]);
  if(sorts == 1 && bubble_bool == true){
      return "bubble sort";
  }else if(sorts == 0 && bubble_bool == true){
      return "heap sort";
  }
  //SELECTION SORT
  bool selection_bool;
  mysterySort(my_array, n, sort, maxsteps);
  selection_bool = selectionsort_behavior(my_array, maxsteps, n, my_array[0]);
  if(sorts == 1 && selection_bool == true){
      return "selection sort";
  }
  //Collaborated merge and quick sort with Ted Jacquet
  //MERGE AND QUICK SORT
  if(sorts == 0){
      maxsteps = n/2;
      int my_array[n];
      int my_array2[maxsteps];
      for(int i = 0; i<n; i++){
          int temp = rand()%1000;
          my_array[i] = temp;
      }
      for(int j = 0; j<maxsteps; j++){
          my_array2[j] = my_array[j];
      }
      mysterySort(my_array, n, sort, maxsteps);
      mysterySort(my_array2, maxsteps, sort, maxsteps);
      int count = 0;
      for(int f = 0; f<maxsteps; f++){
          if(my_array[f] == my_array2[f]){
              count ++;
          }
      }
             if(count == maxsteps){
                 return "merge sort";
             } else{
                 return "quick sort";
             }
  }
  //INSERTION SORT
  bool insertion_bool;
  mysterySort(my_array, n, sort, maxsteps);
  insertion_bool = insertion_sort(my_array, maxsteps, n);
  if(sorts == 1 && insertion_bool == true){
      return "insertion sort";
  }
  return "UNKNOWN";
}
int main(){
  for(int i=0; i < 6; i++) {
	int t_cat = time_category(i);
	if(t_cat == 0) {
	  printf("Algorithm %d is O(n log(n)).\n", i);
	} else if (t_cat == 1) {
	  printf("Algorithm %d is O(n^2).\n", i);
	}
	char* alg = classify(i);
	printf("Algorithm %d is %s.\n\n", i, alg);
  }
}