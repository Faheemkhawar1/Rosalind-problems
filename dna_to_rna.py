def dna_to_rna(dna_string):
    # Replace all 'T' with 'U' to transcribe the DNA to RNA
    rna_string = dna_string.replace('T', 'U')
    return rna_string


def read_dna_from_file(filename):
    with open(filename, 'r') as file:
        dna_string = file.read().strip()  # Remove any extra whitespace
    return dna_string


dna_string = read_dna_from_file('rosalind_rna.txt')

# Transcribe the DNA string to RNA
rna_string = dna_to_rna(dna_string)

print(rna_string)
