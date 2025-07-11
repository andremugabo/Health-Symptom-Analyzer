import os
import csv
from datetime import datetime
import pandas as pd # type: ignore
from sklearn.tree import DecisionTreeClassifier # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
import matplotlib.pyplot as plt # type: ignore
import random
import getpass
import seaborn as sns # type: ignore

# File paths
USERS_FILE = "users.csv"
SYMPTOMS_FILE = "symptoms.csv"
ILLNESS_FILE = "illness.csv"

# Initialize datasets if they don't exist
def initialize_files():
    # Create users file if it doesn't exist
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["username", "name", "dob", "password"])

# User registration
def register_user():
    print("\n--- Registration ---")
    username = input("Enter username: ")
    
    # Check if username already exists
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == username:
                    print("Username already exists!")
                    return
    
    name = input("Enter your full name: ")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    password = getpass.getpass("Enter password: ")
    
    with open(USERS_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, name, dob, password])
    
    print("Registration successful!")

# User login
def login_user():
    print("\n--- Login ---")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    
    with open(USERS_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == username and row[3] == password:
                print(f"Welcome back, {row[1]}!")
                return {"username": row[0], "name": row[1], "dob": row[2]}
    
    print("Invalid username or password!")
    return None

# Calculate age from DOB
def calculate_age(dob_str):
    dob = datetime.strptime(dob_str, "%Y-%m-%d")
    today = datetime.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

# Predict illness level
def predict_illness(age, symptom_severity):
    # Load illness data
    illness_data = pd.read_csv(ILLNESS_FILE)
    
    # Prepare data for model
    X = illness_data[['age', 'symptom_severity']]
    y = illness_data['illness_level']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    # Make prediction
    prediction = model.predict([[age, symptom_severity]])
    return prediction[0]

# Show symptoms and get user selection
def prompt_symptoms(user_info):
    print("\n--- Symptom Checker ---")
    
    # Load symptoms data
    symptoms_df = pd.read_csv(SYMPTOMS_FILE)
    print("Available symptoms:")
    for i, row in symptoms_df.iterrows():
        print(f"{i+1}. {row['symptom']} ({row['intensity']})")
    
    try:
        choice = int(input("Enter the number of your symptom: ")) - 1
        if choice < 0 or choice >= len(symptoms_df):
            print("Invalid choice!")
            return
        
        selected_symptom = symptoms_df.iloc[choice]
        age = calculate_age(user_info['dob'])
        severity = selected_symptom['severity']
        
        # Predict illness level
        illness_level = predict_illness(age, severity)
        
        print("\n--- Analysis ---")
        print(f"Age: {age} years")
        print(f"Symptom: {selected_symptom['symptom']} ({selected_symptom['intensity']})")
        print(f"Predicted illness level: {illness_level}/5")
        print("(1 = least severe, 5 = most severe)")
        
    except ValueError:
        print("Please enter a valid number!")

def generate_visualizations():
    print("\nGenerating visualizations...")
    
    # Load illness data
    illness_data = pd.read_csv(ILLNESS_FILE)

    # Ensure required columns are present
    required_columns = ['age', 'illness_level', 'symptom_intensity', 'date', 'symptom_name']
    for col in required_columns:
        if col not in illness_data.columns:
            print(f"Missing column: {col}")
            return

    # Set date to datetime if needed
    illness_data['date'] = pd.to_datetime(illness_data['date'])

    # Create figure layout
    fig = plt.figure(figsize=(18, 10))
    
    # 1. Age Distribution
    plt.subplot(2, 3, 1)
    illness_data['age'].plot(kind='hist', bins=10, color='skyblue', edgecolor='black')
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Count')
    
    # 2. Illness Level Distribution
    plt.subplot(2, 3, 2)
    illness_data['illness_level'].value_counts().sort_index().plot(kind='bar', color='lightgreen')
    plt.title('Illness Level Distribution')
    plt.xlabel('Illness Level (1–5)')
    plt.ylabel('Count')
    
    # 3. Pie Chart: Symptom Intensity
    plt.subplot(2, 3, 3)
    intensity_counts = illness_data['symptom_intensity'].value_counts()
    plt.pie(intensity_counts, labels=intensity_counts.index, autopct='%1.1f%%', colors=plt.cm.Pastel1.colors)
    plt.title('Symptom Intensity Distribution')

    # 4. Line Chart: Symptom occurrences over time
    plt.subplot(2, 3, 4)
    symptoms_over_time = illness_data.groupby(['date'])['symptom_name'].count()
    symptoms_over_time.plot(kind='line', marker='o', color='coral')
    plt.title('Symptoms Reported Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Symptoms')

    # 5. Heatmap: Age vs Illness Severity
    plt.subplot(2, 3, 5)
    heatmap_data = pd.crosstab(illness_data['age'], illness_data['illness_level'])
    sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt='d')
    plt.title('Age vs Illness Level')
    plt.xlabel('Illness Level')
    plt.ylabel('Age')

    plt.tight_layout()
    plt.savefig('enhanced_illness_visualization.png')
    print("Visualizations saved as 'enhanced_illness_visualization.png'")
    plt.show()

# Main menu
def main():
    initialize_files()
    current_user = None
    
    while True:
        print("\n=== Health Symptom Analyzer ===")
        print("1. Register")
        print("2. Login")
        if current_user:
            print("3. Check Symptoms")
            print("4. View Data Visualizations")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            register_user()
        elif choice == '2':
            current_user = login_user()
        elif current_user and choice == '3':
            prompt_symptoms(current_user)
        elif current_user and choice == '4':
            generate_visualizations()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()