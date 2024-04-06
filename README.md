## Overview
Network Intrusion Detection Data Set consists of network flow data captured from a network. The data set includes various features and labels indicating different types of network traffic.

## Files

- `2022.06.12.csv`: Network flow data for June 12, 2022.
- `2022.06.13.csv`: Network flow data for June 13, 2022.
- `2022.06.14.csv`: Network flow data for June 14, 2022.

## Preprocessing

- Concatenated the daily data files into a single data frame.
- Removed duplicate and missing values.
- Replaced label values ('outlier', 'benign') with numerical values.

## Machine Learning Model

- Trained Random Forest and Decision Tree classifiers on the preprocessed data.
- Evaluated model performance using accuracy and classification reports.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/network-intrusion.git

Install the required dependencies:
pip install -r requirements.txt

Model Deployment
Saved the trained Random Forest classifier as random_forest.joblib.
Loaded the model for inference in other applications.

License

3. **Save the File**: Save the file with the name `README.md` in your project's root directory.

4. **Commit and Push to GitHub**: Add, commit, and push the README file to your GitHub repository using Git commands:

```bash
git add README.md
git commit -m "Add README file"
git push origin main

