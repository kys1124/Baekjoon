#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <iostream>
#include<cstring>
#include<algorithm>

using namespace std;
#define MAXN 100000

int N,Q;
int cost[MAXN];
int arr[MAXN];
string qurey;

struct segTree {
	int tree[1 << 18];
	int root;
	segTree() {};

	void init(int N) {
		root = 1;
		while (root < N)root <<= 1;
		for (int i = N+1; i <= root; i++)tree[i+root-1] = 0;
		root--;
		for (int i = 1; i <= N; i++)tree[i + root] = arr[i - 1];
		for (int i = root; i; i--) {
			tree[i] = tree[i << 1] + tree[(i << 1) | 1];
		}
	}

	void update(int idx, int val) {
		int i = idx + root;
		tree[i] = val;
		for (i >>= 1; i; i >>= 1) {
			tree[i] = tree[i << 1] + tree[(i << 1) | 1];
		}
	}
	int sum(int s, int e) {
		int res = 0;
		for (s += root, e += root; s <= e; s >>= 1, e >>= 1) {
			if (s & 1)res += tree[s++];
			if (~e & 1)res += tree[e--];
		}
		return res;
	}
};
struct  segTree2 {
	int tree[1 << 18];
	int root;
	segTree2() {};

	void init(int N) {
		root = 1;
		while (root < N)root <<= 1;
		for (int i = N + 1; i <= root; i++)tree[i + root - 1] = 10001;
		root--;
		for (int i = 1; i <= N; i++)tree[i + root] = cost[i - 1];
		for (int i = root; i; i--) {
			tree[i] = min(tree[i << 1], tree[(i << 1) | 1]);
		}
	}
	int findMin(int s, int e) {
		int res = 10001;
		for (s += root, e += root; s <= e; s >>= 1, e >>= 1) {
			if (s & 1)res = min(res, tree[s++]);
			if (~e & 1)res = min(res, tree[e--]);
		}
		return res;
	}
};
segTree T;

int search1(int x, int m) {
	int l = 1, r = x, mid;
	int mx;
	int ans=x;
	while (l <= r) {
		mid = (l + r) / 2;
		mx = T.sum(mid, x-1);
		if (mx <= m) {
			r = mid - 1;
			ans = mid;
		}
		else {
			l = mid + 1;
		}
	}
	return ans;
}

int search2(int x, int m) {
	int l = x, r = N-1, mid;
	int mx;
	int ans=x;
	while (l <= r) {
		mid = (l + r) / 2;
		mx = T.sum(x, mid);
		if (mx <= m) {
			l = mid + 1;
			ans = mid+1;
		}
		else {
			r = mid - 1;
		}
	}
	return ans;
}
segTree2 T2;
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N;
	for (int i = 0; i < N; i++)cin >> cost[i];
	for (int i = 0; i < N-1; i++)cin >> arr[i];
	T.init(N - 1);
	T2.init(N);
	
	cin >> Q;
	int x, m;
	for (int i = 0; i < Q; i++) {
		cin >> qurey >> x >> m;
		if (qurey == "CALL") {
			int left = search1(x, m);
			int right = search2(x, m);
			cout << T2.findMin(left, right)<<"\n";
		}
		else {
			T.update(x, m);
		}
	}
	return 0;
}