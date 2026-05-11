# QANet Debugging and Controlled Experiments

## Project Overview / 项目概览

This repository documents a deep learning debugging and experiment project built around a PyTorch implementation of QANet for extractive question answering. The work focuses on turning a non-runnable training pipeline into a trainable evaluation system, then using controlled experiments to study how dropout, learning rate, and optimizer choice affect model behavior.

本仓库记录了一个基于 PyTorch QANet 的深度学习调试与实验项目，用于抽取式问答任务。项目重点是将无法正常运行的训练流程修复为可训练、可评估的实验系统，并通过控制变量实验分析 dropout、learning rate 和 optimizer 对模型表现的影响。

## Scope / 项目范围

- Debugged pipeline-level failures across environment setup, tensor flow, training, optimization, checkpoint loading, and evaluation.
- Fixed mechanism-level issues affecting gradient clipping, loss computation, optimizer math, scheduler behavior, attention/encoder components, and answer-span decoding.
- Designed controlled experiments for dropout, learning rate, and optimizer comparison under a fixed training budget.
- Summarized model behavior using F1, Exact Match (EM), validation loss, checkpoint step, and convergence trends.

- 修复环境配置、张量流、训练、优化、checkpoint 加载和评估流程中的 pipeline-level 问题。
- 修复影响梯度裁剪、loss 计算、optimizer 公式、scheduler 行为、attention/encoder 组件和答案区间解码的 mechanism-level 问题。
- 在固定训练预算下设计 dropout、learning rate 和 optimizer 对比实验。
- 使用 F1、Exact Match (EM)、validation loss、checkpoint step 和收敛趋势总结模型行为。

## Key Results / 关键结果

| Area | Result |
| --- | --- |
| Pipeline debugging | Fixed 24 pipeline-level defects and restored end-to-end training/evaluation execution. |
| Mechanism debugging | Fixed 26 mechanism-level defects across optimization stability and model-structure correctness. |
| Dropout experiment | Dropout 0.10 achieved the best validation result among tested values: F1 28.4401, EM 20.3333, dev loss 5.7477 at step 10,000. |
| Learning-rate experiment | Learning rate 0.002 achieved the best validation result among tested values: F1 28.8104, EM 22.0000, dev loss 5.5529 at step 10,000. |
| Optimizer experiment | Adam outperformed SGD: best dev F1 29.40 vs 6.68, best dev EM 21.92 vs 1.25; final evaluation F1 25.73 vs 2.77. |

## Repository Structure / 仓库结构

```text
.
+-- README.md
+-- 项目说明.md
+-- src/
|   +-- Data/
|   +-- EvaluateTools/
|   +-- Losses/
|   +-- Models/
|   +-- Optimizers/
|   +-- Schedulers/
|   +-- Tools/
|   +-- TrainTools/
|   +-- requirements.txt
+-- docs/
|   +-- README.md
|   +-- debugging-summary.md
|   +-- experiment-notebook-summary.md
|   +-- experiments-summary.md
+-- reports/
|   +-- README.md
|   +-- public-report-summary.md
+-- artifacts/
|   +-- README.md
|   +-- metrics/
+-- .gitignore
```

## Public Release Notes / 公开说明

The public materials in this repository intentionally remove names, student identifiers, course codes, school names, submission metadata, and raw private files. The original report and raw experiment assets are treated as private source material and should not be uploaded unless they are separately anonymized.

本仓库中的公开材料已刻意移除姓名、学号、课程代码、学校名称、提交信息和原始私有文件。原始报告和原始实验资产仅作为内部来源材料，不应直接上传，除非已经单独完成匿名化处理。

## Local-Only Source Material / 仅本地保留材料

The original `Assignment1_2026/` folder is intentionally ignored by Git. The publishable code has been copied and cleaned under `src/`.

原始 `Assignment1_2026/` 文件夹已被 Git 忽略，只保留在本地。适合公开的代码已复制并清理到 `src/`。
