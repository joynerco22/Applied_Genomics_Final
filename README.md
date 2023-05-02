# Applied_Genomics_Final


## BIOL 6220 Spring 2023 Final Project: Microbial Community Profiling
This repository contains my final project information stored into several directories. Please see below for a detailed list of their contents. Environmental microbes have vast metabolic capabilities but their interactions with anthropogenic contaminants are still understudied. Although many microbes can naturally produce antimicrobial compounds, many of their genetic machinery comes from contact with the compound in the environment and selection events. This project looked into a single sample taken from an intertidal mixing zone in Cape Shores, Delaware with the goal of quantifying gene family abundance for heavy metal and antimicrobial resistance genes. Out of curiosity, the sample was also analyzed for horizontal gene transfer using the HTARGfinder pipeline.

HTARGfinder pipeline: https://github.com/Badhan023/HTARGfinder/blob/main/README.md 
Humann3 pipeline: https://huttenhower.sph.harvard.edu/humann/ 

### bin
This folder contains scripts used during the analysis
- **get_HTG_seqs.py:** Script I created to retrieve amino acid sequences from an input of header IDs and their output .txt file from MetaCHIP
- **humann_for_loop.sh:** For loop used to automate the HumanN pipeline over 144 genomes 
- **pipeline_from_gtdbtk.sh:** Pipeline used to analyze and cross-check horizontally transferred genes against the BacMet, CARD and ARG databases.

### data
This folder contains input data used in the analysis. It contains one representative genome from the analysis as an example. 
### doc
This folder contains documentation on the pipelines used in the analysis and a copy of the README.md file.
### results
This folder contains output results from both HumanN 3 and the HTARGfinder pipeline. The HumanN output only reflects the representative genome included in data.
- H2W_SMM_FULL_Parcubacteria7_0.51_39.8.fa_results: The HumanN output containing gene family abundance files in RPK units.
- Two named files mapping the HumanN gene families to Gene Ontology and Kegg Orthology terms, respectively.
- The Unnamed gene families file
- Diamond BLAST results after searching the horizontal gene transfer results against the BacMet, ARGDB, and CARD databases, respectively.
- The DIAMOND BLAST results prior to filtering from the BacMet, ARGDB, and CARD databases, respectively. 
