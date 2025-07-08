import os

# ASCII codes
CYAN = '\033[96m'
BOLD = '\033[1m'
END = '\033[0m'
BOLD_GREEN = '\033[1m\033[92m'
BOLD_BLUE = '\033[1m\033[94m'

# output for each pair
def print_optimized_primers(pairs, highlight=True):
    for idx, pair in enumerate(pairs, 1):
        print()
        print("="*60)
        score = pair.get('pair_score', 0.0)
        print(f"{BOLD}OPTIMIZED PRIMER PAIR#{idx}{END} - SCORE: {score:.1f} / 100")
        print("-" * 60)
        print(
            f"Forward Primer: {pair['forward']['sequence']} (Tm: {pair['forward']['tm']}°C, GC: {pair['forward']['gc_content']}%)")
        print(
            f"Reverse Primer: {pair['reverse']['sequence']} (Tm: {pair['reverse']['tm']}°C, GC: {pair['reverse']['gc_content']}%)")
        try:
            f_start = int(pair['forward']['position'].split('-')[0])
            r_end = int(pair['reverse']['position'].split('-')[1])
            size = abs(f_start - r_end)
            if f_start is not None and r_end is not None:
                print(f"Amplicon size: {abs(f_start - r_end)} bp\n")
            else:
                print("Amplicon size: N/A\n")
        except (KeyError, ValueError, IndexError):
            print("Amplicon Size:   N/A")
        tm_diff = pair.get('tm_difference', 'N/A')
        print(f"Tm Difference:   {tm_diff}°C")
        print(f"Hetero-Dimers:   {pair.get('hetero_dimers', 'N/A')}")
        print("=" * 60)

# comparison of primer pairs to optimized genes
def visualize_amplicon(seq, f_start, f_end, r_start, r_end, wrap=60, idx=None):
    print(f"\n{CYAN}[Visualization for Optimized Pair #{idx}]{END}")
    print(f"{CYAN}Amplicon visualization (5' → 3'){END}")

    for i in range(0, len(seq), wrap):
        line = ''
        for j in range(i, min(i + wrap, len(seq))):
            base = seq[j]
            if f_start <= j < f_end:
                line += f"{BOLD_GREEN}{base}{END}"
            elif r_start <= j < r_end:
                line += f"{BOLD_BLUE}{base}{END}"
            else:
                line += base
        print(line)

    print(f"{BOLD_GREEN}← Forward Primer:{END} {f_start+1}-{f_end}")
    print(f"{BOLD_BLUE}→ Reverse Primer:{END} {r_start+1}-{r_end}")
    print(f"Amplicon size: {abs(f_start - r_end)} bp\n")

