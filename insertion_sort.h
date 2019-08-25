#include <array>

// Implementing insertion sort for fun
template<typename T, size_t SIZE>
void insertion_sort(std::array<T, SIZE>& arr)
{
	for (size_t sorted_index = 1; sorted_index < SIZE; sorted_index++)
	{
		T curr = arr[sorted_index];
		// Find correct position in sub list
		for (size_t sub_index = 0; sub_index < sorted_index; sub_index++)
		{
			if (arr[sub_index] > curr)
			{
				T tmp_last = arr[sub_index];
				arr[sub_index] = curr;
				// Shift remaning elements in sub list up
				for (size_t i = sub_index + 1; i <= sorted_index; i++)
				{
					T tmp_next = arr[i];
					arr[i] = tmp_last;
					tmp_last = tmp_next;
				}
				break; // Sub list sorting done
			}
		}
	}
}

