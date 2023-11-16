#include <stdio.h>

void swapp(int arr[], int x, int y)
{
	int temp;

	temp = arr[x];
	arr[x] = arr[y];
	arr[y] = temp;
}

int locOfSm(int arr[], int start, int end)
{
	int i, j;

	i = start;
	j = i;
	while (i < end)
	{
		if  (arr[i] < arr[j])
			j = i;
		i++;
	}
	return j;
}

void sel_sort(int arr[], int n)
{
	int i, j, size = n - 1;

	while (i < size)
	{
		j = locOfSm(arr, i, size);
		swapp(arr, i, j);
		i++;
	}
}

void display(int arr[], int n)
{
	int i;

	i = 0;
	while (i < n - 1)
	{
		printf("%d  ", arr[i]);
		i++;
	}
	printf("\n");
}

int main(void)
{
	int arr[] = {12, 45, 65, 90, 98, 76, 89, 7, 108, 1898, 82, 10, 87, 13};
	int size = sizeof(arr)/sizeof(int);

	display(arr, size);
	sel_sort(arr, size);
	display(arr, size);

	return 0;
}
