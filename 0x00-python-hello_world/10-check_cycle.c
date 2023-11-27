#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - check if list is cycle
 *
 * @list: list
 * Return: integer
*/
int check_cycle(listint_t *list)
{
	listint_t *ptr1 = list, *ptr2 = list;

	while (ptr2 && ptr2->next)
	{
		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;
		if (ptr1 == ptr2)
			return (1);
	}
	return (0);
}
