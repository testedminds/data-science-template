# Tested Minds Data Science Template


_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._


This is a customized [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/readme.html) version of the [cookiecutter-data-science](http://drivendata.github.io/cookiecutter-data-science/) project from [DrivenData](https://www.drivendata.org/).


#### [Documentation](http://drivendata.github.io/cookiecutter-data-science/)


### Requirements to use the cookiecutter template:

- Python 3.x
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0

``` bash
pip install cookiecutter
```


### To start a new project, run:

    cookiecutter https://github.com/testedminds/data-science-template



### The resulting directory structure

The directory structure of your new project looks like this:

```
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third-party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering)
│                         and a short `-` delimited description, e.g. `1.0-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
└── src                <- Source code for use in this project.
    ├── __init__.py    <- Makes src a Python module
    │
    ├── data           <- Scripts to download or generate data
    │   └── make_dataset.py
    │
    ├── features       <- Scripts to turn raw data into features for modeling
    │   └── build_features.py
    │
    ├── models         <- Scripts to train models and then use trained models to make
    │   │                 predictions
    │   ├── predict_model.py
    │   └── train_model.py
    │
    └── visualization  <- Scripts to create exploratory and results oriented visualizations
        └── visualize.py
```


### Installing development requirements

    pip install -r requirements.txt


### Running the tests

    py.test tests
