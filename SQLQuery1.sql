use AriCompany

SELECT * FROM CrewMembers
SELECT * FROM Aircrafts
SELECT * FROM Experience

--Najstariji èlan--
SELECT TOP 1 IDMembers, Name
FROM CrewMembers
WHERE Age= (SELECT MAX(Age) FROM CrewMembers)

--N-ti Èlan--
WITH RESULTS AS
(SELECT AGE, DENSE_RANK() OVER (ORDER BY AGE DESC) AS DENSERANK
FROM CrewMembers)
SELECT TOP 1 AGE
FROM RESULTS
WHERE RESULTS.DENSERANK = N

--Najiskusniji èlan--
SELECT TOP 1 Name, COUNT(*) AS Experience
FROM CrewMembers
INNER JOIN Experience on CrewMembers.IDMembers = Experience.IDMembers
GROUP BY Name
ORDER BY  COUNT(*) DESC

--Najmanje iskusan èlan--

SELECT TOP 1 Name, COUNT(*) AS Experience
FROM CrewMembers
INNER JOIN Experience on CrewMembers.IDMembers = Experience.IDMembers
GROUP BY Name
ORDER BY  COUNT(*) ASC
