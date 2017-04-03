# J3Py

J3 is a cross-platform visualization library for high-dimensional data
developed in Java.  This Python module provides the ability to launch the
J3 application from within Python by either loading a file (e.g., CSV) or
viewing an existing Pandas DataFrame or Numpy array.  **Requires Java 8+.**

```python

    from j3 import J3
    
    # launch J3 with an empty canvas
    J3()
    
    # launch J3 and load the CSV file
    J3("input.csv")
    
    # launch J3 and load a Pandas DataFrame
    import pandas as pd
    df = pd.read_csv("input.csv")
    J3(df)
```

In addition to launching J3, this module also handles downloading and installing
J3 (to the `~/.j3` folder) to ensure the user is running the latest version.
