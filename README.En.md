# find_native_python

> [English](README.En.md) , [Korean](README.md)

- Search Python source code to see if you are using a native package
- How to use:
   - Examines whether Python files in path `/home/sandbox/python` use native packages.

```
python find_native_python.py /home/sandbox/python
```

- 코드

```python
if __name__ == "__main__" :
    # Getting a project directory as a command line factor
    project_dir = sys.argv[1] if len(sys.argv) > 1 else "."    
    
    results = analyze_directory(project_dir)

    if results:
        print("Native code related calls found:")
        for filepath, calls in results.items():
            for func, lineno in calls:
                print(f" - {filepath}: {func} (Line {lineno})")
    else:
        print("There are no native code related calls.")
```

