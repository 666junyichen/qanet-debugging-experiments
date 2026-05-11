# Experiment Notebook Summary

This document is a public replacement for the raw experiment notebook. The original notebook contains execution metadata, private Drive paths, account identifiers, notebook outputs, and project-specific setup text, so it should remain local-only.

## Purpose

The notebook orchestrated the end-to-end workflow for a QANet-based extractive question-answering project:

- Environment setup.
- Dataset preparation.
- SQuAD preprocessing.
- Model training.
- Checkpoint evaluation.
- Controlled experiments for dropout, learning rate, and optimizer choice.

## Workflow

### 1. Environment Setup

The notebook configured the Python runtime, installed required dependencies, and set the project path for importing local modules.

Public note:

- Do not publish cells containing private Drive mounts, local account names, Colab user metadata, or machine-specific paths.

### 2. Data Preparation

The notebook prepared a SQuAD-style extractive question-answering dataset and generated cached tensor records for training and evaluation.

Generated artifacts included:

- Train and dev `.npz` records.
- Word and character embedding matrices.
- Word and character vocabularies.
- Train/dev evaluation metadata.

Public note:

- Raw datasets and generated `_data/` files are excluded from this public repository.
- Public code keeps the preprocessing logic in `src/Tools/preproc.py`.

### 3. Training

The notebook trained a QANet model using configurable model, optimizer, scheduler, normalization, activation, initialization, and dropout settings.

Tracked metrics included:

- Training loss.
- Validation loss.
- Validation F1.
- Validation Exact Match.
- Best checkpoint step.

Public note:

- Model checkpoints are excluded from this public repository.
- Training code is published under `src/TrainTools/`.

### 4. Evaluation

The notebook evaluated saved checkpoints on the development set and wrote answer predictions for metric computation.

Published evaluation code:

- `src/EvaluateTools/evaluate.py`
- `src/EvaluateTools/eval_utils.py`

Public note:

- Raw prediction logs are excluded.
- Final cleaned metric files are published under `artifacts/metrics/`.

### 5. Controlled Experiments

The notebook compared three groups of model/training factors under a fixed training budget.

Dropout values:

- 0.10
- 0.15
- 0.20

Learning rates:

- 0.0005
- 0.001
- 0.002

Optimizers:

- Adam
- SGD

## Public Results

Best observed results from the cleaned metric summaries:

- Dropout 0.10: F1 28.4401, EM 20.3333, dev loss 5.7477.
- Learning rate 0.002: F1 28.8104, EM 22.0000, dev loss 5.5529.
- Adam vs SGD: best dev F1 29.40 vs 6.68, best dev EM 21.92 vs 1.25.

## Why The Raw Notebook Is Not Published

The raw notebook should remain local-only because it may contain:

- Private Drive mount paths.
- Colab user metadata.
- Account display names.
- Raw output dumps.
- Machine-specific filesystem paths.
- Original project setup text that is not appropriate for public release.

