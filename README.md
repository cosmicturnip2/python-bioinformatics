# Python Bioinformatics

A collection of Python functions for working with DNA and RNA sequences,
built while working through exercises on
[Rosalind](https://rosalind.info/).

## Modules

- `extract.py` — parse FASTA-formatted text into ID/sequence records
- `validate.py` — validate and normalise raw DNA/RNA sequences (IUPAC-aware)
- `analyse.py` — transcription, reverse complementation, base counting,
  and GC content/percentage calculations

## Usage

```python
from extract import extract_id_and_dna_from_fasta
from validate import validate_dna_sequence
from analyse import calculate_gc_percentage

fasta_text = ">Rosalind_0001\nAGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
records = extract_id_and_dna_from_fasta(fasta_text)

for record_id, raw_sequence in records.items():
    sequence = validate_dna_sequence(raw_sequence)
    if sequence:
        print(record_id, calculate_gc_percentage(sequence))
```

## Future work

- An `orchestrate.py` module to tie extraction, validation, and analysis
  into a single end-to-end pipeline.

## Style guide

Code in this repository follows [PEP 8](https://peps.python.org/pep-0008/)
and the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).

## Project structure

```
python-bioinformatics/
├── README.md
├── LICENSE
├── extract.py
├── validate.py
└── analyse.py
```

## License

MIT — see [LICENSE](LICENSE).
