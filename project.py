def scan_python_files(root):
    ...

def analyze_python_file(path):
    ...

def extract_imports(tree):
    ...

def generate_report(results):
    ...

def main():
    ...



'''
NUTZEN / ZWECK:
Ein CLI-Tool, das Python-Projekte untersucht: Dateien, Imports, Funktionen, Klassen und mögliche verwaiste Module erkennen.

PRINT:
$ python project.py ./src

Python files analyzed: 87
Functions found:       243
Classes found:          61
Imports found:         192

Potential issues:
- 4 imports could not be resolved locally
- 3 files have no obvious internal references
- 2 modules exceed 1000 lines

Report saved: report.json
'''
