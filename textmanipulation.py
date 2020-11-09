#!/usr/bin/env python
# Use 'chmod +x textmanipulation.py' to give it execution privileges if 
# double clicked in the file manager.

# Import the system, regular expressions and text extraction libraries. 
# The textract library can be installed by using 'pip install textract'. 
# More info can be found on https://pypi.python.org/pypi/textract/

import sys 
# Import the regular expression library. 
import re 
# Import the text extraction library.
import textract
# import the dateutil library -- broken atm. 
# import dateutil

# The following lines lines make the UTF-8 encoding work. 
# Reload the system library. For some reason it doesn't work without this.
reload(sys)
# Set the default encoding to UTF-8.
sys.setdefaultencoding('utf8') 

# Ask for the path to the file they want to process. 
print 'Enter the name of the text file you want to process'

# Get the raw keyboard input and save it in the 'filename' variable. 
filename = raw_input() 

# Open the source file and extract its contents in the string named 'dirty_input'.
dirty_input = textract.process(filename) 

# Turn the 'dirty_input' into 'clean_input', basically removing every bit of unnecessary space. 
clean_input = re.sub('\s+', ' ', dirty_input).strip() 

# Regular expression used at splitting the source text. Detailed explanation on the bottom of the file.
sentences = re.compile(ur'(?u)(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', re.MULTILINE) 

# Replace the whitespaces with new lines. 
subst = u"\n" 

# Alter the contents of 'clean_input' by the rules of the 'sentences' 
# (a.k.a. regular expression). 
result = re.sub(sentences, subst, clean_input) 

print 'The processed text is below: \n--------------------------------------------------------------------\n'

#Print the processed text.
print result 

"""
The regular expression used to separate sentences is the following:
(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s

(?<!\w\.\w.) Negative lookbehind - asserts that it is impossible to match the regex below:
\w - match any word character
\. - matches the '.' character
\w - matches any word character
. - matches any character with the exception of newline

(?<![A-Z][a-z]\.) Negative lookbehind - asserts that it is impossible to match the regex below:
[A-Z] - match a single character present in the range between 'A' and 'Z' (case sensitive)
[a-z] - match a single character present in teh range between 'a' and 'z' (case sensitive)
\. - matches the '.' character

(?<=\.|\?)\s Positive lookbehind - asserts that the regex beelow can be matched:
\. - matches the '.' character
\? - matches the '?' character
\s - matches the whitespace character
""" 
