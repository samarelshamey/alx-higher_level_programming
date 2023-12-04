#include "lists.h"
/**
 * is_palindrome - cheack if list is palindrome
 *
 * @head: head
 * Return: integer
*/
int is_palindrome(listint_t **head)
{
	if (*head == NULL || head == NULL)
		return (1);
	return (palin(head, *head));
}
/**
 * palin - if is palindrome
 *
 * @head: head
 * @end: end list
 * Return: integer
*/
int palin(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (palin(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
