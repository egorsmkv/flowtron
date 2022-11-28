import json
from text import text_to_sequence, cmudict, _clean_text, get_arpabet
from ukro_g2p.predict import G2P

ROWS_FILE = '/home/yehor/ML/flowtron/dataset_lada_trimmed/accept/metadata.jsonl'

with open(ROWS_FILE) as x:
    dataset = [json.loads(s) for s in x.readlines()]

print(dataset[:3])

g2p = G2P('ukro-base-uncased', cpu=True)

def g2p_strip(g2p, text):
    words = text.lower().split(' ')

    words_phonemes = []
    for word in words:
        word_no_accent = [it for it in word if it != '́']
        word_no_accent = [it for it in word_no_accent if it != '—']
        word_no_accent = [it for it in word_no_accent if it != '?']
        word_no_accent = [it for it in word_no_accent if it != '!']
        word_no_accent = [it for it in word_no_accent if it != ':']
        word_no_accent = [it for it in word_no_accent if it != '.']
        word_no_accent = [it for it in word_no_accent if it != ',']
        if not word_no_accent:
            continue
        phonemes = g2p(word_no_accent)

        words_phonemes.append(''.join(phonemes))
    
    return ' '.join(words_phonemes)

for s in dataset:
    g = s['orig_text']
    p = g2p_strip(g2p, g)

    print(g)
    print(p)
    print()
