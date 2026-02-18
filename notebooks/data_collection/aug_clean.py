!pip install translators
import pandas as pd
from tqdm import tqdm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import translators as ts

data = pd.read_excel('Исправления.xlsx')
rus_sents = []
for i in data['Кит и олень']:
  rus_sents.append(i)
chu_sents = []
for i in data['Ръэв ынкъам ӄораӈы']:
  chu_sents.append(i)
chu_sents.append('Ръэв ынкъам ӄораӈы')
rus_sents.append('Кит и олень')

def aug_data(rus_sents, chu_sents, cut, batch_size=1000):
    rus_batch = rus_sents[cut:cut + batch_size]
    chu_batch = chu_sents[cut:cut + batch_size]
    eng_sents = []
    valid_pairs = []

    for ru, chu in tqdm(zip(rus_batch, chu_batch), total=len(rus_batch)):
        if not isinstance(ru, str):
            continue
        ru = ru.strip()
        if not ru or not any(c.isalpha() for c in ru):
            continue
        try:
            en = ts.translate_text(
                ru,
                translator='yandex',
                from_language='ru',
                to_language='en'
            )
        except Exception:
            continue
        if not isinstance(en, str) or not en.strip():
            continue
        eng_sents.append(en)
        valid_pairs.append((ru, chu))

    back_rus_sents = []
    for en in tqdm(eng_sents):
        try:
            ru_back = ts.translate_text(
                en,
                translator='yandex',
                from_language='en',
                to_language='ru'
            )
        except Exception:
            ru_back = None
        back_rus_sents.append(ru_back)

    rows = []
    for (orig_ru, chu), new_ru in zip(valid_pairs, back_rus_sents):
        if not isinstance(new_ru, str):
            continue
        new_ru = new_ru.strip()
        if not new_ru or not any(c.isalpha() for c in new_ru):
            continue
        if orig_ru == new_ru:
            continue
        vectorizer = TfidfVectorizer()
        try:
            tfidf = vectorizer.fit_transform([orig_ru, new_ru])
            sim = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
        except ValueError:
            continue
        if sim > 0.2:
            rows.append({
                "ru": new_ru,
                "chu": chu,
                "similarity": sim
            })
    df = pd.DataFrame(rows)
    out_name = f"augmented_{cut}_{cut + batch_size}.xlsx"
    df.to_excel(out_name, index=False)
    print(f"part {cut}-{cut + batch_size} complete, saved {len(df)} rows to {out_name}")

for i in [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000]:
  aug_data(rus_sents, chu_sents, i)