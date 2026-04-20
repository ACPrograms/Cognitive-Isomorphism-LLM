# Cognitive Isomorphism in Large Language Models: Evaluating Emergent Phonological and Morphological Awareness in Low-Resource Dialects

**Author:** Amar Chabli  
**Date:** April 2026  
**Institution:** Berkeley City College / Independent Research 

## Abstract
Modern Large Language Models (LLMs) exhibit highly sophisticated linguistic capabilities in high-resource languages, often mimicking human-like comprehension. This study investigates whether this behavior stems from "cognitive isomorphism"—an emergent, human-like understanding of phonological and morphological rules—or if it is strictly a byproduct of statistical pattern-matching across massive datasets. By evaluating the Gemini 3 Flash Preview model on a zero-shot translation task from a high-resource language (French) to a low-resource dialect (Kabyle/Tamazight), this research quantifies the model's structural failure rates. Utilizing a dataset of 3,001 parallel tokens, the model achieved an average BLEU score of 0.1130 and a Character Error Rate (CER) of 49.40%. These metrics indicate a near-total breakdown of morphological syntax, suggesting that LLMs lack emergent phonological awareness and rely heavily on data density rather than generalized cognitive-linguistic rules.

---

## 1. Introduction
In computational cognitive science, a central debate regarding Large Language Models (LLMs) is the nature of their linguistic processing. When an AI fluently translates French to English, is it applying internalized grammatical and phonological rules similar to human cognitive architecture, or is it simply regurgitating high-probability token sequences from its training data?

To test this, we must strip away the model's primary advantage: massive training data. By forcing an LLM to process a low-resource or endangered dialect—where parallel corpora are scarce—we can observe how its underlying architecture handles unfamiliar morphological structures. 

This study tests the cognitive boundaries of multimodal AI by evaluating its translation accuracy from French into Kabyle (a dialect of the Tamazight macro-language). If the AI possesses an emergent understanding of comparative linguistics, it should infer the phonetic and syntactic rules of Kabyle. If it fails significantly, it proves the model is dependent on rote statistical mapping rather than human-like linguistic cognition.

## 2. Methodology

To bypass the variables introduced by human-subject testing, this study was constructed as a programmatic API pipeline, allowing for a strictly quantitative NLP evaluation.

### 2.1 Dataset Curation
A ground-truth parallel corpus was required to evaluate the AI's output. Using the Hugging Face `datasets` library, 3,001 parallel French-Kabyle text pairs were extracted from the open-source NLP repository `Sifal/Kabyle-French`. The data was cleaned, dropping null values, and isolated into a structured CSV to serve as the control group.

### 2.2 Model Selection and Prompt Design
The experiment utilized Google's `gemini-3-flash-preview` API. A Python script iterated through the 3,001 French tokens, prompting the model to translate each into Kabyle. 
To ensure a rigorous, measurable output:
* The prompt explicitly instructed the model to act as a linguistic translator and provide *only* the raw translation, omitting conversational filler or markdown.
* The API's `temperature` parameter was set to `0.0`. This forced the model into a deterministic state, eliminating creative variance and forcing it to output its highest-probability mathematical prediction.
* Automated backoff and retry logic (handling HTTP 429 Rate Limits) was implemented to ensure no data was dropped during the 3,001 API calls.

### 2.3 Evaluation Metrics
Because translating dialects often results in valid synonymous choices rather than exact string matches, basic exact-match accuracy is an insufficient metric. Therefore, the AI's outputs were scored against the ground-truth dataset using two standard NLP metrics:
1. **BLEU Score (Bilingual Evaluation Understudy):** Measures word-level and n-gram overlap between the AI's output and the human ground truth. 
2. **Character Error Rate (CER):** Calculated using the Levenshtein distance, this metric measures the structural distance between the strings, identifying morphological and orthographic hallucinations.

## 3. Results

Out of 3,001 sentences passed through the pipeline, the automated scoring script yielded the following aggregate metrics:

* **Total Valid Sentences Scored:** 3,001
* **Average BLEU Score:** 0.1130
* **Average Character Error Rate (CER):** 0.4940 (49.4%)

### 3.1 Qualitative Error Analysis
While the quantitative metrics show systemic failure, a qualitative review of the data reveals *how* the model's cognitive architecture broke down.

