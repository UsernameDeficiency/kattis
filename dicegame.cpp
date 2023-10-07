#include <iostream>
#include <string>
#include <array>

// Sum integers from lower_lim to upper_lim, inclusive
float natural_sum(float lower_lim, float upper_lim)
{
	int sum = 0;
	for (size_t i = lower_lim; i <= upper_lim; i++)
	{
		sum += i;
	}
	return sum;
}

// dicegame solution
int main()
{
	float throws_gunnar[4], throws_emma[4], size_gunnar[2], size_emma[2];
	for (size_t i = 0; i < 4; i++)
	{
		std::cin >> throws_gunnar[i];
	}
	for (size_t i = 0; i < 4; i++)
	{
		std::cin >> throws_emma[i];
	}
	for (size_t i = 0; i < 2; i++)
	{
		size_gunnar[i] = throws_gunnar[2*i + 1] - throws_gunnar[2*i] + 1;
		size_emma[i] = throws_emma[2*i + 1] - throws_emma[2*i] + 1;
	}
	float expected_gunnar = ((natural_sum(throws_gunnar[0], throws_gunnar[1]) / size_gunnar[0]) + 
		(natural_sum(throws_gunnar[2], throws_gunnar[3]) / size_gunnar[1])) / 2;
	float expected_emma = ((natural_sum(throws_emma [0], throws_emma [1]) / size_emma[0] ) +
		(natural_sum(throws_emma [2], throws_emma [3]) / size_emma[1] )) / 2;
	if (expected_gunnar > expected_emma)
	{
		std::cout << "Gunnar\n";
	}
	else if (expected_emma > expected_gunnar)
	{
		std::cout << "Emma\n";
	}
	else
	{
		std::cout << "Tie\n";
	}
}