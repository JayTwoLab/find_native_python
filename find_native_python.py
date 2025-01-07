
# find_native_python.py

import os
import sys
import ast

# AST Analysis Function
"""
def analyze_python_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        tree = ast.parse(file.read(), filename=filepath)
    
    findings = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            func_name = getattr(node.func, 'id', None) or getattr(node.func, 'attr', None)
            if func_name in ['CDLL', 'windll', 'cdll', 'FFI', 'system', 'Popen', 'run']:
                findings.append((func_name, node.lineno))
    return findings
"""
def analyze_python_file(filepath):
    findings = []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            tree = ast.parse(file.read(), filename=filepath)
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                func_name = getattr(node.func, 'id', None) or getattr(node.func, 'attr', None)
                if func_name in ['CDLL', 'windll', 'cdll', 'FFI', 'system', 'Popen', 'run']:
                    findings.append((func_name, node.lineno))
    except (SyntaxError, UnicodeDecodeError) as e:
        print(f"Error analyzing {filepath}: {e}")
    return findings


# Directory scanning
def analyze_directory(directory):
    results = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                findings = analyze_python_file(filepath)
                if findings:
                    results[filepath] = findings
    return results



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

