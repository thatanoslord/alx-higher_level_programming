#include "lists.h"

/*
 * reverse_list - reverses a linked list
 * @head: start of list
 */

void reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;
	listint_t *curr = *head;

	while (curr)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	*head = prev;
}

/*
 * is_palindrome - check if a linked list is a palindrome
 * @head: start of linked list
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *tmp = *head, *dpl = NULL;

	if (!(*head) || !(*head)->next)
	return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dpl = slow->next;
			break;
		}
		if (!fast->next)
		{
			dpl = slow->next->next;
			break;
		}
		slow = slow->next;
	}
	reverse_list(&dpl);

	while (tmp && dpl)
	{
		if (tmp->n == dpl->n)
		{
			tmp = tmp->next;
			dpl = dpl->next;
		}
		else
		return (0);
	}

	if (!dpl)
		return (1);
	return (0);
}
