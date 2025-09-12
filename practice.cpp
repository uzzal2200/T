#include<bits/stdc++.h>
using namespace std;

void tower(int n, char s, char d, char a)
{
    if (n == 1)
    {
        cout<<" move disc from 1 "<< s<<"to"<<d<<endl;
        return;
    }
    tower(n-1, s, a, d);
    cout<<" move disc from "<<n<<" "<<s<<"to"<<d<<endl;
    tower(n-1, a, d, s);

}
int main()
{
   int n;
   cout<<" Enter the number of discs: ";
    char s, a, d;
    cin>>n;

    cin>>s>>a>>d;

    tower(n, s,d,a);

    return 0;
}