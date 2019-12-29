import argparse
import os
import subprocess

# SET VALUES FOR author name, email and ID number on lines 60, 61, 62

content = r'''\documentclass[a4paper,11pt]{article}

\usepackage{fancyhdr}
\usepackage{extramarks}
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{amsfonts}
\usepackage{tikz}
\usepackage{booktabs}
\usepackage{multirow}
\usepackage{ltablex}
\usepackage{lscape}
\usepackage[section]{placeins}
\usetikzlibrary{automata,positioning}
\usepackage{float}

%%
%% Basic Document Settings
%%
\topmargin=-0.15in
\evensidemargin=0in
\oddsidemargin=0in
\textwidth=6.5in
\textheight=9.0in
\headsep=0.25in

\linespread{1.1}
\pagestyle{fancy}
%%\lhead{\hmwkAuthorName}
%%\rhead{\hmwkModuleCode\ - \hmwkTitle}
\cfoot{\thepage}

\renewcommand\headrulewidth{0.4pt}
\renewcommand\footrulewidth{0.4pt}

\setlength\parindent{0pt}


%%
%% Homework Details
%%   - Module Name 			(hmwkModuleName)
%%   - Module Code			(hmwkModuleCode)
%%   - Homework Title 		(hmwkTitle)
%%   - Due Date				(hmwkDueDate)
%%   - Author				(hmwkAuthorName)
%%   - Author Uni ID # 		(hmwkAuthorIDNumber)
%%

\newcommand{\hmwkModuleName}{%(module_name)s}
\newcommand{\hmwkModuleCode}{%(module_code)s}
\newcommand{\hmwkTitle}{%(homework_title)s}

\newcommand{\hmwkDueDate}{%(due_date)s}
\newcommand{\hmwkAuthorName}{}
\newcommand{\hmwkAuthorEmail}{}
\newcommand{\hmwkAuthorIDNumber}{}


%%
%% Title Page
%%
\title{
	\vspace{2in}
	\textmd{\textbf{\hmwkModuleName\ (\hmwkModuleCode)}}\\
	\textmd{\textbf{\hmwkTitle}}\\
	\normalsize\vspace{0.1in}\small{\hmwkDueDate}\\
	\vspace{3in}
}

\author{\hmwkAuthorName\ \\ \hmwkAuthorEmail \\(\hmwkAuthorIDNumber)}
\date{}

\begin{document}
\maketitle
\pagebreak

\tableofcontents

\pagebreak



\end{document}'''

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--homework_title', default='Assignment')
parser.add_argument('-m', '--module_name')
parser.add_argument('-c', '--module_code')
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
os.unlink('main.toc') # table of contents file