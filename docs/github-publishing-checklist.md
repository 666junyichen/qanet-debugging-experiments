# GitHub Publishing Checklist

## Recommended Repository Names

Recommended:

- `qanet-debugging-experiments`
- `qanet-qa-debugging-controlled-experiments`
- `pytorch-qanet-debugging-experiments`

Best choice:

- `qanet-debugging-experiments`

Reason:

This name is short, searchable, and clear. It communicates the model family, the debugging work, and the experiment focus without exposing course, school, or personal information.

## Safe To Publish

- `README.md`
- `项目说明.md`
- `src/`
- `docs/`
- `reports/public-report-summary.md`
- `artifacts/README.md`
- `artifacts/metrics/`
- `.gitignore`

## Do Not Publish Without Extra Review

- Original PDF reports.
- `Assignment1_2026/`
- Raw datasets.
- Model checkpoints or trained weights.
- Full notebook outputs if they contain private paths, names, account identifiers, course identifiers, or institution metadata.
- Private Google Drive links.
- Files that include names, student identifiers, course codes, school names, or submission details.

## Suggested Commit Message

```text
Add anonymized QANet project documentation
```

## Suggested Repository Description

```text
An anonymized PyTorch QANet debugging and controlled-experiment project for extractive question answering.
```

## Before Uploading

Run a privacy scan for:

- Names
- Student identifiers
- Course identifiers
- Institution names
- Private links
- Local machine paths
- Raw reports and model/data artifacts
