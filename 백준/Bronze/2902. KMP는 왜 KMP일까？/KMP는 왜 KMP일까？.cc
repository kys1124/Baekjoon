#include <iostream>
#include <cstring>
#define MAXLEN 101

using namespace std;

int main(void) {
	char arr[MAXLEN];
	string s;
	cin >> s;
	arr[0] = s[0];
	int index = 1;
	for (int i = 1; i < s.size(); i++) {
		if (int(s[i]) == 45) {
			arr[index] = s[i + 1];
			index += 1;
		}
	}
	for (int i = 0; i < index; i++) {
		cout << arr[i];
	}
	return 0;
}
