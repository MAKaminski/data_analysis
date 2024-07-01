## Traffic Info

![GitHub stars](https://img.shields.io/github/stars/MAKaminski/data_analysis)
![GitHub watchers](https://img.shields.io/github/watchers/MAKaminski/data_analysis)
![GitHub forks](https://img.shields.io/github/forks/MAKaminski/data_analysis)
![GitHub contributors](https://img.shields.io/github/contributors/MAKaminski/data_analysis)
![GitHub all releases](https://img.shields.io/github/downloads/MAKaminski/data_analysis/total)
![GitHub release date](https://img.shields.io/github/release-date/MAKaminski/data_analysis)
![GitHub last commit](https://img.shields.io/github/last-commit/MAKaminski/data_analysis)

## Repo
![GitHub repo size](https://img.shields.io/github/repo-size/MAKaminski/data_analysis)
![GitHub code size](https://img.shields.io/github/languages/code-size/MAKaminski/data_analysis)
![GitHub language count](https://img.shields.io/github/languages/count/MAKaminski/data_analysis)
![GitHub top language](https://img.shields.io/github/languages/top/MAKaminski/data_analysis)
![Coverage](https://img.shields.io/codecov/c/github/MAKaminski/data_analysis)
![GitHub license](https://img.shields.io/github/license/MAKaminski/data_analysis)

## Issues
![GitHub issues](https://img.shields.io/github/issues/MAKaminski/data_analysis)
![GitHub closed issues](https://img.shields.io/github/issues-closed/MAKaminski/data_analysis)
![GitHub pull requests](https://img.shields.io/github/issues-pr/MAKaminski/data_analysis)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/MAKaminski/data_analysis)

# Exploring Data Aggregation Across Diverse Frameworks
Welcome to my GitHub repository, where you'll find the code and insights from my latest project – a comprehensive exploration into the world of data aggregation using multiple frameworks. This project, which I've documented in detail on my .dev blog, aims to shed light on the performance, scalability, and usability of different data processing tools in handling complex, distributed test data.

## About the Project
In this endeavor, I've embarked on a two-fold journey:

**Generator** - A program that allows users to create test data with specific parameters using various frameworks  
**Profiler** - Analyzing execution time/speed, memory usage and general scalability  
**Processor** - Processing the generated data and applying the Profiler in order to identify best-fit use cases depending on data distributioin  

## Number of files
File format  
> Excel .xlsx  
> CSV   .csv  
> XLSB  .xlsb  

Data type distribution (Integers, Strings, Dates)
This process not only simulates real-world data complexities but also provides a versatile dataset for our aggregation experiments.

Aggregating Data Using Various Frameworks: The project utilizes four distinct frameworks – Pandas, Scikit-learn, Polar, and Dask – to aggregate the generated data. I've conducted a thorough analysis, focusing on:

Append operations (combining records from multiple files)
Add operations (summing records across datasets)
Each framework was evaluated based on execution time, memory usage, scalability, data integrity, and more, offering a nuanced view of their capabilities in different scenarios.

## Insights and Findings
The project reveals intriguing insights about each framework's strengths and weaknesses, providing valuable guidance for anyone working with large and diverse datasets. Whether you're a data scientist, a software engineer, or just a data enthusiast, you'll find the findings from this project enlightening and potentially influential in your choice of data processing tools.

## Repository Contents
>📊 Code: All scripts used for data generation and aggregation.  
>📑 Data Samples: Sample datasets created for testing.  
>📝 Documentation: Detailed explanation of methodologies and tools used.  
>📈 Performance Analysis: Comparative charts and analysis reports.

## Directory Structure

**DATA_ANALYSIS** (Main Code)
* `.flake8` (Optional) [Ignoring Linting Errors]
* `poetry.lock` (Optional) [Building Tightly Woven Packages]
* `pyproject.toml` (Optional) [Building Tightly Woven Packages]
* `README.md` (Default)

**.vscode** (Visual Studio Code configuration)
* `launch.json` (Optional)
* `settings.json` (Optional) [Ignoring Linting Errors]

**data_analysis** (Subdirectory within Main Code)
* `__init__.py` (Default)
* `data_generator.py` (Generator)
* `profiler.py` (Profiler)
* `_pycache_` (Runtime code cache)
    * `profiler.cpython-312.pyc` (Compiled code)

**data** (Test Data Storage)
* *Data File Storage*

**tests** (Unit Tests)
* `__init__.py` (Default)

# Join the Conversation
I invite you to dive into the code, experiment with it, and join the ongoing discussion about data aggregation frameworks. Your insights, feedback, and contributions are welcome as we continue to explore this ever-evolving landscape of data processing.

# Links & Resources
Read the full .dev article for an in-depth journey into this project.
