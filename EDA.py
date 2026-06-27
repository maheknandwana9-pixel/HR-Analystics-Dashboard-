import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ----------------------------
# Load Dataset
# ----------------------------
df = pd.read_excel("WA_Fn-UseC_-HR-Employee-Attrition.xlsx")

# ----------------------------
# Create Images Folder
# ----------------------------
os.makedirs("images", exist_ok=True)

# ----------------------------
# General Settings
# ----------------------------
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (8,5)

print("="*50)
print("DATASET SHAPE")
print(df.shape)

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDATA TYPES")
print(df.dtypes)

print("\nSTATISTICAL SUMMARY")
print(df.describe())

# =====================================================
# 1. Attrition Rate
# =====================================================
plt.figure()
sns.countplot(x='Attrition', data=df)
plt.title("Employee Attrition Rate")
plt.savefig("images/1_attrition_rate.png")
plt.show()

# =====================================================
# 2. Department Wise Attrition
# =====================================================
plt.figure(figsize=(10,5))
sns.countplot(x='Department', hue='Attrition', data=df)
plt.title("Department Wise Attrition")
plt.savefig("images/2_department_attrition.png")
plt.show()

# =====================================================
# 3. Gender Wise Attrition
# =====================================================
plt.figure()
sns.countplot(x='Gender', hue='Attrition', data=df)
plt.title("Gender Wise Attrition")
plt.savefig("images/3_gender_attrition.png")
plt.show()

# =====================================================
# 4. Age Distribution
# =====================================================
plt.figure()
sns.histplot(df['Age'], kde=True)
plt.title("Age Distribution")
plt.savefig("images/4_age_distribution.png")
plt.show()

# =====================================================
# 5. Age vs Attrition
# =====================================================
plt.figure()
sns.boxplot(x='Attrition', y='Age', data=df)
plt.title("Age Group Analysis")
plt.savefig("images/5_age_attrition.png")
plt.show()

# =====================================================
# 6. Monthly Income Distribution
# =====================================================
plt.figure()
sns.histplot(df['MonthlyIncome'], kde=True)
plt.title("Monthly Income Distribution")
plt.savefig("images/6_income_distribution.png")
plt.show()

# =====================================================
# 7. Income vs Attrition
# =====================================================
plt.figure()
sns.boxplot(x='Attrition', y='MonthlyIncome', data=df)
plt.title("Income vs Attrition")
plt.savefig("images/7_income_attrition.png")
plt.show()

# =====================================================
# 8. Overtime Analysis
# =====================================================
plt.figure()
sns.countplot(x='OverTime', hue='Attrition', data=df)
plt.title("Overtime Analysis")
plt.savefig("images/8_overtime_attrition.png")
plt.show()

# =====================================================
# 9. Job Satisfaction Analysis
# =====================================================
plt.figure()
sns.countplot(x='JobSatisfaction', hue='Attrition', data=df)
plt.title("Job Satisfaction Analysis")
plt.savefig("images/9_job_satisfaction.png")
plt.show()

# =====================================================
# 10. Work Life Balance
# =====================================================
plt.figure()
sns.countplot(x='WorkLifeBalance', hue='Attrition', data=df)
plt.title("Work Life Balance Analysis")
plt.savefig("images/10_work_life_balance.png")
plt.show()

# =====================================================
# 11. Job Role Attrition
# =====================================================
plt.figure(figsize=(12,6))
sns.countplot(y='JobRole', hue='Attrition', data=df)
plt.title("Job Role Attrition")
plt.savefig("images/11_jobrole_attrition.png")
plt.show()

# =====================================================
# 12. Marital Status Analysis
# =====================================================
plt.figure()
sns.countplot(x='MaritalStatus', hue='Attrition', data=df)
plt.title("Marital Status Analysis")
plt.savefig("images/12_marital_status.png")
plt.show()

# =====================================================
# 13. Education Field Analysis
# =====================================================
plt.figure(figsize=(10,5))
sns.countplot(y='EducationField', hue='Attrition', data=df)
plt.title("Education Field Analysis")
plt.savefig("images/13_education_field.png")
plt.show()

# =====================================================
# 14. Environment Satisfaction
# =====================================================
plt.figure()
sns.countplot(x='EnvironmentSatisfaction',
              hue='Attrition',
              data=df)
plt.title("Environment Satisfaction")
plt.savefig("images/14_environment_satisfaction.png")
plt.show()

# =====================================================
# 15. Years At Company
# =====================================================
plt.figure()
sns.boxplot(x='Attrition',
            y='YearsAtCompany',
            data=df)
plt.title("Years At Company Analysis")
plt.savefig("images/15_years_company.png")
plt.show()

# =====================================================
# 16. Correlation Heatmap
# =====================================================
numeric_df = df.select_dtypes(include=['int64','float64'])

plt.figure(figsize=(14,10))
sns.heatmap(
    numeric_df.corr(),
    cmap='coolwarm'
)
plt.title("Correlation Heatmap")
plt.savefig("images/16_heatmap.png")
plt.show()

# =====================================================
# BUSINESS INSIGHTS
# =====================================================

print("\n")
print("="*60)
print("BUSINESS INSIGHTS")
print("="*60)

attrition_rate = (
    df['Attrition']
    .value_counts(normalize=True)['Yes']
    * 100
)

print(f"\nOverall Attrition Rate: {attrition_rate:.2f}%")

print("\nTop Departments with Attrition:")
print(
    df[df['Attrition']=='Yes']
    ['Department']
    .value_counts()
)

print("\nOvertime Impact:")
print(
    pd.crosstab(
        df['OverTime'],
        df['Attrition']
    )
)

print("\nJob Satisfaction Impact:")
print(
    pd.crosstab(
        df['JobSatisfaction'],
        df['Attrition']
    )
)

print("\nWork Life Balance Impact:")
print(
    pd.crosstab(
        df['WorkLifeBalance'],
        df['Attrition']
    )
)

print("\nEDA Completed Successfully")
print("All charts saved inside images folder")


import pandas as pd

# Excel file read karo
df = pd.read_excel("WA_Fn-UseC_-HR-Employee-Attrition.xlsx")

# CSV file me save karo
df.to_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv", index=False)

print("Excel converted to CSV successfully!")