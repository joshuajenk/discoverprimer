            ======== Primer Discovery  ========

            Created By: Joshua Jenkelowitz
            Vanderbilt University
            Produced 06/2025

Primer Discovery is a Python-based software suite developed to address the limitations of existing primer design tools in high-stakes molecular diagnostics and research workflows. It combines modular flexibility with advanced thermodynamic modeling, structural stability analysis, and integrated specificity screening to deliver high-quality primers tailored to user-defined parameters and biological targets.
Unlike traditional platforms that rely solely on template-matching algorithms or default configurations, Primer Discovery implements:

- Custom nearest-neighbor thermodynamic calculations for melting temperature (Tm) estimation, adaptable to variable salt, magnesium, and primer concentrations.
- Hairpin and dimer structure prediction using positional base-pair complementarity, with adjustable sensitivity thresholds for loop and stem lengths.
- Sequence quality scoring that balances Tm accuracy, GC content optimization, secondary structure penalties, and BLAST-derived specificity risk.
- Hydrolysis probe (TaqMan) compatibility assessment, identifying internal probe sites based on GC content, Tm range, and structural integrity.
- NCBI BLAST integration with fallback local sequence screening, ensuring robust assessment of primer specificity against both curated and local sequence libraries. 

The tool accepts curated nucleic acid sequences from Excel input tables and automatically maps short codes to full pathogen names, ensuring clean clinical interfaces without compromising internal flexibility. Each design workflow includes interpretability-rich output, including per-primer warnings for structural concerns, specificity risk scores, and QC-informed pair ranking.
