from Bio import SeqIO
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('header_ids', nargs='+', help='list of header IDs')
args = parser.parse_args()

# map the filename to the first command line argument provided
filename = sys.argv[1]

# read in the multi-fasta file
records = list(SeqIO.parse(filename, 'fasta'))

# define a function to retrieve the amino acid sequences for a list of header IDs
def get_aa_sequences(header_ids):
    # create an empty dictionary to store the results
    aa_sequences = {}
    for header_id in header_ids:
        for record in records:
            if record.id == header_id:
                # use the .seq attribute to retrieve the amino acid sequence directly
                aa_sequences[header_id] = str(record.seq)
                # break out of the inner loop once a match is found
                break
        else:
            # if no match is found, add a None value to the dictionary
            aa_sequences[header_id] = None
    return aa_sequences

# retrieve the amino acid sequences for header IDs of interest
header_ids = args.header_ids
aa_sequences = get_aa_sequences(header_ids)
for header_id, aa_sequence in aa_sequences.items():
    if aa_sequence is None:
        print(f'No match found for header ID "{header_id}')
    else:
        print(f'>{header_id}')
        print(aa_sequence)
