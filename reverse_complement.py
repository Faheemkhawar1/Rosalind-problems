def reverse_complement(dna_string):
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    # an empty string for the reverse complement
    reverse_complement_string = ''
    # Reverse the DNA string and take the complement of each symbol
    for base in reversed(dna_string):
        reverse_complement_string += complement_dict[base]

    return reverse_complement_string


def read_dna_from_file(filename):
    with open(filename, 'r') as file:
        dna_string = file.read().strip()  # Remove any extra whitespace
    return dna_string


dna_string = read_dna_from_file('rosalind_revc.txt')

# Get the reverse complement of the DNA string
reverse_complement_string = reverse_complement(dna_string)
print(reverse_complement_string)
