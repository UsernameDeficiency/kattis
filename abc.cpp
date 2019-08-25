#include <iostream>
#include <string>
#include <array>
#include "insertion_sort.h"

using namespace std;

// abc solution
int main()
{
	array<int, 3> abc;
	string order;

	for (auto& ele : abc)
	{
		cin >> ele;
	}

	cin.ignore(1, '\n');
	getline(cin, order);
	insertion_sort(abc);

	for (auto in_c: order)
	{
		if (in_c == 'A')
		{
			cout << abc[0];
		}
		else if (in_c == 'B')
		{
			cout << abc[1];
		}
		else if (in_c == 'C')
		{
			cout << abc[2];
		}
		cout << " ";
	}
}
