🧪 **PROJECT TITLE: DRUG RECOMMENDATION SYSTEM**

📌 **PROJECT OVERVIEW**

This project aims to build a Drug Recommendation System using machine learning and data analysis techniques.
The system analyzes patient medical profiles (age, gender, conditions, glucose levels, BMI, etc.) and suggests the most suitable drug(s) with confidence scores.
The project follows a structured workflow similar to a professional data science pipeline, ensuring reproducibility, accuracy, and scalability.

⚙️ **PROJECT MODULES**
🔹 **Module 1: Data Preparation & Backend Setup**

- Task 1: Dataset Cleaning (duplicates, missing values).
- Task 2: Feature Engineering (condition–drug mappings, patient history).
- Task 3: Input Pipeline (train/test split, preprocessing).

➡️ **Endpoint 1: Drug Recommendation Service**

- Input: Patient medical record (age, gender, symptoms, condition).
- Output: Suggested drug(s) with confidence score.

🔹 **Module 2: Knowledge & Query Processing**

- Task 4: NLP Query Integration (allow natural language queries).
- Task 5: Medical Database Integration (DrugBank / WHO dataset).

➡️ **Endpoint 2: Query-to-Drug Recommendation**

- Input: Natural language query (e.g., “Which drug is recommended for hypertension?”).
- Output: Recommended drug(s), dosage, and explanation.

🔹 **Module 3: Model Training & Evaluation**

- Task 6: Train ML Models (Logistic Regression, Random Forest, XGBoost).
- Task 7: Model Evaluation (accuracy, precision, recall, F1-score).

➡️ **Endpoint 3: Predictive Recommendation**

- Input: Structured patient data. 
- Output: Top-N recommended drugs.

🔹 **Module 4: Frontend & Integration**

- Patient Form Page → Input patient details & get recommendations.
- Condition Search Page → Search by medical condition.
- Visualization Page → Drug usage trends, dosage charts, prediction confidence.

📊 **VISUALIZATIONS**

- Some planned Power BI & Python visualizations include:
- Drug prescription trends by age group & gender.
- Drug recommendations by disease/condition.
- Correlation heatmaps of features vs. stroke risk.
- Model performance comparison bar chart.
- Interactive dashboards for insights.

🛠️ **TECH STACK** 

- Programming Language: Python 3.13+.
- Libraries: Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Seaborn.
- Backend: Flask.
- Database: SQLite / PostgreSQL, Pinecone (for embeddings) or MongoDB.
- Visualization: Power BI, Matplotlib.
- Frontend: Flask Templates.
