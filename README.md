# find_native_python

- 파이썬 소스코드를 검색하여, 네이티브 패키지를 사용하는지 여부를 검사

- 예제:

```bash
python find_native_python.py /home/sandbox/python
```

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



