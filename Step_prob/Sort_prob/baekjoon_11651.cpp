#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

bool compare(const pair<int, int>& a, const pair<int, int>& b) {
	if (a.second == b.second)
		return a.first < b.first;
	return a.second < b.second;
}
int main() {
	int num = 0;
	scanf("%d", &num);
	
	vector< pair<int, int> > v(num);

	for (int i = 0;i < num;i++) {
		scanf("%d %d", &v[i].first, &v[i].second);
	}

	sort(v.begin(), v.end(), compare);

	for (int i = 0;i < num;i++) {
		printf("%d %d\n", v[i].first, v[i].second);
	}
	
	return 0;
}