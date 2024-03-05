#include "lists.h"
#include "stddef.h"
#include "stdlib.h"

/**
 * insert_node - This parameter inserts a number
 *		into a sorted singly-linked list.
 * @head: This is the pointer to the head of the linked list.
 * @number: The number to be inserted.
 * Return: Gives 0 if the function fails or pointer to the new node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *old_node = *head, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (old_node == NULL || old_node->n >= number)
	{
		new_node->next = old_node;
		*head = new_node;
		return (new_node);
	}

	while (old_node && old_node->next && old_node->next->n < number)
		old_node = old_node->next;

	new_node->next = old_node->next;
	old_node->next = new_node;

	return (new_node);
}

