#include <iostream>
#include <cstdio>
#pragma warning (disable: 4996)
using namespace std;

int arr[1000000];
void swap(int* a, int* b);
void quicksort(int i, int j);

void swap(int* a, int* b) {
	int temp;
	temp = *a;
	*a = *b;
	*b = temp;
}

void quicksort(int start, int end) {
	if (start >= end) return;
	int pivot = arr[(start + end) / 2];
	int left = start;
	int right = end;

	while (left <= right) {
		while (arr[left] < pivot) left++;
		while (arr[right] > pivot) right--;
		if (left <= right) {
			swap(arr[left], arr[right]);
			left++;
			right--;
		}
	}
	quicksort(start, right);
	quicksort(left, end);
}

int main() {
	int num = 0;
	scanf("%d",&num);
	

	for (int i = 0; i < num; i++)
		scanf("%d",&arr[i]);

	
	int left = 0;
	int right = num - 1;

	quicksort(left, right);

	for (int j = 0; j < num; j++)
		printf("%d\n", arr[j]);
}



