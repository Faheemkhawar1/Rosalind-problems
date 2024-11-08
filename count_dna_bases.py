def count_dna_bases(filename):
    # Open the file and read the DNA sequence
    with open(filename, 'r') as file:
        dna_sequence = file.read().strip()

    # Count each DNA base
    count_a = dna_sequence.count('A')
    count_c = dna_sequence.count('C')
    count_g = dna_sequence.count('G')
    count_t = dna_sequence.count('T')

    # Print the counts as requested
    print(count_a, count_c, count_g, count_t)


count_dna_bases('rosalind_dna.txt')
