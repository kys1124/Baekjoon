#include <iostream>
#include <cstring>
#define MAXLEN 81
using namespace std;

int main(void) {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int num;
		char arr[MAXLEN];
		cin >> num >> arr;
		for (int j = 0; j<strlen(arr); j++) {
			if (j == num - 1) continue;
			else cout << arr[j];
		}
		cout << endl;
	}

	return 0;
}