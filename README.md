# University Latex Document Generation Scripts
A set of Python scripts which accept arguments allowing for a blank customised Latex Document to be generated from the command line. These documents are used for assignments and problem sheets given through the course.

## Requirements
* [Python 3](https://www.python.org/downloads/) (utilises os, argparse, subprocess libraries)

## Example Usage

[Example Output PDFs](example_outputs)

### [new_essay_latex_doc.py](scripts/new_essay_latex_doc.py)
```
python3 new_essay_latex_doc.py -t 'Document Title' -m 'Module Name' -c 'Module Code' -d 'Due Date'
```

### [new_small_header_latex_doc.py](scripts/new_small_header_latex_doc.py)
```
python3 new_small_header_latex_doc.py -t 'Document Title' -c 'Module Code' -l 'Lecturer Name' -d 'Date Due'
```

### [new_problem_worksheet_latex_doc.py](scripts/new_problem_worksheet_latex_doc.py)
```
python3 new_problem_worksheet_latex_doc.py -t 'Document Title' -m 'Module Name' -c 'Module Code' -l 'Lecturer Name' -d 'Due Date' -dt 'Due Time'
```

