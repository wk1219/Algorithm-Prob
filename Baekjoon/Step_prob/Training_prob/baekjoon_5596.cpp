#include<iostream>

int main() {
	int a1, b1, c1, d1 = 0;
	int a2, b2, c2, d2 = 0;
	int res1, res2 = 0;

	std::cin >> a1 >> b1 >> c1 >> d1;
	std::cin >> a2 >> b2 >> c2 >> d2;

	res1 = a1 + b1 + c1 + d1;
	res2 = a2 + b2 + c2 + d2;

	if (res1 < res2)
		std::cout << res2 << std::endl;
	else if (res1 >= res2)
		std::cout << res1 << std::endl;
}