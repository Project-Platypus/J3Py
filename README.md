# J3Py

**J3Py is archived and is no longer maintained.**

J3Py provided a Python interface for launching [J3](https://github.com/Project-Platypus/J3),
our 3D visualization tool.  The latest version of J3 publishes installers for Windows, Linux,
and Mac, which is our recommended way to install J3.

Using Rhodium, we can then save the output to a CSV or other supported file, which can then
be opened with J3.

```python
output = optimize(model, "NSGAII", 10000)
output.save('optimization_results.csv')
```
