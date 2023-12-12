#include <iostream>

using namespace std;

int decimal(string s, int b)
{
    int sum = 0;
    for (int i = 0; i < s.size(); i++)
    {
        if (s[i] >= '0' && s[i] <= '9')
        {
            sum = sum * b + (s[i] - '0');
        }
        else
            sum = sum * b + (s[i] - 'A' + 10);
    }
    printf("%d", sum);
    return sum;
}

int main()
{
    string s;
    int b = 0;
    cin >> s >> b;
    decimal(s, b);
}