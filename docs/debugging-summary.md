# Debugging Summary

## Purpose

The debugging phase transformed a non-functional QANet-based question-answering implementation into a stable training and evaluation system. The work separated failures into two levels: pipeline-level bugs that prevented execution, and mechanism-level bugs that allowed code to run but corrupted learning behavior or evaluation reliability.

## Pipeline-Level Fixes

Total fixed defects: 24

Main categories:

- Environment and configuration: project paths, argument initialization, and scheduler configuration.
- Model forward pass and tensor flow: positional encoding shapes, embedding input order, convolution padding, tensor transposition, layer normalization broadcasting, attention masks, and pointer-network tensor operations.
- Training and optimization process: loss argument order, incorrect use of `loss.item()` for backward propagation, learning-rate update logic, and dropout scaling.
- Evaluation and checkpoint handling: checkpoint key mismatch and validation metric generation.

Impact:

- Restored end-to-end execution from configuration loading to forward pass, backward pass, optimizer update, checkpoint handling, and validation metric computation.
- Converted the original framework from non-runnable to trainable and evaluable.

## Mechanism-Level Fixes

Total fixed defects: 26

Optimization and evaluation stability: 13 defects

- Corrected checkpoint saving so the best-performing validation checkpoint is preserved.
- Made checkpoint loading compatible with multiple state-dictionary formats.
- Moved gradient clipping before optimizer updates.
- Aligned loss-function expectations with pointer-head outputs.
- Corrected Adam and SGD update formulas, weight decay direction, state-buffer keys, and learning-rate initialization.
- Fixed cosine scheduler scaling.
- Corrected answer-span decoding from batch dimension to sequence dimension.

Model structure and inference mechanisms: 13 defects

- Addressed attention calculation, encoder tensor organization, normalization, activation, initialization, and inference-related data-processing issues.
- Improved consistency between theoretical model design and implementation behavior.

## Engineering Takeaway

The project showed that successful execution is not enough for a deep learning system. Training can appear to run while hidden bugs in loss scaling, optimizer math, checkpoint selection, scheduler formulas, and decoding logic produce misleading results. The debugging work therefore focused on both runtime correctness and learning-mechanism correctness.

