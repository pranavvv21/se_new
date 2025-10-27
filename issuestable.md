

| Issue | Type | Line(s) (Original File) | Description | Fix Approach (Implemented in Final File) |
| :---- | :---- | :---- | :---- | :---- |
| **Insecure eval() used** | Security (Medium) | 59 | The eval() function was used, which is a significant security vulnerability. | Removed the eval("print('eval used')") line entirely. |
| **Use of global statement** | Bad Practice | 27 | The loadData function used the global keyword to modify stock\_data, leading to poor code structure. | Refactored the entire script into an Inventory class; stock\_data is now an instance attribute (self.stock\_data). |
| **Bare 'except' block** | Bad Practice | 19 | The removeItem function used a bare except:, which hides all errors and was flagged by Bandit. | Replaced the bare except: with a specific except KeyError: to only catch errors where the item is not in the dictionary. |
| **Dangerous default value** | Bug | 8 | The addItem function used logs=\[\] as a default argument, which is a mutable list shared across all function calls. | Changed the default argument to logs=None and added logic (if logs is None: logs \= \[\]) to create a new list inside the function. |
| **Unsafe file handling** | Bad Practice | 26, 32 | Files were opened without the with statement, risking resource leaks if an error occurred before f.close(). | Rewrote load\_data and save\_data to use the with open(...) as f: context manager, which handles closing the file automatically. |
| **Missing file encoding** | Bad Practice | 26, 32 | open() was called without specifying a text encoding, which can cause errors on different operating systems. | Added encoding="utf-8" to all open() calls to ensure consistent file handling. |
| **Unused import** | Cleanup / Style | 2 | The logging module was imported but never used. | Removed the import logging line. |
| **Missing docstrings** | Style | 1, 8, 14, 22, etc. | The module and all functions were missing docstrings. | Added a module-level docstring, a class docstring, and docstrings for all methods to explain their purpose. |
| **PEP 8 naming** | Style | 8, 14, 22, 25, etc. | Functions used camelCase (e.g., addItem, printData) instead of the standard snake\_case. | Renamed all functions/methods to snake\_case (e.g., add\_item, print\_data) to follow PEP 8 conventions. |

