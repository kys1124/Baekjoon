#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<vector>
#include<cstring>
#include<algorithm>

#define MAXN 4010
#define MAXLEN 4000010

using namespace std;

struct node {
	char val;
	int childCnt;
	vector<node*>child;
	int flag;
};

node colorT[MAXLEN];
node nameT[MAXLEN];
string color[MAXN];
string name[MAXN];

node* getColorNode(int idx) {
	return &colorT[idx];
}
node* getNameNode(int idx) {
	return &nameT[idx];
}

int C, N, Q;
string team;
int colorIdx;
int nameIdx;
node* colorRoot;
node* nameRoot;

void addColor(string s, int num) {
	node* cur = colorRoot;
	int Len = s.length();
	bool flag;
	for (int i = 0; i < Len; i++) {
		flag = false;
		for (int j = 0; j < cur->childCnt; j++) {
			if (cur->child[j]->val == s[i]) {
				flag = true;
				cur = cur->child[j];
				break;
			}
		}
		if (flag)continue;
		while (s[i]) {
			node* next = getColorNode(colorIdx);
			colorIdx++;
			next->child.clear();
			next->childCnt = 0;
			next->flag = 0;
			next->val = s[i];
			cur->childCnt++;
			cur->child.emplace_back(next);
			cur = next;
			i++;
		}
	}
	if (!cur->flag)cur->flag = num;
}

void addName(string s, int num) {
	node* cur = nameRoot;
	int Len = s.length()-1;
	bool flag;
	for (int i = Len; i>=0; i--) {
		flag = false;
		for (int j = 0; j < cur->childCnt; j++) {
			if (cur->child[j]->val == s[i]) {
				flag = true;
				cur = cur->child[j];
				break;
			}
		}
		if (flag)continue;
		while (i>=0) {
			node* next = getNameNode(nameIdx);
			nameIdx++;
			next->child.clear();
			next->childCnt = 0;
			next->flag = 0;
			next->val = s[i];
			cur->childCnt++;
			cur->child.emplace_back(next);
			cur = next;
			i--;
		}
	}
	if (!cur->flag)cur->flag = num;
}
int arr1[1001];
int arr2[1001];
bool search(string s) {
	node* cur = colorRoot;
	node* nameCur = nameRoot;
	int Len = s.length();
	int idx1 = 0;
	int idx2 = 0;
	bool flag1;
	for (int i = 0; i < Len; i++) {
		flag1 = false;
		if (cur->childCnt == 0)break;
		for (int j = 0; j < cur->childCnt; j++) {
			if (cur->child[j]->val == s[i]) {
				cur = cur->child[j];
				flag1 = true;
				break;
			}
		}
		if (!flag1)break;
		if (cur->flag) arr1[idx1++] = i+1;
	}
	for (int i = 0; i <Len; i++) {
		flag1 = false;
		for (int j = 0; j < nameCur->childCnt; j++) {
			if (nameCur->child[j]->val == s[Len-i-1]) {
				nameCur = nameCur->child[j];
				flag1 = true;
				break;
			}
		}
		if (!flag1)break;
		if (nameCur->flag)arr2[idx2++] = i+1;
	}
	int sm;
	int i = 0, j = idx2-1;
	while (i<idx1 && j>=0){
		int sm = arr1[i] + arr2[j];
		if (sm > Len)j--;
		else if (sm < Len)i++;
		else return true;
	}
	return false;
}
bool ret;
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> C >> N;
	colorRoot = getColorNode(colorIdx);
	nameRoot = getNameNode(nameIdx);
	colorIdx++;
	nameIdx++;
	for (int i = 1; i <= C; i++) {
		cin >> color[i];
		addColor(color[i], i);
	}
	for (int i = 1; i <= N; i++) {
		cin >> name[i];
		addName(name[i], i);
	}
	cin >> Q;
	for (int i = 0; i < Q; i++) {
 		cin >> team;
		ret = search(team);
		if (ret)cout << "Yes" << "\n";
		else cout << "No" << "\n";
	}
	return 0;
}