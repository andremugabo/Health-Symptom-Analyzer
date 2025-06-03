# Health Symptom Analyzer

## Overview
This application is a Health Symptom Analyzer that helps users:
- Register and log in securely
- Select symptoms from a predefined list
- Get predictions about their illness severity level
- View insightful visualizations of health data

## Features
- User authentication system (registration/login)
- Symptom severity prediction using Decision Tree Classifier
- Data visualization including:
  - Age distribution charts
  - Illness level analysis
  - Symptom intensity pie charts
  - Time-series symptom tracking
  - Age vs. illness severity heatmaps

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Step-by-Step Installation

1. **Clone the repository** (if applicable) or create a new directory for the project
   ```bash
   git clone https://github.com/andremugabo/Health-Symptom-Analyzer.git
   cd Health-Symptom-Analyzer
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

   Or install them individually:
   ```bash
   pip install pandas scikit-learn matplotlib seaborn
   ```

4. **Required Data Files**
   Create these files in your project directory:

   - `symptoms.csv` (symptom definitions):
     ```csv
     symptom,intensity,severity
     fever,mild,1
     headache,moderate,2
     cough,severe,3
     fatigue,mild,1
     sore_throat,moderate,2
     shortness_of_breath,severe,3
     nausea,mild,1
     dizziness,moderate,2
     chest_pain,severe,3
     muscle_aches,mild,1
     runny_nose,moderate,2
     sneezing,mild,1
     chills,moderate,2
     vomiting,severe,3
     diarrhea,moderate,2
     ```

   - `illness.csv` (sample patient data - use the 100-record version provided earlier)

5. **Run the application**
   ```bash
   python app.py
   ```

## Dependencies Explanation

### Core Dependencies
| Package | Purpose | Version |
|---------|---------|---------|
| `pandas` | Data manipulation and analysis | ≥1.0.0 |
| `scikit-learn` | Machine learning (Decision Tree) | ≥0.22.0 |
| `matplotlib` | Data visualization | ≥3.0.0 |
| `seaborn` | Enhanced visualizations | ≥0.10.0 |

### Standard Library Modules
| Module | Purpose |
|--------|---------|
| `os` | File system operations |
| `csv` | CSV file handling |
| `datetime` | Date/time calculations |
| `random` | Random number generation |
| `getpass` | Secure password input |

## File Structure
```
health-symptom-analyzer/
├── app.py                  # Main application code
├── users.csv               # Auto-generated user database
├── symptoms.csv            # Symptom definitions
├── illness.csv             # Patient health records
└── requirements.txt        # Dependency list
```

## Usage Guide

### 1. Registration
- Creates secure user accounts
- Stores: username, full name, date of birth (YYYY-MM-DD), and password
- Passwords are stored in plaintext (for educational purposes only)

### 2. Login
- Authenticates users against stored credentials
- Returns to main menu on failure

### 3. Symptom Checker
- Displays available symptoms with intensities
- Predicts illness level (1-5 scale) based on:
  - User's age (calculated from DOB)
  - Selected symptom severity

### 4. Data Visualizations
Generates five professional charts:
1. Age distribution histogram
2. Illness level frequency bar chart
3. Symptom intensity pie chart
4. Symptoms-over-time line chart
5. Age vs. illness level heatmap

## Technical Notes

### Machine Learning Model
- Uses `DecisionTreeClassifier` from scikit-learn
- Trained on the `illness.csv` dataset
- Features: age and symptom severity
- Target: illness level (1-5)

### Data Requirements
Visualizations require these columns in `illness.csv`:
- `age`: Patient age (numeric)
- `symptom_severity`: 1-3 scale (mild-severe)
- `illness_level`: 1-5 scale (prediction target)
- `date`: Recording date (YYYY-MM-DD)
- `symptom_name`: Text description
- `symptom_intensity`: mild/moderate/severe

## Troubleshooting

### Common Issues
1. **Missing CSV files**:
   - Error: "FileNotFoundError"
   - Solution: Ensure all CSV files exist in the project directory

2. **Dependency errors**:
   - Error: "ModuleNotFoundError"
   - Solution: Run `pip install -r requirements.txt`

3. **Visualization issues**:
   - Error: "Missing column X"
   - Solution: Verify `illness.csv` has all required columns

4. **Date format problems**:
   - Error: "ValueError: time data ..."
   - Solution: Use YYYY-MM-DD format in all date fields



## License
This project is open-source under the MIT License.

