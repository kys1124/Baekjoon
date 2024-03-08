#include <iostream>

using namespace std;

void CAL(int a, int b);

int main(void) {
	int T;
	cin >> T;
	for (int i = 0; i< T; i++) {
		int a, b;
		cin >> a >> b;
		CAL(a, b);
	}
	return 0;
}

void CAL(int a, int b) {
	int result = 1;
	for (int i = 0; i < b;i++) {
		result *= a;
		result %= 10;
	}
	if (result == 0) {
		result = 10;
	}
	cout << result << endl;
}