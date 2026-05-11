# Source Code

This folder contains the cleaned, public source tree for the QANet debugging and controlled-experiment project.

## Modules

- `Models/`: QANet architecture, attention, embeddings, encoder blocks, output heads, dropout, activations, initialization, and normalization layers.
- `TrainTools/`: training loop helpers, checkpoint handling, evaluation calls during training, and gradient handling.
- `EvaluateTools/`: saved-checkpoint evaluation and answer-span decoding utilities.
- `Optimizers/`: custom SGD, SGD with momentum, and Adam implementations.
- `Schedulers/`: learning-rate scheduler implementations.
- `Losses/`: question-answering loss functions.
- `Data/`: SQuAD dataset loading and cached tensor dataset utilities.
- `Tools/`: preprocessing and shared utility helpers.

## Public Data Policy

This folder contains code only. Raw datasets, generated `_data/` files, model checkpoints, logs, private paths, and notebook execution metadata are intentionally excluded from the public source tree.

