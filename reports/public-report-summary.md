# Public Report Summary

## Project

QANet Debugging and Controlled Experiments

## Problem

The initial QANet implementation for extractive question answering could not be reliably trained or evaluated because of pipeline-level execution bugs and mechanism-level learning bugs. The project first restored functional training and evaluation, then used controlled experiments to understand the effect of key training choices.

## Debugging Outcome

- Fixed 24 pipeline-level defects affecting configuration, tensor flow, forward execution, backward propagation, optimization, checkpoint handling, and evaluation.
- Fixed 26 mechanism-level defects affecting optimizer correctness, scheduler behavior, gradient clipping, loss computation, attention/encoder behavior, initialization, and answer-span decoding.
- Restored a broken model framework into a complete experimental system capable of training, validation, checkpointing, and metric reporting.

## Experiment Outcome

- Dropout comparison showed that 0.10 performed best among tested values, with F1 28.4401 and EM 20.3333.
- Learning-rate comparison showed that 0.002 performed best among tested values, with F1 28.8104 and EM 22.0000.
- Optimizer comparison showed that Adam substantially outperformed SGD, with best dev F1 29.40 vs 6.68 and best dev EM 21.92 vs 1.25.

## Technical Lessons

- Deep learning debugging requires checking both whether code runs and whether the learning mechanism is mathematically correct.
- Evaluation results can be misleading when checkpoint selection, decoding dimensions, or loss/output contracts are wrong.
- Controlled experiments are more interpretable after implementation-level defects are removed.

