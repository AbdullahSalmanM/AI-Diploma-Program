#!/usr/bin/env python3
"""Upgrade placeholder notebooks created by create_all_missing_notebooks.py.

Goals:
- Replace placeholder content ("Topic: AI Application" / "✅ Ready to implement!") with runnable, topic-specific examples.
- Ensure notebook cell `source` lines include newlines so Jupyter renders correctly.
- Only mutate notebooks that are confirmed placeholders.

This is a best-effort upgrader: it prioritizes **working code** with lightweight, local data.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Callable, Dict, List, Tuple

WORKSPACE = Path('.')
PLACEHOLDER_MARKERS = (
    'Topic: AI Application',
    '✅ Ready to implement!',
)


def _lines_with_newlines(text: str) -> List[str]:
    lines = text.splitlines()
    # Preserve empty file edge cases
    if not lines:
        return ['\n']
    return [ln + '\n' for ln in lines]


def _mk_notebook(md: str, code_cells: List[str]) -> dict:
    cells = [
        {
            'cell_type': 'markdown',
            'metadata': {},
            'source': _lines_with_newlines(md),
        }
    ]
    for code in code_cells:
        cells.append(
            {
                'cell_type': 'code',
                'execution_count': None,
                'metadata': {},
                'outputs': [],
                'source': _lines_with_newlines(code),
            }
        )

    return {
        'cells': cells,
        'metadata': {
            'language_info': {'name': 'python'},
        },
        'nbformat': 4,
        'nbformat_minor': 2,
    }


def _title_from_activity(activity: str) -> str:
    return activity.strip().rstrip('.')


def _base_md(course: str, unit: str, activity: str, extra_obj: List[str]) -> str:
    objectives = '\n'.join([f'- {o}' for o in extra_obj])
    return f"""# {_title_from_activity(activity)}

## \U0001F4DA Learning Objectives

By completing this notebook, you will:
{objectives}

## \U0001F517 Prerequisites

- \u2705 Python basics
- \u2705 Jupyter Notebook basics

---

## Official Structure Reference

This notebook covers practical activities from **Course {course}, Unit {unit}**:
- {activity}
- **Source:** `DETAILED_UNIT_DESCRIPTIONS.md`

---
"""


def _tmpl_visualization(course: str, unit: str, activity: str) -> Tuple[str, List[str]]:
    md = _base_md(course, unit, activity, [
        'Create common chart types with Matplotlib/Seaborn',
        'Build an interactive Plotly chart',
        'Apply basic styling and annotations',
    ]) + """
## Overview

We will generate a small synthetic dataset locally and visualize it using:
- Matplotlib + Seaborn (static)
- Plotly (interactive)
"""

    code1 = """import numpy as np
import pandas as pd

# Plotting libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Make results reproducible
rng = np.random.default_rng(42)

n = 300
x = rng.normal(0, 1, size=n)
y = 2.0 * x + rng.normal(0, 0.6, size=n)
cat = rng.choice(['A', 'B', 'C'], size=n, p=[0.4, 0.35, 0.25])

df = pd.DataFrame({'x': x, 'y': y, 'category': cat})
df.head()"""

    code2 = """# Basic Seaborn scatter + regression line
sns.set_theme(style='whitegrid')
plt.figure(figsize=(7, 4))
sns.regplot(data=df, x='x', y='y', scatter_kws={'alpha': 0.35})
plt.title('y vs x with regression fit')
plt.show()

# Distribution plots
fig, ax = plt.subplots(1, 2, figsize=(10, 4))
sns.histplot(df['x'], kde=True, ax=ax[0])
ax[0].set_title('Distribution of x')

sns.boxplot(data=df, x='category', y='y', ax=ax[1])
ax[1].set_title('y by category')
plt.tight_layout()
plt.show()"""

    code3 = """# Interactive Plotly chart (optional)
try:
    import plotly.express as px

    fig = px.scatter(df, x='x', y='y', color='category', trendline='ols',
                     title='Interactive scatter (Plotly)')
    fig.show()
except ImportError:
    print('Plotly not installed. Install with: pip install plotly')"""

    return md, [code1, code2, code3]


def _tmpl_pandas_eda(course: str, unit: str, activity: str) -> Tuple[str, List[str]]:
    md = _base_md(course, unit, activity, [
        'Load/construct a dataset with Pandas',
        'Perform basic cleaning (missing values, types)',
        'Run simple EDA and feature engineering',
    ]) + """
## Overview

We will construct a dataset locally, introduce missing values, then:
- clean it
- explore relationships
- prepare features for ML
"""

    code1 = """import numpy as np
import pandas as pd

rng = np.random.default_rng(7)

n = 500
age = rng.integers(18, 70, size=n)
income = rng.normal(4000, 1200, size=n).clip(800, None)
city = rng.choice(['Riyadh', 'Jeddah', 'Dammam'], size=n, p=[0.5, 0.3, 0.2])
clicked = (income > 4200).astype(int)

