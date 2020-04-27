#include "lists.h"
/**
 * check_cycle - Check if a linked list has a cycle in it.
 * @list: Value check.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
*/
int check_cycle(listint_t *list)
{
	listint_t *actual = list, *check = list;

	while (check && actual->next)
	{
		actual = actual->next;
		check = check->next->next;

		if (actual == check)
			return (1);
	}
	return (0);
}
