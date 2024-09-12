#include "lists.h"
#include <stdlib.h>
/*
 * insert_node - inserts a node into a sorted singly linked list
 * @head: start node
 * @number: new node number
 * Return: updated list
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL, *itr = *head;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
	return (NULL);

	new_node->n = number;

	if (!itr || itr->n >= number)
	{
		new_node->next = itr;
		*head = new_node;
		return (*head);
	}

	while (itr && itr->next && itr->next->n < number)
	itr = itr->next;

	new_node->next = itr->next;
	itr->next = new_node;

	return (*head);
}
