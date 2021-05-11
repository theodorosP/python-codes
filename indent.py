import textwrap
sample_text ='''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''
#remove indentation  from the begining of the setence with textwrap.dedent
text_without_Indentation = textwrap.dedent(sample_text)
#place the indent you want
final_result = textwrap.indent(text_without_Indentation, '> ')
print()
print(final_result)
print()