# inject missing values
income[rng.choice(n, size=30, replace=False)] = np.nan

df = pd.DataFrame({'age': age, 'income': income, 'city': city, 'clicked': clicked})
df.head()"""

    code2 = """# Cleaning
print(df.isna().sum())

df['income'] = df['income'].fillna(df['income'].median())
df['city'] = df['city'].astype('category')

# Simple feature engineering

df['income_per_age'] = df['income'] / df['age']

print(df.dtypes)
df.describe(include='all')"""

    code3 = """# EDA (lightweight)
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style='whitegrid')
plt.figure(figsize=(7, 4))
sns.scatterplot(data=df, x='income', y='age', hue='clicked', alpha=0.4)
plt.title('Income vs Age (colored by clicked)')
plt.show()

plt.figure(figsize=(7, 4))
sns.countplot(data=df, x='city', hue='clicked')
plt.title('Clicks by City')
plt.show()"""

    return md, [code1, code2, code3]


def _tmpl_sklearn_supervised(course: str, unit: str, activity: str) -> Tuple[str, List[str]]:
    md = _base_md(course, unit, activity, [
        'Train a baseline classifier with scikit-learn',
        'Evaluate using accuracy + confusion matrix',
        'Show how to encode categorical features',
    ])

    code1 = """import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# small synthetic dataset
rng = np.random.default_rng(123)
n = 600
x1 = rng.normal(size=n)
x2 = rng.normal(size=n)
color = rng.choice(['red','green','blue'], size=n)

y = ((x1 + 0.8*x2 + (color == 'red')*0.6 + rng.normal(scale=0.5, size=n)) > 0.2).astype(int)

df = pd.DataFrame({'x1': x1, 'x2': x2, 'color': color, 'y': y})
X = df.drop(columns=['y'])
y = df['y']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

pre = ColumnTransformer([
    ('cat', OneHotEncoder(handle_unknown='ignore'), ['color']),
], remainder='passthrough')

clf = Pipeline([
    ('pre', pre),
    ('model', LogisticRegression(max_iter=1000))
])

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print('accuracy:', accuracy_score(y_test, y_pred))
print('confusion\n', confusion_matrix(y_test, y_pred))
print('\nreport\n', classification_report(y_test, y_pred))"""

    return md, [code1]


def _tmpl_sklearn_unsupervised(course: str, unit: str, activity: str) -> Tuple[str, List[str]]:
    md = _base_md(course, unit, activity, [
        'Cluster data with K-Means',
        'Use the elbow method and silhouette score',
        'Visualize clusters',
    ])

    code1 = """import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

X, _ = make_blobs(n_samples=500, centers=4, cluster_std=1.2, random_state=42)

inertias = []
sil = []
ks = range(2, 9)
for k in ks:
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    labels = km.fit_predict(X)
    inertias.append(km.inertia_)
    sil.append(silhouette_score(X, labels))

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].plot(list(ks), inertias, marker='o')
ax[0].set_title('Elbow method (inertia)')
ax[0].set_xlabel('k')

ax[1].plot(list(ks), sil, marker='o')
ax[1].set_title('Silhouette score')
ax[1].set_xlabel('k')
plt.tight_layout()
plt.show()

# Fit final model
k_best = 4
km = KMeans(n_clusters=k_best, n_init=10, random_state=42)
labels = km.fit_predict(X)

plt.figure(figsize=(6, 5))
plt.scatter(X[:, 0], X[:, 1], c=labels, s=15)
plt.title(f'K-Means clustering (k={k_best})')
plt.show()"""

    return md, [code1]


def _tmpl_pca(course: str, unit: str, activity: str) -> Tuple[str, List[str]]:
    md = _base_md(course, unit, activity, [
        'Standardize features',
        'Run PCA with scikit-learn',
        'Visualize explained variance and 2D projection',
    ])

    code1 = """import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

iris = load_iris()
X = iris.data

y = iris.target

X_scaled = StandardScaler().fit_transform(X)

pca = PCA(n_components=2, random_state=42)
X2 = pca.fit_transform(X_scaled)

print('explained_variance_ratio:', pca.explained_variance_ratio_)

plt.figure(figsize=(6, 5))
for cls in np.unique(y):
    plt.scatter(X2[y == cls, 0], X2[y == cls, 1], s=18, label=iris.target_names[cls])
plt.title('Iris PCA (2 components)')
plt.legend()
plt.show()

# Scree plot
pca_full = PCA().fit(X_scaled)
plt.figure(figsize=(7, 4))
plt.plot(np.cumsum(pca_full.explained_variance_ratio_), marker='o')
plt.title('Cumulative explained variance')
plt.xlabel('Number of components')
plt.ylabel('Cumulative ratio')
plt.grid(True)
plt.show()"""

    return md, [code1]


def _tmpl_rl_gym_setup(course: str, unit: str, activity: str) -> Tuple[str, List[str]]:
    md = _base_md(course, unit, activity, [
        'Install and import Gym/Gymnasium',
        'Create an environment and run a random agent',
        'Understand states/actions/rewards',
    ])

    code1 = """# Gym has two common packages: gymnasium (new) and gym (older)
