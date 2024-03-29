"""
    Background

DNA is really just a sequence of molecules called nucleotides, arranged into a particular shape (a double helix). 
Every human cell has billions of nucleotides arranged in sequence. Each nucleotide of DNA contains one of four 
different bases: adenine (A), cytosine (C), guanine (G), or thymine (T). Some portions of this sequence (i.e., 
genome) are the same, or at least very similar, across almost all humans, but other portions of the sequence have 
a higher genetic diversity and thus vary more across the population.

One place where DNA tends to have high genetic diversity is in Short Tandem Repeats (STRs). An STR is a short 
sequence of DNA bases that tends to repeat consecutively numerous times at specific locations inside of a person's 
DNA. The number of times any particular STR repeats varies a lot among individuals. In the DNA samples below, for 
example, Alice has the STR AGAT repeated four times in her DNA, while Bob has the same STR repeated five times.


    Sample STRs

Using multiple STRs, rather than just one, can improve the accuracy of DNA profiling. If the probability that two 
people have the same number of repeats for a single STR is 5%, and the analyst looks at 10 different STRs, then the 
probability that two DNA samples match purely by chance is about 1 in 1 quadrillion (assuming all STRs are 
independent of each other). So if two DNA samples match in the number of repeats for each of the STRs, the analyst 
can be pretty confident they came from the same person. CODIS, the FBI's DNA database, uses 20 different STRs as 
part of its DNA profiling process.

What might such a DNA database look like? Well, in its simplest form, you could imagine formatting a DNA database 
as a CSV file, wherein each row corresponds to an individual, and each column corresponds to a particular STR.

name,AGAT,AATG,TATC
Alice,28,42,14
Bob,17,22,19
Charlie,36,18,25

The data in the above file would suggest that Alice has the sequence AGAT repeated 28 times consecutively somewhere 
in her DNA, the sequence AATG repeated 42 times, and TATC repeated 14 times. Bob, meanwhile, has those same three 
STRs repeated 17 times, 22 times, and 19 times, respectively. And Charlie has those same three STRs repeated 36, 
18, and 25 times, respectively.

So given a sequence of DNA, how might you identify to whom it belongs? Well, imagine that you looked through the 
DNA sequence for the longest consecutive sequence of repeated AGATs and found that the longest sequence was 17 
repeats long. If you then found that the longest sequence of AATG is 22 repeats long, and the longest sequence of 
TATC is 19 repeats long, that would provide pretty good evidence that the DNA was Bob's. Of course, it's also 
possible that once you take the counts for each of the STRs, it doesn't match anyone in your DNA database, in which 
case you have no match.

In practice, since analysts know on which chromosome and at which location in the DNA an STR will be found, they 
can localize their search to just a narrow section of DNA. But we'll ignore that detail for this problem.

Your task is to write a program that will take a sequence of DNA and a CSV file containing STR counts for a list of 
individuals and then output to whom the DNA (most likely) belongs.


    Specification

The program should require as its first command-line argument the name of a CSV file containing the STR counts for 
a list of individuals and should require as its second command-line argument the name of a text file containing the 
DNA sequence to identify.

    If your program is executed with the incorrect number of command-line arguments, your program should print an 
    error message of your choice (with print). If the correct number of arguments are provided, you may assume that 
    the first argument is indeed the filename of a valid CSV file and that the second argument is the filename of a 
    valid text file.

Your program should open the CSV file and read its contents into memory.

    You may assume that the first row of the CSV file will be the column names. The first column will be the word 
    name and the remaining columns will be the STR sequences themselves.

Your program should open the DNA sequence and read its contents into memory.

For each of the STRs (from the first line of the CSV file), your program should compute the longest run of 
consecutive repeats of the STR in the DNA sequence to identify. Notice that we've defined a helper function for you,
longest_match, which will do just that!

If the STR counts match exactly with any of the individuals in the CSV file, your program should print out the name 
of the matching individual.

    You may assume that the STR counts will not match more than one individual.
    If the STR counts do not match exactly with any of the individuals in the CSV file, your program should print No 
    match.
"""

import csv, sys, re


def main():
    # TODO: Check for command-line usage
    # While True loop to check for correct inputs
    while True:
        try:
            # Checks correct length of input has been taken and correct file types 
            if len(sys.argv) == 3 and re.findall(r".csv$", sys.argv[1]) and re.findall(r".txt$", sys.argv[2]):
                break
            else:
                raise Exception
        except:
            # Displays error if the correct length and file types not given and gives message
            print("Error: 1. Incorrect number of Command line arguments, or incorrect arguments given.")
            exit()


    # TODO: Read database file into a variable
    # After correct input given, the csv file is opened and read into a list varible called rows
    rows = []
    with open(sys.argv[1]) as file:
        database_reader = csv.DictReader(file)
        field_names = database_reader.fieldnames[1:]
        no_of_fieldnames = len(field_names) - 1
        data = csv.reader(file)
        for row in data:
            rows.append([row[0],row[1:]])
        file.close()
    

    # TODO: Read DNA sequence file into a variable
    # Reads txt file and saves to a variable
    with open(sys.argv[2]) as file:
        sequence_string = file.readline()
        file.close()    


    # TODO: Find longest match of each STR in DNA sequence
    # Using pre-defined function 'longest_match' below, finds the longest sequence of each fieldname from the 
    #   database that is being gathered.
    longest_sequence = []
    for sequence in field_names:
        longest_sequence.append(longest_match(sequence_string, sequence))


    # TODO: Check database for matching profiles
    # Cycles through database matching with the longest_sequence list, each time the longest_sequence and the 
    #   database match a True is added to a list, once that list is the length of the number of field_names being
    #   checked then it exits, if wrong, it empties the string and begins searching again. If no match found then
    #   returns No match
    true_list = []
    for row in rows:
        i = 0
        for items in row[1]:
            if int(items) == longest_sequence[i]:
                true_list.append(True)
                if i == no_of_fieldnames:
                    return row[0]
                i += 1
            else:
                i = 0
                true_list = []
                pass
    return "No Match"


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run

print(main())