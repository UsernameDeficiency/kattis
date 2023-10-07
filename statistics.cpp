#include <iostream>
#include <vector>
#include <string>

/* statistics solution
 * For each line of input, calculate min(X), max(X) and range(X) = max(X) - min(X) */
int main()
{
	std::string input;
	std::string lines[10];
	//size_t i = 0;
	//while (std::cin.getline(input[i++], 100))
	//{
	//	std::cout << "Writing " << i << "\n";
	//}
	int i = 0;
	while (std::getline(std::cin, input, '\n'))
	{
		lines[i++] = input;
		std::cout << "lines[" << i - 1 << "] = " << lines[i - 1] << std::endl;
	}
	//for (size_t i = 0; input[i] == 0; i++)
	//{
	//	std::cin.getline(input[i], 100);
	//	std::cout << "input[i] = " << input[i] << std::endl;
	//}
}