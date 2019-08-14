#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main()
{
	unsigned long long area;
	cin >> area;
	cout << setprecision(64) << 4*sqrt(area);
}
