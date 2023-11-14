#dictionary of a glossary
glossary = {'variables -': 'containers for storing data values. ',
            'lists - ' : 'collections of elements within a square bracket. ',
            'data - ': 'classifications of items used as to store values. ',
            'string - ': 'collection of usually alphabeticals under a quotation. ',
            'loops - ': 'programming element that repeats a portion of a code to a set amount of times'}

#a variable to convert it into a list.
glossary_list = list(glossary.items())

#printing each dictionary, with the [] brackets as used to naviagate through the dictionary
print(glossary_list[0][0], glossary_list[0][1])
print(glossary_list[1][0], glossary_list[1][1])
print(glossary_list[2][0], glossary_list[2][1])
print(glossary_list[3][0], glossary_list[3][1])
print(glossary_list[4][0], glossary_list[4][1])