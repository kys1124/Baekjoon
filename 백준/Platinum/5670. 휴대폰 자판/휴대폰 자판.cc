#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include<iostream>
#include<string>
#include<vector>
#define MAXN 100010
using namespace std;

int N;
string s;
int idx;
struct node {
	char val;
	int childcnt;
	vector<node*> child;
	bool flag;
}trie[1000010];

node* getNode(int idx) {
	return &trie[idx];
}

node* root;
string S[MAXN];

void addTrie(string s) {
	node* cur = root;
	int len = s.length();
	bool flag2 = false;
	for (int i = 0; i < len; i++) {
		flag2 = false;
		for (int j = 0; j < cur->childcnt; j++) {
			if (s[i] == cur->child[j]->val) {
				cur = cur->child[j];
				flag2 = true;
				break;
			}
		}
		if (flag2) continue;
		else {
			while (s[i]) {
				node* newNode = getNode(idx++);
				newNode->childcnt = 0;
				newNode->flag = false;
				newNode->val = s[i];
				newNode->child.clear();
				cur->childcnt++;
				cur->child.emplace_back(newNode);
				cur = newNode;
				i++;
			}
		}
	}
	if (!cur->flag)cur->flag = true;
}

int countTrie(string s) {
	node* cur = root;
	int len = s.length();
	int cnt = 1;
	if (len == 1)return 1;
	for (int j = 0; j < cur->childcnt; j++) {
		if (s[0] == cur->child[j]->val) {
			cur = cur->child[j];
			break;
		}
	}
	for (int i = 1; i < len; i++) {
		if (cur->childcnt == 1) {
			if (cur->flag)cnt++;
			cur = cur->child[0];
			continue;
		}
		for (int j = 0; j < cur->childcnt; j++) {
			if (s[i] == cur->child[j]->val) {
				cur = cur->child[j];
				cnt++;
				break;
			}
		}
	}
	return cnt;
}
int ret;
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	while (cin >> N) {
		idx = 0;
		root = getNode(idx++);
		root->val = '\0';
		root->childcnt = 0;
		root->flag = 0;
		root->child.clear();
		for (int i = 0; i < N; i++) {
			cin >> S[i];
			addTrie(S[i]);
		}
		ret = 0;
		for (int i = 0; i < N; i++) {
			ret += countTrie(S[i]);
		}
		cout << fixed;
		cout.precision(2);
		cout << (double)ret / (double)N << "\n";
	}
	return 0;
}