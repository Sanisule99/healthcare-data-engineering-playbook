-- ============================================
-- Healthcare SQL Analytics Examples
-- ============================================

-- 1. Count encounters by type
SELECT
    encounter_type,
    COUNT(*) AS encounter_count
FROM encounters
GROUP BY encounter_type
ORDER BY encounter_count DESC;

-- 2. Average length of stay
SELECT
    encounter_type,
    AVG(length_of_stay_days) AS avg_los_days
FROM encounters
GROUP BY encounter_type;

-- 3. Most common diagnoses
SELECT
    diagnosis_code,
    diagnosis_description,
    COUNT(*) AS diagnosis_count
FROM diagnoses
GROUP BY diagnosis_code, diagnosis_description
ORDER BY diagnosis_count DESC;

-- 4. Patients with multiple encounters
SELECT
    patient_id,
    COUNT(*) AS total_encounters
FROM encounters
GROUP BY patient_id
HAVING COUNT(*) > 1;

-- 5. High utilization patients
SELECT
    patient_id,
    SUM(length_of_stay_days) AS total_days
FROM encounters
GROUP BY patient_id
ORDER BY total_days DESC;

-- 6. Join patients + encounters
SELECT
    p.patient_id,
    p.sex,
    p.age,
    e.encounter_type,
    e.length_of_stay_days
FROM patients p
JOIN encounters e
ON p.patient_id = e.patient_id;

-- 7. Inpatient cohort
SELECT *
FROM encounters
WHERE encounter_type = 'inpatient';
