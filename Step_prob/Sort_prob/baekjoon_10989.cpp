#include <iostream>
#include <cstdio>
#pragma warning (disable: 4996)
using namespace std;

int arr[10001];
int cnt[10001];
int result[10001];

int main() {
	int num = 0;
	scanf("%d", &num);

	for (int i = 0; i < num; i++)
		scanf("%d", &arr[i]);

	for (int j = 0; j < num; j++) {
		cnt[arr[j]]++;
	}
	
	for (int k = 0; k < num; k++) {
		cnt[k + 1] += cnt[k];
	}

	for (int k = 0; k < num; k++) {
		result[cnt[arr[k]]-1] = arr[k];
		cnt[arr[k]] -= 1;
	}
	for (int i = 0; i < num; i++) {
		printf("%d\n", result[i]);
	}
}



