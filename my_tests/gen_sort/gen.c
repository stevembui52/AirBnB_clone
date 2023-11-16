#include <stdio.h>
#include <stdlib.h>

#define MAX 25

void sorting()
{
	int  n, i, j, k, l, temp;
	int arr[MAX];
	
	printf("enter numbers\n");
	scanf("%d", &n);
	for (i = 0; i < n; i++)
	{
		arr[i] =  rand() % MAX;
	}

	for (j = 0; j < n; j++)
		printf("%d  ", arr[j]);
	printf("\n");

	for (k = 0; k < n; k++)
	{
		for (l = k + 1; l < n; l++)
		{
			if (arr[l] < arr[k])
			{
				temp = arr[k];
				arr[k] = arr[l];
				arr[l] = temp;
			}
		}
	}
	for (j = 0; j < n; j++)
        printf("%d  ", arr[j]);
    printf("\n");
}

int main()
{
	sorting();
	return 0;
}
