#!/usr/bin/env python3
import sys

START_CHR=160 #First printable latin-1 character
TABLE_DELIM=" " #The delimiter for the translation table

def translate(table, data, compress=True):
	"""This function actually applies the translation table to the data."""
	out=data
	point=START_CHR
	for conv in table:
		out=out.replace(*((conv, chr(point)) if compress else (chr(point), conv)))
		point+=1
	return out

def process_python(data, code):
	"""Runs the python code on the data (either pre-processing or post-processing)."""
	x=data
	return eval(code)

def run(code, data=None):
	if not data: #Splits by blank line for one-file mode
		code, data=code.split("\n\n", 1)
	
	code=code.split("\n")
	process="x" #Default process is a no-op
	
	compress=max(map(ord, data))<127 #Encoding or decoding if on only ascii in data
	
	if len(code)==1: #only table
		table=code[0]
	elif len(code)==2: #table plus processing
		table, process=code
	else:
		raise ValueError("Too many lines in schema")
	
	if compress: #We are pre-processing if encoding
		data=process_python(data, process)

	table=table.replace("\\"+TABLE_DELIM, chr(127)) #Replace all escape delimiters
	table=table.split(TABLE_DELIM)
	table=[i.replace(chr(127), TABLE_DELIM) for i in table] #Convert escaped back
	
	out=translate(table, data, compress)
	
	if not compress: #We post-process if decoding
		out=process_python(out, process)
	
	return out

def main():
	if len(sys.argv)==1 or "--help" in sys.argv[1:] or "-h" in sys.argv[1]:
		print("""The Official Compress interpreter.

Command Line Flags:
-o or --one-file    Run in one file mode where the schema and
                    data are in one file separated by a blank line.
-h or --help        Show this help message and exit.""")

	else:
		if '-o' in sys.argv[1] or '--one-file' in sys.argv[1:]:
			with open(sys.argv[-1], encoding="latin-1") as code:
				print(run(code.read()))
		else:
			with open(sys.argv[-2], encoding="latin-1") as code, \
				 open(sys.argv[-1], encoding="latin-1") as data:
				print(run(code.read(), data.read()))

if __name__=="__main__":
	main()