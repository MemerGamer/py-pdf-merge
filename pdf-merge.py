#!/bin/env python

from pypdf import PdfMerger 
import sys 

if len(sys.argv) < 1:
    print("Usage: ",sys.argv[0], "/path/to/filename.pdf path/to/filename2.pdf ...")
    exit(-1)

pdfs = sys.argv[1:]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
