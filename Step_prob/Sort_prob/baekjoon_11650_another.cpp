#include <cstdio>
#include <iostream>
#include <utility>
#include <algorithm>
#include <vector>
#pragma warning(disable : 4996)

using namespace std;

bool compare(pair <int, int> &a, pair <int, int> &b) {
	if (a.first == b.first)
		return a.second < b.second;
	return a.first < b.first;
}
int main() {
	int num;
	scanf("%d", &num);

	vector< pair<int, int> > v(num);

	for (int i = 0;i < num; i++) {
		scanf("%d %d", &v[i].first, &v[i].second);
	}

	sort(v.begin(), v.end(), compare);

	for (int i = 0;i < num;i++)
		printf("%d %d\n", v[i].first, v[i].second);

	return 0;
}