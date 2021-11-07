/*
Project: CS 310 Project 3
File: make_change.c
Name: Darab Ali Qasimi
Date: Nov 14
Collaboration Declaration: assistance recieved from Pyone, Dipesh, and Sofia
*/
#include <stdio.h>
#include <limits.h>

int greedy(int val, int* coins, int n){
	int i;
	int count = 0;
	if(val == 0){
		return 0;
	}else{
		i = 0;
		while(val>0){
			if(i<n){
				if(coins[i] <= val){
					val -= coins[i];
					count += 1;
					if(!(coins[i] <= val)){
						i++;
					}
				}else{
					i++;
				}
			}else{
				break;
			}
		}
	}
	if(count == 0 || val !=0)
		return -1;
	return count;
}

int divide_and_conquer(int val, int* coins, int n, int* table) {
	int used_coins, i, j, val_coins = val;
	if(val >= 0){
	    for (i = 0; i<n; i++){
	        if (table[val] > 0){
	            return table[val];
	        }else if(val == coins[i]){
	        	table[val] = 1;
	            return 1;
	        }
	    }
	    val_coins = -1;
	    for (j=0; j<n; j++){
	        if (val >= coins[j]){
	            used_coins = divide_and_conquer(val-coins[j], coins , n, table);
	            if ((used_coins != -1 && used_coins < val_coins)|| val_coins == -1){
	                val_coins = used_coins;
	                table[val] = val_coins+1;
	            	}
	        	}
	    	}
	}else{
		return -1;
	}
    if(table[val] != -1){
        return val_coins +1;
    }else{
        return -1;
    }
}

int dyn_prog(int val, int* coins, int n, int* table, int* sol) {
	int i, decre,l; 
	if(val>= 0){
		for(i=1; i<= val; i++){
			decre = -1;
			for(l=0; l<n; l++){
				if((table[i-coins[l]] < decre || decre == -1 ) && (coins[l]<= i) && table[i-coins[l]]!=-1){
					decre = table[i-coins[l]];
					sol[i] = coins[l];
				}
			}
			if(decre!=-1){
				table[i] = decre+1;
			}
		}
	}else{
		return -1;
	}
	return table[val];
}

void print_sol(int val, int* sol) {
	int coins;
	while(val> 0){
		coins = sol[val];
		printf("Solution coins: %d \n", coins);
		val -= coins;
	}
}

int main(int argc, char** argv) {
  int n = argc - 2;
  int val;
  sscanf(argv[argc-1], "%d", &val);
  int coins[n];
  
  for(int i=0; i < n; i++) {
    sscanf(argv[i+1], "%d", &coins[i]);
  }
  printf("Making change for %d.\n", val);
  int res;
  res = greedy(val, coins, n);
  if(res != -1) {
	printf("Greedy found change using %d coins.\n", res);
  } else {
	printf("Greedy could not find change.\n");
  }
  int table[val+1];

  for(int i=0; i < val+1; i++) {
	table[i] = -1;
  }
  table[0] = 0;
  res = divide_and_conquer(val, coins, n, table);
  if(res != -1) {
	printf("Divide & conquer found change using %d coins.\n", res);
  } else {
	printf("Divide & conquer could not find change.\n");
  }
  int sol[val+1];
  for(int i=0; i < val+1; i++) {
	table[i] = -1;
	sol[i] = -1;
  }
  table[0] = 0;
  sol[0] = 0;
  res = dyn_prog(val, coins, n, table, sol);
  if(res != -1) {
	printf("Dynamic programming found change using %d coins.\n", res);
	print_sol(val, sol);
  } else {
	printf("Dynamic programming could not find change.\n");
  }
}
