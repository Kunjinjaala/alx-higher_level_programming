#include "lists.h"

/**
 * insert_node - Inserts a number into the sorted list.
 *
 * @head: A pointer the head of the sorted list.
 *
 * @number: The number to insert.
 *
 * Return: 0 If the function fails or pointer to the new node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new_node;
	
	new_node = malloc(sizeof(listint_t))
	if (new_node == NULL):
		return NULL

	new_node->n = number:

