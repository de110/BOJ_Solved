#include <stdio.h>
#include <iostream>
#include <stack>

using namespace std;

int main()
{
    stack<int> stack;
    int n, cnt = 0;
    string ans;

    cin >> n;

    int seq[n];

    for (int i = 0; i < n; i++)
    {
        cin >> seq[i];
    }

    for (int i = 1; i < n + 1; i++)
    {
        stack.push(i);
        ans += '+';

        while (!stack.empty() && stack.top() == seq[cnt])
        {
            stack.pop();
            ans += '-';
            cnt++;
        }
    }
    if (!stack.empty())
        cout << "NO";
    else
    {
        for (int i = 0; i < ans.size(); i++)
            cout << ans[i] << '\n';
    }
}