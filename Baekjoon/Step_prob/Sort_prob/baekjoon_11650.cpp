#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#pragma warning (disable : 4996)
using namespace std;

int main() {

	int num;
	int a, b;

	cin >> num;

	pair<int, int> p[100000];
	vector<pair<int, int>> v(num);

	for (int i = 0;i < num;i++) {
		cin >> v[i].first >> v[i].second;
	}

	sort(v.begin(), v.end());

	for (int i = 0;i < num;i++) {
		cout << v[i].first << " " << v[i].second << "\n";
	}
}