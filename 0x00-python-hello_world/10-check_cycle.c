#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - checks if a singly linked list has acycle in it
 * @list: singly linked list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *jump, *node;

	if (!list || !list->next)
		return (0);
	node = list;
	jump = list->next;

	while (jump && jump->next && node && node->next)
	{
		if (jump == node)
			return (1);
		jump = jump->next->next;
		if (!jump)

			break;
		node = node->next;
	}

	return (0);
}
