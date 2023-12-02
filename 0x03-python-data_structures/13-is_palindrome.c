#include "lists.h"
#include <stdlib.h>

/**
 * palindrome - check if is palindrome with recursion
 * @ls: argument pointer
 * @rn: argument pointer
 * Return: 1 if is palindrome, 0 if  not palindrome
 */
int palindrome_is(listint_t **ls, listint_t *rn)
{
	int res;

	if (rn != NULL)
	{
		res = palindrome_is(ls, rn->next);
		if (res != 0)
		{
			res = (rn->n == (*ls)->n);
			*ls = (*ls)->next;
			return (res);
		}
		return (0);
	}
	return (1);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of node list
 * Return: 0 is success or if not
 */
int is_palindrome(listint_t **head)
{
	if (!head)
		return (0);
	return (palindrome_is(head, *head));
}
