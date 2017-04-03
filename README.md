# J3 for Python

J3 is a cross-platform visualization library for high-dimensional data
developed in Java.  This Python module provides the ability to launch the
J3 application from within Python.

J3 for Python automatically downloads the latest version of J3 from Github.
The only requirements it that the computer has Java 8 installed.  J3 for
Python can handle Python DataFrames and Numpy arrays.

## Usage

```python

    from j3 import J3
    J3("input.csv")
    
    import pandas as pd
    df = pd.read_csv("input.csv")
    J3(df)
```
    