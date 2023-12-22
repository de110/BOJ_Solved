#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    cin >> n;

    pair<int, int> time[100000];

    for (int i = 0; i < n; i++)
    {
        cin >> time[i].second >> time[i].first;
    }

    sort(time, time + n);

    int cnt = 0;
    int load = 0;

    for (int i = 0; i < n; i++)
    {
        if (time[i].second >= load)
        {
            load = time[i].first;
            cnt++;
        }
    }

    cout << cnt;
    return 0;
}