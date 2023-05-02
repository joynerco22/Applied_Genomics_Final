# Applied_Genomics_Final


## BIOL 6220 Spring 2023 Final Project: Microbial Community Profiling
This repository contains my final project information stored into several directories. Please see below for a detailed list of their contents.

## bin
This folder contains scripts used during the analysis
- get_HTG_seqs.py: Script I created to retrieve amino acid sequences from an input of header IDs and their output .txt file from MetaCHIP
- humann_for_loop.sh: For loop used to automate the HumanN pipeline over 144 genomes 
- pipeline_from_gtdbtk.sh: Pipeline used to analyze and cross-check horizontally transferred genes against the BacMet, CARD and ARG databases.

## data
This folder contains input data used in the analysis. It contains one representative genome from the analysis as an example. 
## doc
This folder contains documentation on the pipelines used in the analysis and a copy of the README.md file.
## results
This folder contains output results from both HumanN 3 and the HTARGfinder pipeline. The HumanN output only reflects the representative genome included in data. 
