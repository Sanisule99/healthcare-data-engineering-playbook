# FHIR Patient + Observation Walkthrough

## 1. What is FHIR?

FHIR stands for **Fast Healthcare Interoperability Resources**. It is a modern healthcare data exchange standard that represents clinical data as modular resources such as:

- Patient
- Observation
- Condition
- Encounter
- MedicationRequest
- DiagnosticReport

FHIR matters because it helps healthcare systems exchange data in a standardized way.

## 2. Why FHIR Matters for Healthcare Data Engineering

FHIR is useful for:

- Data integration across systems
- Clinical dashboards
- Quality measurement
- AI model feature extraction
- Public health reporting
- Clinical decision support tools

## 3. Querying a FHIR API

A FHIR API endpoint usually looks like:

```text
https://server-url/fhir/Patient
```

You can request specific resource types such as:

```text
/Patient
/Observation
/Condition
/Encounter
```

## 4. Turning FHIR JSON into Tables

FHIR responses are returned as JSON bundles. For analytics, we usually flatten selected fields into tables.

Example Patient table:

| patient_id | gender | birth_date |
|---|---|---|
| 123 | female | 1985-01-10 |

Example Observation table:

| observation_id | patient_reference | code | value | unit |
|---|---|---|---|---|
| obs1 | Patient/123 | 8480-6 | 120 | mmHg |

## 5. How to Extend This Tutorial

Try adding:

- Condition resources
- Encounter resources
- Lab-only observations
- Date filters
- Patient-specific queries

## 6. Practice Challenge

Modify the Python script to:

1. Query 50 Observations
2. Extract only observations with numeric values
3. Save the result as a CSV file
4. Create a simple summary table by observation code
