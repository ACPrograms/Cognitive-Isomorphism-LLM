# Cognitive Isomorphism in Multimodal AI: Evaluating Emergent Phonological Awareness in Low-Resource Dialects

**Independent Research Project**  
**Intersection of Computational Cognitive Science & Natural Language Processing (NLP)**

## Abstract
This repository contains the methodology, scripts, and datasets for an independent evaluation of Large Language Models (LLMs). The core thesis investigates whether modern LLMs exhibit "emergent phonological awareness" when processing low-resource dialects, or if their cognitive architecture strictly relies on pattern-matching dominant, high-resource training data. 

By testing **Gemini 3 Flash Preview** on a zero-shot translation task from a high-resource language (French) to a low-resource dialect (Kabyle / Tamazight), this study quantitatively measures the model's structural and morphological failure rates.

## Methodology
To bypass the complexities of human subject testing while maintaining rigorous cognitive science methodologies, this study utilizes a programmatic API pipeline to evaluate AI cognition.

1. **Dataset Curation (`01_extract_dataset.py`)**: Extracted 3,001 parallel high-quality French-Kabyle tokens from open-source NLP repositories (Hugging Face / OPUS). 
2. **API Execution (`02_run_llm_api.py`)**: Queried the Gemini 3 Flash Preview API via Python. The model was prompted to perform deterministic, zero-shot translations (Temperature = 0.0) of 3,001 French sentences into Kabyle. Backoff logic and rate-limit handling were implemented to ensure dataset integrity.
3. **Statistical NLP Evaluation (`03_evaluate_metrics.py`)**: Evaluated the AI's outputs against the human "ground truth" dataset using standard NLP metrics to test for morphological hallucination and syntax breakdown.

## Quantitative Results
The evaluation of **3,001 valid sentences** yielded the following metrics:

* **Average BLEU Score: 0.1130**
  *(Measures word-level overlap. A score of 1.0 is perfect. 0.1130 indicates a near-total failure to predict correct Kabyle vocabulary and syntax).*
* **Average Character Error Rate (CER): 0.4940**
  *(Calculated via Levenshtein distance. A score of 0.0 is perfect. A ~49.4% error rate indicates massive structural hallucination at the character level).*

## Conclusion
The statistical data strongly supports the conclusion that the model lacks true emergent phonological awareness. In low-resource environments, its translation capabilities deteriorate into morphological hallucinations. The AI does not "understand" the structural rules of the language; rather, its cognitive architecture breaks down when deprived of massive, high-resource training density, exposing it as a statistical pattern-matcher.

## Repository Structure
* `/data`: Contains the 3,001-token parallel corpus, the raw API outputs, and the final scored dataset.
* `/scripts`: Contains the Python architecture used for data extraction, API interaction, and NLP metric evaluation (BLEU/CER).
* `/paper`: Contains the formal write-up of this research.
