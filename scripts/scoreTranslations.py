# 1. Install required evaluation libraries:
# pip install pandas nltk Levenshtein

import pandas as pd
import Levenshtein
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
import re

print("Loading API results...")
# Load the dataset generated in Phase 2
df = pd.read_csv("tamazight_gemini_results.csv")

# Drop any rows where the API completely failed or returned empty
df = df.dropna(subset=['Tamazight_Kabyle', 'LLM_Translation'])
df = df[df['LLM_Translation'] != "ERROR"]

def clean_text(text):
    """Normalizes text by making it lowercase and stripping punctuation."""
    text = str(text).lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

bleu_scores = []
cer_scores = []
smoothie = SmoothingFunction().method1 # Prevents zero-scores on short sentences

print("Calculating NLP metrics...")

for index, row in df.iterrows():
    # Clean both strings
    ref = clean_text(row['Tamazight_Kabyle'])
    hyp = clean_text(row['LLM_Translation'])
    
    # 1. Calculate BLEU Score
    ref_tokens = [ref.split()]
    hyp_tokens = hyp.split()
    
    if len(hyp_tokens) > 0 and len(ref_tokens[0]) > 0:
        bleu = sentence_bleu(ref_tokens, hyp_tokens, smoothing_function=smoothie)
    else:
        bleu = 0.0
    bleu_scores.append(bleu)
    
    # 2. Calculate Character Error Rate (CER)
    if len(ref) > 0:
        cer = Levenshtein.distance(ref, hyp) / len(ref)
    else:
        cer = 1.0
    cer_scores.append(cer)

# Append scores to dataframe
df['BLEU_Score'] = bleu_scores
df['CER'] = cer_scores

# Calculate Aggregates
avg_bleu = sum(bleu_scores) / len(bleu_scores)
avg_cer = sum(cer_scores) / len(cer_scores)

print("\n=== FINAL RESEARCH METRICS ===")
print(f"Total Valid Sentences Scored: {len(df)}")
print(f"Average BLEU Score: {avg_bleu:.4f} (Higher is better, 1.0 is perfect overlap)")
print(f"Average Character Error Rate (CER): {avg_cer:.4f} (Lower is better, 0.0 is zero errors)")
print("==============================\n")

# Export for the final paper
output_filename = "tamazight_final_scored.csv"
df.to_csv(output_filename, index=False)
print(f"Phase 3 Complete: Scored dataset saved to {output_filename}.")