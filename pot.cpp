#include <iostream>
#include <string>
#include <math.h>

using namespace std;

int main()
{
	size_t iter{};
	unsigned long long sum{}; // Still much smaller than theoretical max. sum, it works however...
	std::string line;
	cin >> iter;
	for (size_t i = 0; i < iter; i++)
	{
		cin >> line;
		size_t exp = line.back() - '0'; // Convert ASCII digit to corresponding integer
		line.pop_back();
		sum += pow(stoi(line), exp);
	}
	cout << sum;
}
