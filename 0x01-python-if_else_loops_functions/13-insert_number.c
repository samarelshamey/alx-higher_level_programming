#include "lists.h"
/**
 * insert_node - insert node in sorted list
 *
 * @head: pointer to head node
 * @number: number to be inserted
 *
 * Return: integer
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = *head, *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (!ptr || new->n < ptr->n)
	{
		new->next = ptr;
		return (*head = new);
	}
	while (ptr)
	{
		if (!ptr->next || new->n < ptr->next->n)
		{
			new->next = ptr->next;
			ptr->next = new;
			return (ptr);
		}
		ptr = ptr->next;
	}
	return (NULL);
}
