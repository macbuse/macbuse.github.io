import re
import os
from gtts import gTTS

def extract_sentences_and_speak(text, output_dir="mandarin_audio"):
    """
    Extracts full Mandarin sentences and generates MP3s.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

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

    print(f"Found {len(clean_matches)} Mandarin sentences. Generating audio...")

    for sentence in clean_matches:
        # Use a simplified hash or first 10 chars for filename to avoid OS errors
        safe_fn = re.sub(r'[^\w\s]', '', sentence)[:10].strip().replace(' ', '_')
        filename = f"{safe_fn}.mp3"
        filepath = os.path.join(output_dir, filename)
        
        if not os.path.exists(filepath):
            try:
                # 'zh-cn' for Mandarin Chinese
                tts = gTTS(text=sentence, lang='zh-cn')
                tts.save(filepath)
                print(f"Saved: {filename} -> '{sentence}'")
            except Exception as e:
                print(f"Error saving '{sentence}': {e}")
