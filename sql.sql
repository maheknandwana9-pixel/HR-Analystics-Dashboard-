CREATE DATABASE hr_attrition;
USE hr_attrition;
SHOW TABLES;
SELECT COUNT(*) AS Total_Employees
FROM `wa_fn-usec_-hr-employee-attrition`;
SELECT
Attrition,
COUNT(*) AS Employee_Count
FROM `wa_fn-usec_-hr-employee-attrition`
GROUP BY Attrition;

SELECT
Attrition,
ROUND(
COUNT(*)*100/
(
SELECT COUNT(*)
FROM `wa_fn-usec_-hr-employee-attrition`
),
2
) AS Percentage
FROM `wa_fn-usec_-hr-employee-attrition`
GROUP BY Attrition;

SELECT
Department,
COUNT(*) AS Attrition_Count
FROM `wa_fn-usec_-hr-employee-attrition`
WHERE Attrition='Yes'
GROUP BY Department
ORDER BY Attrition_Count DESC;

SELECT
Gender,
COUNT(*) AS Attrition_Count
FROM `wa_fn-usec_-hr-employee-attrition`
WHERE Attrition='Yes'
GROUP BY Gender;

SELECT
OverTime,
COUNT(*) AS Employees_Left
FROM `wa_fn-usec_-hr-employee-attrition`
WHERE Attrition='Yes'
GROUP BY OverTime;

SELECT
JobSatisfaction,
COUNT(*) AS Employees_Left
FROM `wa_fn-usec_-hr-employee-attrition`
WHERE Attrition='Yes'
GROUP BY JobSatisfaction
ORDER BY JobSatisfaction;

SELECT
WorkLifeBalance,
COUNT(*) AS Employees_Left
FROM `wa_fn-usec_-hr-employee-attrition`
WHERE Attrition='Yes'
GROUP BY WorkLifeBalance
ORDER BY WorkLifeBalance;

SELECT
Department,
ROUND(AVG(MonthlyIncome),2)
AS Average_Salary
FROM `wa_fn-usec_-hr-employee-attrition`
GROUP BY Department
ORDER BY Average_Salary DESC;

SELECT
JobRole,
COUNT(*) AS Attrition_Count
FROM `wa_fn-usec_-hr-employee-attrition`
WHERE Attrition='Yes'
GROUP BY JobRole
ORDER BY Attrition_Count DESC;

SELECT
EmployeeNumber,
JobRole,
MonthlyIncome
FROM `wa_fn-usec_-hr-employee-attrition`
ORDER BY MonthlyIncome DESC
LIMIT 10;

SELECT
EmployeeNumber,
Department,
JobRole,
OverTime,
JobSatisfaction
FROM `wa_fn-usec_-hr-employee-attrition`
WHERE OverTime='Yes'
AND JobSatisfaction<=2;

SELECT
Department,
COUNT(*) AS High_Risk_Employees
FROM `wa_fn-usec_-hr-employee-attrition`
WHERE OverTime='Yes'
AND JobSatisfaction<=2
GROUP BY Department
ORDER BY High_Risk_Employees DESC;

SELECT
Department,
ROUND(
AVG(TotalWorkingYears),
2
) AS Avg_Experience
FROM `wa_fn-usec_-hr-employee-attrition`
GROUP BY Department;

SELECT
COUNT(*) AS Overtime_Employees
FROM `wa_fn-usec_-hr-employee-attrition`
WHERE OverTime='Yes';
