#include <Python.h>
#include <stdio.h>

/*
 * print_python_bytes - prints info about python bytes
 * @p: python list item
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int size, limit = 10, i;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
	if (str[i] >= 0)
		printf(" %02x", str[i]);
	else
		printf(" %02x", 256 + str[i]);

	printf("\n");
}

/*
 * print_python_list - prints info about a python list
 * @p: python list
 */
void print_python_list(PyObject *p)
{
	long int listLen = ((PyVarObject *)p)->ob_size, i;
	PyListObject *list = (PyListObject *)p;
	PyObject *listItem;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", listLen);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < listLen; i++)
	{
		listItem = list->ob_item[i];
		printf("Element %ld: %s\n", i, (listItem->ob_type)->tp_name);
		if (PyBytes_Check(listItem))
			print_python_bytes(listItem);
	}
}
