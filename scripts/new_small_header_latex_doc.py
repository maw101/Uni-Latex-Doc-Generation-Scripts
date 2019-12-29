import argparse
import os
import subprocess

# SET VALUES FOR author name and ID number on lines 14, 15

content = r'''\documentclass[a4paper, 11pt]{article}
\usepackage{fullpage} %% changes the margin

\renewcommand{\baselinestretch}{0.89} %% line spacing

\begin{document}
\noindent
\large\textbf{%(doc_title)s} \hfill \textbf{} \\
\normalsize %(module_code)s \hfill Student ID:  \\
%(lecturer_name)s \hfill Due Date: %(due_date)s



\end{document}'''

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--doc_title', default='Assignment')
parser.add_argument('-c', '--module_code')
parser.add_argument('-l', '--lecturer_name')
parser.add_argument('-d', '--due_date')

args = parser.parse_args()

with open('main.tex','w') as f:
    f.write(content % args.__dict__)

cmd = ['pdflatex', '-interaction', 'nonstopmode', 'main.tex']
proc = subprocess.Popen(cmd)
proc.communicate()

retcode = proc.returncode
if not retcode == 0:
    os.unlink('main.pdf')
    raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd))) 

os.unlink('main.aux')
os.unlink('main.log')