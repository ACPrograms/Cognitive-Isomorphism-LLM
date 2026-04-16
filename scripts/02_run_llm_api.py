# pip install google-generativeai pandas

import pandas as pd
import time
import google.generativeai as genai
import os

# Set up your NEW API Key
genai.configure(api_key="ReplaceWithYourKeyHere")

# Initialize the model 
model = genai.GenerativeModel('gemini-3-flash-preview')
print("Model initialized: Gemini 3 Flash Preview")

# Load the data
print("Loading dataset...")
df = pd.read_csv("../data/tamazight_french_3001.csv", header=None, names=["ID_Kab", "Tamazight_Kabyle", "ID_Fr", "French"])

df = df[["French", "Tamazight_Kabyle"]]
df["LLM_Translation"] = ""

print(f"Dataset loaded. Total rows: {len(df)}. Beginning API calls...")

# Iterate through the dataset
for index, row in df.iterrows():
    french_text = row['French']
    prompt_text = f"You are a linguistic translation assistant. Translate the following French sentence into the Kabyle dialect of Tamazight. Provide ONLY the translation, with no conversational filler, markdown, or explanations: '{french_text}'"
    
    success = False
    retries = 0
    max_retries = 3
    
    # The Retry Loop
    while not success and retries < max_retries:
        try:
            response = model.generate_content(
                prompt_text,
                generation_config=genai.types.GenerationConfig(temperature=0.0)
            )
            
            # Extract response and save it
            llm_output = response.text.strip()
            df.at[index, "LLM_Translation"] = llm_output
            success = True # Breaks the while loop and advances the index
            
            # Print progress
            if (index + 1) % 10 == 0:
                print(f"Processed {index + 1}/3001 sentences...")
                
            time.sleep(1)

        except Exception as e:
            retries += 1
            if str(e).find("429") != -1:
                print(f"Quota exceeded at row {index}. Waiting for 90 seconds before retrying...")
                time.sleep(90)  # Wait for 90 seconds
            else:
                print(f"API Error at row {index} (Attempt {retries}/{max_retries}): {e}")
            
            if retries < max_retries:
                print("Retrying in 60 seconds...")
                time.sleep(60)
            else:
                print("Max retries reached. Logging ERROR and skipping to next row.")
                df.at[index, "LLM_Translation"] = "ERROR"

# Export the final results
output_filename = "../data/tamazight_gemini_results.csv"
df.to_csv(output_filename, index=False)
print(f"Phase 2 Complete: Results saved to {output_filename}.")
