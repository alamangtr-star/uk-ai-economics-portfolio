# UK AI Economic Exposure Observatory — Public Portfolio

Independent applied AI economics and research engineering demonstration. This repository is deliberately separate from the unpublished research project. It contains a static website, an interactive economic simulator and a reproducible Python econometrics demonstration. No empirical results, manuscript, research datasets, private code or downloads are included. The simulator defaults are hypothetical and not calibrated to the study.

## Run locally

Open `index.html` in a browser. No installation, API key, network request or server is needed for the simulator.
## Python Econometrics Demo

A reproducible demonstration of applied economic analysis and econometric modelling using Python, pandas, NumPy and statsmodels.

### Analytical Features

- Ordinary Least Squares (OLS)
- Weighted Least Squares (WLS)
- HC3 robust standard errors
- Confidence intervals
- Leave-one-out sensitivity analysis
- Automated data validation and unit testing

### Install dependencies

```bash
python3 -m pip install -r requirements-python-demo.txt
```

### Run the econometric analysis

```bash
python3 python_econometrics_demo.py
```

### Run automated tests

```bash
python3 -m unittest -v test_python_econometrics_demo
```

All demonstration data are synthetic. No unpublished research findings, confidential datasets or private research code are included.

## Publish

Create a NEW public repository, e.g. `uk-ai-economics-portfolio`. Upload only the contents of this folder (not its parent, not the private archive). In Settings → Pages, choose Deploy from a branch, `main`, `/ (root)`, Save. Use the URL displayed by GitHub Pages. Before sharing, inspect the repository and its history for accidental disclosure. Do not connect the private Streamlit project to this public site.

## Review and attribution

Independent project, not affiliated with Anthropic. AI-assisted development; the owner should verify and take responsibility for all claims and code. Private replication materials can be made available to authorised reviewers subject to the owner's approval and any applicable university, data and journal rules. No open-source licence is granted by this repository; GitHub public repository functionality and applicable legal rights still apply.
