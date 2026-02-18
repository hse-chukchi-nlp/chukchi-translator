# Building Machine Translation for Chukchi: A Parallel Corpus and Models for an Endangered Low-Resource Language

This repository contains code, data, and models for the future research paper "Building Chukchi Corpora: A Chukchi-Russian Parallel Corpus and a Monolingual Chukchi Corpus for Low-Resource NLP"

## Abstract

Many endangered and under-resourced languages lack publicly available corpora suitable for modern NLP, limiting research and downstream applications such as language documentation, morphological modeling, search, and alignment-based text study. We present a new Chukchi-Russian parallel corpus and a complementary monolingual Chukchi corpus compiled from heterogeneous online and printed resources. The parallel corpus is assembled via structured extraction, sentence-level alignment, and semantic filtering, yielding 70,636 Chukchi-Russian pairs after cleaning. The monolingual corpus contains 19,362 Chukchi sentences gathered from untranslated and unaligned materials. We describe data sources, normalization rules for Chukchi orthography, automatic and manual quality control procedures, and corpus statistics. The resulting corpora provide a practical foundation for Chukchi computational research and language preservation efforts.

## Repository Structure

```text
notebooks/
├─ data_collection/
│  ├─ krainiy_sever_website_parsing.ipynb
│  │   └─ Парсинг материалов с сайта «Крайний Север» (сбор сырых текстов/страниц).
│  ├─ krainiy_sever_database_creation.ipynb
│  │   └─ Превращение результатов парсинга в удобную базу/таблицы (структурирование корпуса).
│  ├─ Filtering_ru_ckt_corpora_with_LaBSE.ipynb
│  │   └─ Фильтрация русско-чукотских пар с помощью LaBSE (отсеивание шумных/непараллельных примеров).
│  └─ Aligning_texts_with_LaBSE.ipynb
│      └─ Выравнивание предложений/фрагментов на ru-ckt с LaBSE (поиск соответствий).
│
└─ training/
   ├─ Fine_tuning_LaBSE.ipynb
   │   └─ Дообучение LaBSE под задачу близости/сопоставления ru↔ckt (для фильтрации/поиска пар).
   ├─ Fine_tuning_NLLB_200.ipynb
   │   └─ Fine-tune NLLB-200 под перевод для ru-ckt направления.
   ├─ Fine_tuning_mBART_50_rus_ckt.ipynb
   │   └─ Fine-tune mBART-50 для перевода RU→CKT.
   ├─ Fine_tuning_mBART_50_ckt_rus.ipynb
   │   └─ Fine-tune mBART-50 для перевода CKT→RU.
   ├─ Fine_tuning_Gemma_3_rus_ckt.ipynb
   │   └─ Fine-tune Gemma 3 под перевод/инструкционную схему RU→CKT.
   ├─ Fine_tuning_Gemma_3_ckt_rus.ipynb
   │   └─ Fine-tune Gemma 3 под перевод/инструкционную схему CKT→RU.
   ├─ Fine_tuning_Sockeye_rus_ckt.ipynb
   │   └─ Эксперименты с Sockeye для RU→CKT (обучение/настройка/оценка).
   └─ fine_tune_sockeye.ipynb
       └─ Более общий/черновой ноутбук для fine-tune Sockeye.
```

## Citation

TBD