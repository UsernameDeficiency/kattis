#include <iostream>
#include <string>

int main()
{
	std::string people{};
	std::string pieces{};

	std::cin >> people >> pieces;

	int diff = std::stoi(pieces) - std::stoi(people);
	if (diff > 1)
	{
		std::cout << "Dr. Chaz will have " << diff << " pieces of chicken left over!";
	}
	else if (diff == 1)
	{
		std::cout << "Dr. Chaz will have 1 piece of chicken left over!";
	}
	else if (diff == -1)
	{
		std::cout << "Dr. Chaz needs 1 more piece of chicken!";
	}
	else
	{
		std::cout << "Dr. Chaz needs " << -diff << " more pieces of chicken!";
	}
}
