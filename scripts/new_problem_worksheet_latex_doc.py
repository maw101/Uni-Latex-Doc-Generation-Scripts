import argparse
import os
import subprocess

# SET VALUES FOR author name and ID number on lines 99, 100

content = r'''\documentclass[a4paper]{article}

\usepackage{fancyhdr}
\usepackage{extramarks}
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{amsfonts}
\usepackage{tikz}
%%\usepackage[plain]{algorithm}
%%\usepackage{algpseudocode}
\usetikzlibrary{automata,positioning}

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
\lhead{\hmwkAuthorName}
\chead{\hmwkModuleCode\ - \hmwkTitle}
\rhead{\firstxmark}
\lfoot{\lastxmark}
\cfoot{\thepage}

\renewcommand\headrulewidth{0.4pt}
\renewcommand\footrulewidth{0.4pt}

\setlength\parindent{0pt}

%%
%% Create Problem Sections
%%
\newcommand{\enterProblemHeader}[1]{
    \nobreak\extramarks{}{Problem \arabic{#1} continued on next page\ldots}\nobreak{}
    \nobreak\extramarks{Problem \arabic{#1} (continued)}{Problem \arabic{#1} continued on next page\ldots}\nobreak{}
}

\newcommand{\exitProblemHeader}[1]{
    \nobreak\extramarks{Problem \arabic{#1} (continued)}{Problem \arabic{#1} continued on next page\ldots}\nobreak{}
    \stepcounter{#1}
    \nobreak\extramarks{Problem \arabic{#1}}{}\nobreak{}
}

\setcounter{secnumdepth}{0}
\newcounter{partCounter}
\newcounter{homeworkProblemCounter}
\setcounter{homeworkProblemCounter}{1}
\nobreak\extramarks{Problem \arabic{homeworkProblemCounter}}{}\nobreak{}

%%
%% Homework Problem Environment
%%
%% This environment takes an optional argument. When given, it will adjust the
%% problem counter. This is useful for when the problems given for your
%% assignment aren't sequential. See the last 3 problems of this template for an
%% example.
%%
\newenvironment{homeworkProblem}[1][-1]{
    \ifnum#1>0
        \setcounter{homeworkProblemCounter}{#1}
    \fi
    \section{Problem \arabic{homeworkProblemCounter}}
    \setcounter{partCounter}{1}
    \enterProblemHeader{homeworkProblemCounter}
}{
    \exitProblemHeader{homeworkProblemCounter}
}

%%
%% Homework Details
%%   - Module Name 			(hmwkModuleName)
%%   - Module Code			(hmwkModuleCode)
%%   - Lecturer				(hmwkModuleLecturer)
%%   - Homework Title 		(hmwkTitle)
%%   - Due date				(hmwkDueDate)
%%   - Due time				(hmwkDueTime)
%%   - Author				(hmwkAuthorName)
%%   - Author Uni ID # 		(hmwkAuthorIDNumber)
%%

\newcommand{\hmwkModuleName}{%(module_name)s}
\newcommand{\hmwkModuleCode}{%(module_code)s}
\newcommand{\hmwkModuleLecturer}{%(lecturer_name)s}
\newcommand{\hmwkTitle}{%(homework_title)s}
\newcommand{\hmwkDueDate}{%(due_date)s}
\newcommand{\hmwkDueTime}{%(due_time)s}
\newcommand{\hmwkAuthorName}{}
\newcommand{\hmwkAuthorIDNumber}{}

%%
%% Title Page
%%
\title{
	\vspace{2in}
	\textmd{\textbf{\hmwkModuleName\ (\hmwkModuleCode)}}\\
	\textmd{\textbf{\hmwkTitle}}\\
	\normalsize\vspace{0.1in}\small{Due\ on\ \hmwkDueDate\ at \hmwkDueTime}\\
	\vspace{0.1in}\large{\textit{\hmwkModuleLecturer}}
	\vspace{3in}
}

\author{\hmwkAuthorName\ \\(\hmwkAuthorIDNumber)}
\date{}
\renewcommand{\part}[1]{\textbf{\large Part \Alph{partCounter}}\stepcounter{partCounter}\\}

%%
%% Various Helper Commands
%%

%% Useful for algorithms
\newcommand{\alg}[1]{\textsc{\bfseries \footnotesize #1}}
%% Alias for the Solution section header
\newcommand{\solution}{\textbf{\large Solution}}

\begin{document}
\maketitle
\pagebreak


%% DELETE ONCE DOCUMENT COMPLETE:



%% TEMPLATE FOR three level bullet point:
%%\begin{enumerate}
%%	\item
%%	\begin{enumerate}
%%		\item
%%		\begin{enumerate}
%%			\item text
%%		\end{enumerate}
%%	\end{enumerate}
%%\end{enumerate}

%% TEMPLATE FOR table
%%\begin{table}[ht]
%%	\centering
%%	\begin{tabular}{c || c | c | c | c | c}
%%		& \(x \mod 5 = 0\)
%%		& \(x \mod 5 = 1\)
%%		& \(x \mod 5 = 2\)
%%		& \(x \mod 5 = 3\)
%%		& \(x \mod 5 = 4\)
%%		\\
%%		\hline
%%		\(x0\) & 0 & 2 & 4 & 1 & 3 \\
%%		\(x1\) & 1 & 3 & 0 & 2 & 4 \\
%%	\end{tabular}
%%\end{table}

%% TEMPLATE FOR psuedo-code
%%Write part of \alg{Quick-Sort($list, start, end$)}
%%    \begin{algorithm}[]
%%        \begin{algorithmic}[1]
%%            \Function{Quick-Sort}{$list, start, end$}
%%                \If{$start \geq end$}
%%                    \State{} \Return{}
%%                \EndIf{}
%%                \State{} $mid \gets \Call{Partition}{list, start, end}$
%%                \State{} \Call{Quick-Sort}{$list, start, mid - 1$}
%%                \State{} \Call{Quick-Sort}{$list, mid + 1, end$}
%%            \EndFunction{}
%%        \end{algorithmic}
%%        \caption{Start of QuickSort}
%%    \end{algorithm}

%% TEMPLATE FOR Maths snippet
%%\[
%%\begin{split}
%%n^2 + n + 1 &=
%%\\
%%&\leq n^2 + n^2 + n^2
%%\\
%%&= 3n^2
%%\\
%%&\leq c \cdot 2n^3
%%\end{split}
%%\]

%% NEW LINE: \\
%% BOLDFACE TEXT: \textbf{text here}
%% ITALICS: \(text\)
%% SUBSECTION: \subsection{Part A}
%% TEMPLATE FOR NUMBERED LIST: \begin{enumerate} \item Item Text \end{enumerate}



%% END DELETE


\begin{homeworkProblem}
	
	\textbf{HEADING}
	\\
    Text

\end{homeworkProblem}
\pagebreak



\end{document}'''

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--homework_title', default='Assignment')
parser.add_argument('-m', '--module_name')
parser.add_argument('-c', '--module_code')
parser.add_argument('-l', '--lecturer_name')
parser.add_argument('-d', '--due_date')
parser.add_argument('-dt', '--due_time', default='')

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