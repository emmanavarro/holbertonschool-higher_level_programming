#include "lists.h"

/**
 * check_cycle - Detect a loped linked list
 * @list: list head
 *
 * Return: 0 false, 1 true
 */
int check_cycle(listint_t *list)
{
listint_t *actual, *check;

	actual = list;
	check = list;

	while (actual != NULL && check != NULL && check->next != NULL)
	{
		actual = actual->next;
		check = check->next->next;
		if (actual == check)
			return (1);
	}

	return (0);
}