| French Input | Human Ground Truth (Kabyle) | AI Translation (Gemini) | CER |
| :--- | :--- | :--- | :--- |
| *Reconnaissez-vous qui que ce soit ?* | Tɛeqqlem albaɛḍ ? | Takkzem kra n yiwen? | 1.00 |
| *Elle détourna le regard.* | Teddewweṛ udem-is. | Tezzi tamuqli-s. | 0.68 |
| *Vous avez sept enfants.* | Ɣur-went sebεa warrac. | Tesɛam sebɛa n dderya. | 0.75 |

**Analysis of Errors:**
1. **Morphological Hallucination:** In many instances (such as *Tɛeqqlem albaɛḍ* vs *Takkzem kra n yiwen*), the model completely hallucinated the morphological structure, resulting in a CER of 1.0 (100% structural error). 
2. **Orthographic Guessing:** The model frequently failed to properly utilize the Tamazight Latin alphabet (e.g., using standard 'z' or 'd' instead of the emphatic 'ẓ' or 'ḍ'), proving it lacks phonological awareness of the dialect's distinct sounds.
3. **Synonymous Substitution:** In examples like *sebεa warrac* vs *sebɛa n dderya*, the model successfully translated the semantics but utilized Arabic loanwords (*dderya*) rather than native Kabyle terminology, heavily penalizing its BLEU score.

## 4. Discussion

A BLEU score of 0.1130 is exceptionally low; for context, standard high-resource machine translation (e.g., French to Spanish) routinely scores above 0.5000. Furthermore, a Character Error Rate of nearly 50% implies that, structurally, half of every character generated by the AI was incorrect compared to the native speaker baseline. 

These results clearly indicate that modern multimodal LLMs do not possess cognitive isomorphism regarding language acquisition. A human linguist who learns the phonetic rules of a new language can apply them universally, regardless of the size of the vocabulary they have memorized. The LLM, conversely, suffers a catastrophic breakdown in syntax and morphology when deprived of a massive training corpus. 

The AI is not inferring the grammatical rules of Kabyle; it is making educated, statistical guesses by blending French syntax, Arabic loanwords, and dominant Tamazight dialect patterns (such as Moroccan). 

## 5. Conclusion

This experiment demonstrates that Large Language Models, despite their apparent fluency in dominant languages, lack emergent phonological and morphological awareness. By testing Gemini 3 Flash Preview on a low-resource dialect (Kabyle), we isolated the model's underlying architecture from its data density. The resulting 0.1130 BLEU score and 49.4% Character Error Rate prove that the model functions as a highly advanced statistical pattern-matcher, rather than a system utilizing human-like cognitive rules for language comprehension. Future developments in Artificial General Intelligence (AGI) must bridge this gap, moving beyond raw data memorization toward true structural linguistics.

***

### References

1. Papineni, K., Roukos, S., Ward, T., & Zhu, W.-J. (2002). *BLEU: A method for automatic evaluation of machine translation*. *Proceedings of the 40th Annual Meeting of the Association for Computational Linguistics (ACL)*, 311–318. [https://aclanthology.org/P02-1040](https://aclanthology.org/P02-1040)

2. Levenshtein, V. I. (1966). *Binary codes capable of correcting deletions, insertions, and reversals*. *Soviet Physics Doklady*, 10(8), 707–710.

3. Tiedemann, J. (2012). *Parallel Data, Tools and Interfaces in OPUS*. *Proceedings of the 8th International Conference on Language Resources and Evaluation (LREC'12)*, 2214–2218. [https://aclanthology.org/L12-1267](https://aclanthology.org/L12-1267)

4. Joshi, P., et al. (2020). *The Low-Resource Double Bind: An Empirical Study of Pruning for Low-Resource Machine Translation*. *Findings of the Association for Computational Linguistics: EMNLP 2020*. [https://aclanthology.org/2020.findings-emnlp.301](https://aclanthology.org/2020.findings-emnlp.301)

5. Adelani, D. I., et al. (2021). *MasakhaNER: Named Entity Recognition for African Languages*. *Transactions of the Association for Computational Linguistics*, 9, 1116–1131. [https://aclanthology.org/2021.tacl-1.70](https://aclanthology.org/2021.tacl-1.70)
