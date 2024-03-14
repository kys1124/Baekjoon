#include<iostream>
#include<algorithm>
#define MAXLEN 100000

using namespace std;

int main(void) {
	int N;
	cin >> N;
	
	int arr[MAXLEN];
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}

	sort(arr, arr + N);
	int M = arr[0];
	cout << M;
	for (int i=0; i<N; i++){
		if (arr[i] != M) {
			M = arr[i];
			cout << " " << M;
		}
	}
	return 0;
}