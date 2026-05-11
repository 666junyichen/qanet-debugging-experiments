# Sanitized Metrics

This folder contains cleaned metric JSON files extracted from the controlled experiments.

## Contents

- `dropout/`: validation histories for dropout values 0.10, 0.15, and 0.20.
- `learning_rate/`: validation histories for learning rates 0.0005, 0.001, and 0.002.
- `optimizer/`: validation histories for Adam and SGD.
- `final_eval/`: final evaluation metrics for Adam and SGD.

## Cleaning Applied

Private local checkpoint paths were removed from the copied experiment JSON files. Numeric metrics, training histories, and experiment configurations were preserved.

## Do Not Add

- Model checkpoints.
- Raw logs.
- Private local paths.
- Account names.
- Institution or course identifiers.