# This notebook tries both.
try:
    import gymnasium as gym
    gym_name = 'gymnasium'
except ImportError:
    import gym
    gym_name = 'gym'

print('Using:', gym_name)

env = gym.make('CartPole-v1')
obs, info = env.reset()

print('observation shape:', getattr(obs, 'shape', None))
print('action space:', env.action_space)

# Run a random agent for a few episodes
import numpy as np

rng = np.random.default_rng(0)

def run_episode(max_steps=500):
    obs, info = env.reset()
    total_reward = 0.0
    for t in range(max_steps):
        action = env.action_space.sample()
        step = env.step(action)
        # gymnasium returns: obs, reward, terminated, truncated, info
        if len(step) == 5:
            obs, reward, terminated, truncated, info = step
            done = terminated or truncated
        else:
            obs, reward, done, info = step

        total_reward += float(reward)
        if done:
            break
    return total_reward, t+1

for ep in range(3):
    r, steps = run_episode()
    print(f'episode {ep}: reward={r:.1f}, steps={steps}')

env.close()"""

    return md, [code1]


def _choose_template(path: Path, course: str, unit: str, activity: str) -> Tuple[str, List[str]]:
    name = path.name.lower()
    text = activity.lower()

    # Visualization
    if 'plotly' in name or 'visualization' in name or 'matplotlib' in name or 'seaborn' in name or 'chart' in name:
        return _tmpl_visualization(course, unit, activity)

    # Pandas / EDA / preprocessing
    if 'pandas' in name or 'eda' in name or 'data_clean' in name or 'data' in name and ('clean' in name or 'preprocess' in name):
        return _tmpl_pandas_eda(course, unit, activity)

    # PCA / dimensionality reduction
    if 'pca' in name or 'dimensionality_reduction' in name:
        return _tmpl_pca(course, unit, activity)

    # RL
    if 'openai_gym' in name or 'rl_environment' in name or 'cartpole' in name or 'frozenlake' in name or 'q_learning' in name or 'sarsa' in name:
        return _tmpl_rl_gym_setup(course, unit, activity)

    # Supervised / evaluation
    if 'logistic_regression' in name or 'classification' in name or 'confusion' in name or 'roc' in name or 'svm' in name:
        return _tmpl_sklearn_supervised(course, unit, activity)

    # Unsupervised / clustering
    if 'k_means' in name or 'clustering' in name or 'silhouette' in name or 'elbow' in name:
        return _tmpl_sklearn_unsupervised(course, unit, activity)

    # Default: a solid Pandas + sklearn baseline
    return _tmpl_sklearn_supervised(course, unit, activity)


def _extract_course_unit_from_path(p: Path) -> Tuple[str, str]:
    # Ex: Course 09/unit1-rl-fundamentals/examples/...
    parts = p.parts
    course = None
    unit = None
    for i, part in enumerate(parts):
        if part.startswith('Course '):
            course = part.split(' ')[1]
        if part.lower().startswith('unit'):
            m = re.match(r'unit(\d+)', part.lower())
            if m:
                unit = m.group(1)
    return (course or '?', unit or '?')


def main() -> None:
    audit_file = WORKSPACE / 'AUDIT_placeholder_notebooks.txt'
    if not audit_file.exists():
        raise SystemExit('AUDIT_placeholder_notebooks.txt not found. Run the audit first.')

    targets = [Path(line.strip()) for line in audit_file.read_text(encoding='utf-8').splitlines() if line.strip()]

    upgraded = 0
    skipped = 0
    for rel in targets:
        p = WORKSPACE / rel
        if not p.exists():
            skipped += 1
            continue

        raw = p.read_text(encoding='utf-8')
        if not any(m in raw for m in PLACEHOLDER_MARKERS):
            skipped += 1
            continue

        try:
            nb = json.loads(raw)
        except Exception:
            skipped += 1
            continue

        # derive activity from first markdown cell if present
        activity = None
        try:
            if nb.get('cells'):
                cell0 = nb['cells'][0]
                if cell0.get('cell_type') == 'markdown':
                    src = cell0.get('source', [])
                    if isinstance(src, list) and src:
                        # first line like "# ..."
                        first = ''.join(src).strip().splitlines()[0]
                        if first.startswith('#'):
                            activity = first.lstrip('#').strip()
        except Exception:
            pass

        if not activity:
            # fallback: from filename
            activity = p.stem.replace('_', ' ')

        course, unit = _extract_course_unit_from_path(p)
        md, codes = _choose_template(p, course, unit, activity)
        new_nb = _mk_notebook(md, codes)

        p.write_text(json.dumps(new_nb, indent=2, ensure_ascii=False), encoding='utf-8')
        upgraded += 1

    print('Upgraded:', upgraded)
    print('Skipped:', skipped)


if __name__ == '__main__':
    main()
