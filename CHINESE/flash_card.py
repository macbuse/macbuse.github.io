#! /home/macbuse/miniconda3/bin/python3.11

import os
import json
import re
import time
from deep_translator import GoogleTranslator
from pypinyin import pinyin, Style
from gtts import gTTS

os.makedirs("audio", exist_ok=True)

def clean_pinyin_for_filename(hanzi_text):
    """
    Converts Hanzi to a lowercase, tone-free, alphanumeric filename string.
    Example: '明天我要去医院' -> 'ming_tian_wo_yao_qu_yi_yuan'
    """
    # 1. Get flat Pinyin without tone marks (Style.NORMAL gives us basic 'jian', 'kang')
    raw_pinyin_list = pinyin(hanzi_text, style=Style.NORMAL)
    flat_strings = [word[0].lower() for word in raw_pinyin_list]
    
    # 2. Join words with underscores
    combined_string = "_".join(flat_strings)
    
    # 3. Sanitize out any accidental punctuation or whitespace characters
    sanitized = re.sub(r'[^a-z0-9_]', '', combined_string)
    return sanitized

def generate_card_data(hanzi_text):
    cleaned_text = hanzi_text.strip()
    
    # Generate the readable filename prefix
    filename_prefix = clean_pinyin_for_filename(cleaned_text)
    mp3_path = f"audio/{filename_prefix}.mp3"
    
    # Calculate proper accented Pinyin for display on the flashcard
    accented_pinyin_list = pinyin(cleaned_text, style=Style.TONE)
    pinyin_track = " ".join([word[0] for word in accented_pinyin_list])
    
    # Fetch Translation
    try:
        english_track = GoogleTranslator(source='zh-CN', target='en').translate(cleaned_text)
    except Exception:
        english_track = "Translation Unavailable"
        
    # Download the MP3 Asset using the new semantic filename
    try:
        tts = gTTS(text=cleaned_text, lang='zh-CN')
        tts.save(mp3_path)
        print(f"✓ Saved audio: {mp3_path}")
    except Exception as e:
        print(f"× Audio generation failed for {cleaned_text}: {e}")
    time.sleep(5)  # Be polite to the TTS service

    return {
        "hanzi": cleaned_text,
        "pinyin": pinyin_track,
        "mp3": mp3_path,
        "translation": english_track
    }
if __name__ == "__main__":
    with open('./extracted_sentences.md','r') as f:
        raw_vocabulary = f.read().splitlines()
    print(f"Loaded {len(raw_vocabulary)} raw vocabulary items from extracted_sentences.md.")

    # Limit to first 100 for testing; remove or adjust as needed
    raw_vocabulary = raw_vocabulary[:250]  
    json_filename = "data.json"
    
    # 1. Load existing data if it exists to preserve current state
    if os.path.exists(json_filename):
        try:
            with open(json_filename, "r", encoding="utf-8") as f:
                compiled_dataset = json.load(f)
        except json.JSONDecodeError:
            print("! data.json was corrupted or empty. Initializing new list.")
            compiled_dataset = []
    else:
        compiled_dataset = []

    # 2. Extract unique keys (Hanzi) already compiled to prevent duplicates
    existing_hanzi = {card["hanzi"] for card in compiled_dataset}
    
    new_cards_added = 0
    print("Starting incremental deck compilation...\n")
    
    # 3. Process incrementally
    for phrase in raw_vocabulary:
        phrase = phrase.strip()
        if not phrase:
            continue
            
        if phrase in existing_hanzi:
            print(f"• Skipping '{phrase}': already exists in dataset.")
            continue
            
        # Compile new asset node
        card_node = generate_card_data(phrase)
        compiled_dataset.append(card_node)
        existing_hanzi.add(phrase) # Track in loop memory
        new_cards_added += 1
        print(f"✓ Added '{phrase}' to dataset. Total new cards: {new_cards_added}")

    # 4. Atomically dump the expanded list back to disk
    if new_cards_added > 0:
        with open(json_filename, "w", encoding="utf-8") as f:
            json.dump(compiled_dataset, f, ensure_ascii=False, indent=2)
        print(f"\nSuccess! Appended {new_cards_added} new items to {json_filename}.")
    else:
        print("\nNo new vocabulary items to add. Dataset is up to date.")
