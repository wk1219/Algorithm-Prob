#include <iostream>
#include <cstdio>
#include <utility>
#include <vector>
#pragma warning (disable : 4996)
using namespace std;

int main() {
	int num;
	scanf("%d", &num);

	vector< pair<int, int> > v(num);

	for (int i = 0;i < num;i++)
		scanf("%d,%d", &v[i].first, &v[i].second);

	for (int i = 0;i < num;i++) {
		printf("%d\n", v[i].first + v[i].second);
	}
	return 0;
}