"""
A module for extracting DNA and RNA sequences.
"""


# 1. Extraction Functions
def extract_id_and_dna_from_fasta(fasta_text: str) -> dict[str, str]:
    """
    Extract each ID and DNA sequence in this order from a FASTA file.

    Args:
        fasta_text (str): The raw FASTA file.

    Returns:
        records (dict[str, str]): All extracted IDs with their sequence.
    """
    records = {}
    # Split FASTA into items of ID and its sequence parts.
    raw_blocks = fasta_text.strip().split(">")
    # For each split item, get the ID and its joined sequence.
    for block in raw_blocks:
        if not block:
            continue
        lines = block.strip().splitlines()
        header_id = lines[0].strip()
        sequence = "".join(line.strip() for line in lines[1:])
        records[header_id] = sequence
    return records
