#include <iostream>
#include <cstdio>
#pragma warning (disable: 4996)
using namespace std;

int arr[10001] = { 0, };
int cnt = 0;

int main() {
	int num = 0;
	scanf("%d", &num);

	for (int i = 0; i < num; i++) {
		scanf("%d", &cnt);
		arr[cnt]++;
	}

	for (int i = 1;i <= 10000;i++) {
		for (int j = 0; j < arr[i]; j++) {
			printf("%d\n", i);
		}
	}
	return 0;
}
