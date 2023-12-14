#include <iostream>

using namespace std;

int greedy(int kg)
{
    int count = 0;

    while (kg >= 0)
    {
        if (kg % 5 == 0)
        {
            count += (kg / 5);
            cout << count << '\n';
            return 0;
        }
        else
        {
            count++;
            kg -= 3;
        }
    }
    cout << -1;
    return 0;
}

int main()
{
    int N;
    cin >> N;
    greedy(N);
    return 0;
}