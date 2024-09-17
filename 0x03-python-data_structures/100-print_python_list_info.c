#include <Python.h>
#include <object.h>
#include <listobject.h>
/*
 * print_python_list_info - prints info about a python list
 * @p: python list
 */
void print_python_list_info(PyObject *p)
{
	long int listLen = PyList_Size(p);
	int i;
	PyListObject *list = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", listLen);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < listLen; i++)
	printf("Element %d: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
}
