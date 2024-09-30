#include <Python.h>
#include <stdio.h>

/*
 * print_python_float - prints info about python float object
 * @p: python object pointer
 */

void print_python_float(PyObject *p)
{
	double val = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
		{
		printf("  [ERROR] Invalid Float Object\n");
		return;
		}
	val = ((PyFloatObject *)p)->ob_fval;
	str = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
	PyMem_Free(str);
}

/*
 * print_python_bytes - prints info about python bytes
 * @p: python list item
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	Py_ssize_t size, limit = 10, i;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", str);

	if (size >= 10)
	limit = 10;
	else
	limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
	printf(" %02hhx", str[i]);

	printf("\n");
}

/*
 * print_python_list - prints info about a python list
 * @p: python list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t listLen, i;
	PyListObject *list = (PyListObject *)p;
	PyObject *listItem;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		listLen = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", listLen);
		printf("[*] Allocated = %lu\n", list->allocated);
		for (i = 0; i < listLen; i++)
		{
			listItem = PyList_GET_ITEM(p, i);
			printf("Element %ld: %s\n", i, (listItem->ob_type)->tp_name);
			if (PyBytes_Check(listItem))
				print_python_bytes(listItem);
			else if (PyFloat_Check(listItem))
				print_python_float(listItem);
		}
	}
	else
	printf("  [ERROR] Invalid List Object\n");
}
