#include <iostream>

using namespace std;

void decimal(int x, int b)
{
    int m = x, n; // 몫, 나머지
    string s;
    while (m != 0)
    {
        m = x / b;
        n = x % b;
        x = m;
        if (n >= 0 && n <= 9)
            s.insert(0, to_string(n));
        else
        {
            char nn = n + 55;
            s.insert(0, 1, nn);
        }
    }
    cout << s;
}

int main()
{
    int s;
    int b = 0;
    cin >> s >> b;
    decimal(s, b);
    return 0;
}