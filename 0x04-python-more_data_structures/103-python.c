#include <stdio.h>
#include <Python.h>
void print_python_bytes(PyObject *p)
{
	long int byteSize;
	int Indeks;
	char *byteString = NULL;

	printf("[.] Bytes pect information\n");

	if (!PyBytes_Check(p))
	{
	printf("  [ERROR] Invalid Bytes Object\n");
	return;
	}

	PyBytes_AsStringAndSize(p, &byteString, &byteSize);

	printf("  byte size: %li\n", byteSize);
	printf("  byte string: %s\n", byteString);

	if (byteSize < 10)
		printf("  first %li bytes:", byteSize + 1);
	else
		printf("  first 10 bytes:");

	for (Indeks = 0; Indeks <= byteSize && Indeks < 10; Indeks++)
		printf(" %02hhx", byteString[Indeks]);

	printf("\n");
}

void print_python_list(PyObject *p)
{
	long int listSize = PyList_Size(p);
	int Indeks;
	PyListObject *list = (PyListObject *)p;
	const char *elementType;

	printf("[*] Python list information\n");
	printf("[*] Size of the Python List = %li\n", listSize);
	printf("[*] Allocated = %li\n", list->allocated);

	for (Indeks = 0; Indeks < listSize; Indeks++)
	{
		elementType = (list->ob_item[Indeks])->ob_type->tp_name;
		printf("Element %i: %s\n", Indeks, elementType);

	if (!strcmp(elementType, "bytes"))
		print_python_bytes(list->ob_item[Indeks]);
	}
}
