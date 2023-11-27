#include "lists.h"

/**
 * int check_cycle - checks cycle
 * @list: list of cycle
 * Return: 1 if found or 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if (!list)
	{
		return (0);
	}
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
		{
			return (1);
		}
	}
	return (0);
}
