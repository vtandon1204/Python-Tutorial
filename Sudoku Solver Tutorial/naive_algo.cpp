#include <iostream>
using namespace std;
int main()
{
    //  Naive Algorithm for Pattern Searching
    int n, m;
    bool flag;
    char txt[n], pat[m];
    cout << "enter the text size" << endl;
    cin >> n;
    cout << "enter the text" << endl;
    for (int i = 0; i < n; i++)
    {
        cin >> txt[i];
    }
    cout << "enter the pattern size" << endl;
    cin >> m;
    cout << "enter the pattern" << endl;
    for (int i = 0; i < m; i++)
    {
        cin >> pat[i];
    }

    for (int i = 0; i <= n - m; i++)
    {
        for (int j = 0; j < m; j++)
        {
            flag = true;
            if (pat[j] != txt[i + j])
            {
                flag = false;
                break;
            }
        }
        if (flag == true)
        {
            cout << "the pattern is found at index " << i << " of text array" << endl;
        }
    }
    return 0;
    // Time Complecity --> O(m*(n-m+1)) (worst case)
}
