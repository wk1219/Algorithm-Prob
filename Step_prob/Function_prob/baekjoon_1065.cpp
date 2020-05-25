#include <cstdio>
#pragma warning(disable : 4996)
using namespace std;

int main() {
	int num;
	int cnt = 0;
	int temp;
	int han[3];

	scanf("%d", &num);

	for (int i=1;i<=num;i++){
		if (i < 100) 
			cnt = i;
		else if (i == 1000) 
			break;
		else
		{
			int k = 0;
			temp = i;
			while (temp > 0) {
				han[k] = temp % 10;
				temp /= 10;
				k++;
			}
			if (han[0] - han[1] == han[1] - han[2]) cnt++;
		} 
	}
	printf("%d\n", cnt);
}