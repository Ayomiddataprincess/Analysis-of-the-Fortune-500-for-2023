SELECT *
FROM FORTUNE_500

--DATA CLEANING
UPDATE FORTUNE_500
SET Revenue_growth = REPLACE(Revenue_growth, '%', '');

UPDATE FORTUNE_500
SET Employees = REPLACE(Employees, ',', '')
WHERE Employees LIKE '%,%';

ALTER TABLE FORTUNE_500
ALTER COLUMN Revenue_growth DECIMAL(5,2);

ALTER TABLE FORTUNE_500
ALTER COLUMN Employees INT;

--Analysis of dataset
SELECT Top 10 *
FROM FORTUNE_500
ORDER BY Revenue_USD_millions DESC

SELECT Top 10 *
FROM FORTUNE_500
ORDER BY Revenue_growth DESC

SELECT DISTINCT Industry
FROM FORTUNE_500

SELECT COUNT (DISTINCT Name)
FROM FORTUNE_500

SELECT COUNT (DISTINCT Industry)
FROM FORTUNE_500

SELECT Industry, SUM(Revenue_USD_millions) AS TotalRevenue
FROM FORTUNE_500
GROUP BY Industry
ORDER BY TotalRevenue DESC;

SELECT Industry, 
       AVG(Revenue_USD_millions) AS AVGRevenue, 
       AVG(Revenue_growth) AS AVGRevenueGrowth
FROM FORTUNE_500
GROUP BY Industry
ORDER BY AVGRevenue DESC;

SELECT Industry, SUM(Employees) AS TotalEmployees
FROM FORTUNE_500
GROUP BY Industry
ORDER BY TotalEmployees DESC;


SELECT Industry, AVG(Employees) AS AvgEmployees
FROM FORTUNE_500
GROUP BY Industry;

SELECT Headquarters, AVG(Revenue_USD_millions) AS AVGRevenue
FROM FORTUNE_500
GROUP BY Headquarters
ORDER BY AVGRevenue DESC;

SELECT Industry, COUNT(*) AS NumberOfCompanies
FROM FORTUNE_500
GROUP BY Industry
ORDER BY NumberOfCompanies DESC;

SELECT MIN(Revenue_USD_millions) AS MinRevenue, MAX(Revenue_USD_millions) AS MaxRevenue, AVG(Revenue_USD_millions) AS AvgRevenue
FROM FORTUNE_500;

SELECT AVG(Revenue_growth) AS AvgRevenueGrowth, MIN(Revenue_growth) AS MinGrowth, MAX(Revenue_growth) AS MaxGrowth
FROM FORTUNE_500;

SELECT DISTINCT 
    Industry, 
    SUM(Revenue_USD_millions) AS Total_Industry_Revenue, 
    (SUM(Revenue_USD_millions) / (SELECT SUM(Revenue_USD_millions) FROM FORTUNE_500)) * 100 AS Percentage_Of_Total_Revenue
FROM 
    FORTUNE_500
GROUP BY 
    Industry
ORDER BY 
    Total_Industry_Revenue DESC;

