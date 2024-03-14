#include<iostream>
#include<algorithm>

#define MAXLEN 10
using namespace std;

int main(void) {

	long num;
	int arr[MAXLEN];
	cin >> num;
	int count = 0;
	for (int i = 0; i < MAXLEN; i++) {
		arr[i] = num % 10;
		count += 1;
		if ((num / 10) == 0) {
			break;
		}
		num /= 10;
	}
	sort(arr, arr + count);
	for (count; 0 < count; count--) {
		cout << arr[count-1];
	}
	return 0;

}