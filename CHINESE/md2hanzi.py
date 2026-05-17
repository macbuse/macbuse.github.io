#! /home/macbuse/miniconda3/bin/python3.11
import re
import os

def extract_sentences(text):
    """
    Extracts full Mandarin sentences and generates MP3s.
    """

    # Regex breakdown:
    # [\u4e00-\u9fff] : Chinese characters
    # [\u3000-\u303f] : CJK punctuation (。，？！)
    # \s              : Whitespace
    # [^A-Za-z]       : Negative lookahead/constraint to ensure no Latin letters
    
    # We find chunks of Chinese text that may include spaces and punctuation
    # but stop when they hit an English letter.
    zh_sentence_pattern = re.compile(r'[\u4e00-\u9fff\u3000-\u303f\s]+')
    
    # Filter matches to ensure we didn't just grab "pure whitespace" 
    # and strip any trailing/leading English-style punctuation.
    raw_matches = zh_sentence_pattern.findall(text)
    clean_matches = [m.strip() for m in raw_matches if any(c in m for c in map(chr, range(0x4e00, 0x9fff)))]

    print(f"Found {len(clean_matches)} Mandarin entities.")
    return clean_matches
        

if __name__ == "__main__":
    # Example usage

    with open('./mandarin.md','r', encoding='utf-8') as f:
        md_content = f.read()
    # Filter out very short matches (like single characters)
    extracted_sentences = [_ for _ in extract_sentences(md_content) if len(_) > 1]  
    # Remove duplicates while preserving order
    extracted_sentences = list(set(extracted_sentences))  

    print(extracted_sentences[:10])
    with open('./extracted_sentences.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(extracted_sentences))
    print("Extraction complete. Check extracted_sentences.md for results.")
