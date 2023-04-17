import pymysql
#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="040503", database="employee_attrition")
cursor = connection.cursor()
#inserting data to db
def addtodatabase(Age,DistanceFromHome,EnvironmentSatisfaction,JobInvolvement,JobRole,JobSatisfaction,NumCompaniesWorked,PercentSalaryHike,StockOptionLevel,TotalWorkingYears,
            WorkLifeBalance,YearsAtCompany,YearsInCurrentRole,EducationField_Human_Resources,EducationField_Life_Sciences,EducationField_Marketing,
            EducationField_Medical,EducationField_Other,EducationField_Technical_Degree,MaritalStatus_Divorced,MaritalStatus_Married,MaritalStatus_Single,
            OverTime_No,OverTime_Yes,DailyRate,MonthlyIncome):
    cursor.execute("INSERT INTO mytable(ID, Age, DistanceFromHome,EnvironmentSatisfaction,JobInvolvement,JobRole,JobSatisfaction,NumCompaniesWorked,PercentSalaryHike,StockOptionLevel,TotalWorkingYears,WorkLifeBalance,YearsAtCompany,YearsInCurrentRole,EducationField_Human_Resources,EducationField_Life_Sciences,EducationField_Marketing,EducationField_Medical,EducationField_Other,EducationField_Technical_Degree,MaritalStatus_Divorced,MaritalStatus_Married,MaritalStatus_Single,OverTime_No,OverTime_Yes,DailyRate,MonthlyIncome) VALUES (DEFAULT, %d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%f,%f)", (Age, DistanceFromHome,EnvironmentSatisfaction,JobInvolvement,JobRole,JobSatisfaction,NumCompaniesWorked,PercentSalaryHike,StockOptionLevel,TotalWorkingYears,WorkLifeBalance,YearsAtCompany,YearsInCurrentRole,EducationField_Human_Resources,EducationField_Life_Sciences,EducationField_Marketing,EducationField_Medical,EducationField_Other,EducationField_Technical_Degree,MaritalStatus_Divorced,MaritalStatus_Married,MaritalStatus_Single,OverTime_No,OverTime_Yes,DailyRate,MonthlyIncome))
    connection.commit()
    return 1