#include <Python.h>

/**
 * print_python_list_info - prints basic info about Python lists
 * @p: PyObject pointer (assumed to be a Python list)
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t i, size, allocated;
    PyObject *obj;

    size = PyList_Size(p);
    allocated = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (i = 0; i < size; ++i)
    {
        obj = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
    }
}
