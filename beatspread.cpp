#include <iostream>

int main()
{
	int x, y, a, b;
	std::cin >> x; // Discard first line
	while (std::cin >> x >> y)
	{
		a = x + y;
		b = x - y;
		if ((b >= 0) && (a % 2 == 0))
		{
			std::cout << a/2 << ' ' << b/2 << std::endl;
		}
		else
		{
			std::cout << "impossible\n";
		}
	}
}
