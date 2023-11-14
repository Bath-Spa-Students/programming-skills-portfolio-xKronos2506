#dictionary of a glossary
glossary = {"variables - ": "containers for storing data values. ",
            "lists - " : "collections of elements within a square bracket. ",
            "data - ": "classifications of items used as to store values. ",
            "string - ": "collection of usually alphabeticals under a quotation",
            "loops - ": "programming element that repeats a portion of a code to a set amount of times"}

#adding 5 more terms inside the glossary variable
glossary ['algorithm'] = 'a step-by-step instruction to perform a certain task. '
glossary ['iteration'] = 'a repetitive excecution on an instruction or code. '
glossary ['flowchart'] = 'is a graphic presentation which highlights each proccesses and actions on an algorithm. '
glossary ['boolean'] = 'a data type that represents "True" and "False", known as truth values. '
glossary ['integer'] = 'a data type that represents whole numbers, either positive, negative or zero'
#printing both key and value in the glossary
for term, meaning in glossary.items():
    print(f"{term}: {meaning}\n")