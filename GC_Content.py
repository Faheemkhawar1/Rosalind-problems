def gc_content(dna_sequence):
    """Calculate GC-content of a DNA string."""
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    return (gc_count / len(dna_sequence)) * 100


def read_fasta(file_name):
    """Read a FASTA file and store the sequences."""
    sequences = {}
    current_id = ""
    current_sequence = []

    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()  # Remove any extra spaces or newlines
            if line.startswith('>'):  # header line
                if current_id:
                    sequences[current_id] = ''.join(
                        current_sequence)  # Save the previous sequence
                current_id = line[1:]  # Get the ID (remove '>')
                current_sequence = []  # Reset the sequence for the next DNA string
            else:
                current_sequence.append(line)  # Add the sequence lines
        # Save the last sequence
        if current_id:
            sequences[current_id] = ''.join(current_sequence)

    return sequences


def find_highest_gc_content(file_name):
    """Find the sequence with the highest GC-content from the FASTA file."""
    sequences = read_fasta(file_name)

    max_gc = 0  # Initialize the maximum GC-content
    max_id = ""  # Initialize the ID of the sequence with the highest GC-content

    for seq_id, dna in sequences.items():
        gc = gc_content(dna)  # Calculate GC-content for each sequence
        if gc > max_gc:
            max_gc = gc
            max_id = seq_id

    # Print the result
    print(f"{max_id}\n{max_gc:.6f}")


find_highest_gc_content("rosalind_gc.txt")
