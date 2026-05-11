# Experiments Summary

## Experiment Design

The experiment phase used controlled comparisons on a repaired QANet system for extractive question answering. Each experiment kept the dataset, model architecture, training budget, checkpoint interval, and major training settings fixed, then changed one factor at a time.

Metrics:

- F1
- Exact Match (EM)
- Development/validation loss
- Best checkpoint step
- Convergence trend

Dataset:

- SQuAD v1.1

Training budget:

- 10,000 steps for the reported controlled comparisons
- Checkpoint evaluation every 400 steps where applicable

## Dropout

Tested values: 0.10, 0.15, 0.20

| Dropout | Best F1 | Best EM | Best Step | Dev Loss at Best F1 |
| --- | ---: | ---: | ---: | ---: |
| 0.10 | 28.4401 | 20.3333 | 10,000 | 5.7477 |
| 0.15 | 21.5187 | 14.8333 | 10,000 | 6.5681 |
| 0.20 | 6.7577 | 2.5833 | 10,000 | 9.2130 |

Finding:

Dropout 0.10 gave the strongest validation result among tested values. Higher dropout reduced effective model capacity and caused underfitting in this configuration.

## Learning Rate

Tested values: 0.0005, 0.001, 0.002

| Learning Rate | Best F1 | Best EM | Best Step | Dev Loss at Best Checkpoint |
| --- | ---: | ---: | ---: | ---: |
| 0.0005 | 26.0128 | 18.5833 | 8,800 | 5.9305 |
| 0.001 | 28.5315 | 21.8333 | 8,800 | 5.8330 |
| 0.002 | 28.8104 | 22.0000 | 10,000 | 5.5529 |

Finding:

Learning rate 0.002 achieved the best tested validation performance. The smallest tested learning rate converged more slowly under the fixed training budget.

## Optimizer

Compared optimizers: Adam and SGD

| Optimizer | Best Dev F1 | Best Dev EM | Final Eval F1 | Final Eval EM | Final Eval Loss |
| --- | ---: | ---: | ---: | ---: | ---: |
| Adam | 29.40 | 21.92 | 25.73 | 16.89 | 3.40 |
| SGD | 6.68 | 1.25 | 2.77 | 1.02 | 4.88 |

Finding:

Adam provided a much more stable and effective optimization trajectory than SGD under the same training budget and model configuration.

## Overall Conclusion

The final model behavior depended on the interaction between implementation correctness, model capacity, optimization efficiency, and training stability. The best observed settings in these controlled comparisons were dropout 0.10, learning rate 0.002, and Adam optimization.

