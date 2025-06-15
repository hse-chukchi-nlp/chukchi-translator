# Building Machine Translation for Chukchi: A Parallel Corpus and Models for an Endangered Low-Resource Language

This repository contains code, data, and models for the future research paper "Building Machine Translation for Chukchi: A Parallel Corpus and Models for an Endangered Low-Resource Language"

## Abstract

Neural machine translation systems based on encoder-decoder architectures demonstrate strong performance in large data scenarios, but are significantly less effective when applied to low-resource languages. Moreover, the majority of those languages are not supported by large pretrained NMT models, leaving them excluded from recent advances in multilingual translation. We present the first neural machine translation model for Chukchi, a low-resource and endangered language spoken in northeastern Siberia. To support this effort, we collect a new Chukchi-Russian parallel dataset by aggregating and preprocessing data from various available online resources, including Tatoeba and Universal Dependencies, resulting in 67k sentence pairs. We train and evaluate several neural machine translation architectures, experimenting with Sockeye, mBART50, NLLB-200, and instruction-tuned large language models such as Gemma-3-4b-it. Our methodology incorporates transfer learning, tokenizer extension, and synthetic data generation via back translation based on monolingual data and self-training. Evaluation using BLEU, chrF++, and human judgement shows that transfer learning and multilingual pretraining significantly improve translation quality. This work provides a benchmark for Chukchi translation and contributes practical resources for the preservation of endangered languages such as Chukchi and advancement of computational linguistics.

## Repository Structure

TBD

## Citation

TBD