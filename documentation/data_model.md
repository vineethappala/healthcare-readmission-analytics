# Healthcare Readmission Analytics — Data Model

## 1. Project Overview

This project analyzes patient readmissions, healthcare utilization, length of stay, follow-up activity, and encounter costs using a synthetic healthcare dataset.

The analytical model is designed to support patient-level and encounter-level analysis while maintaining clear relationships between core healthcare entities.

## 2. Data Model

The project uses four core tables:

- patients
- encounters
- diagnoses
- follow_ups

The `encounters` table serves as the primary fact table.

## 3. Table Definitions

### patients

Stores patient-level demographic and insurance information.

| Column | Description |
|---|---|
| patient_id | Unique patient identifier |
| date_of_birth | Patient date of birth |
| gender | Patient gender |
| race | Race/ethnicity category |
| insurance_type | Insurance category |
| zip_code | ZIP code |

### encounters

Stores individual healthcare encounters.

| Column | Description |
|---|---|
| encounter_id | Unique encounter identifier |
| patient_id | Related patient |
| admission_date | Admission date |
| discharge_date | Discharge date |
| admission_type | Emergency, Elective, or Urgent |
| department | Treating department |
| primary_diagnosis | Primary diagnosis |
| length_of_stay | Number of days between admission and discharge |
| total_charges | Encounter charges |
| discharge_disposition | Discharge status/destination |
| readmitted_30_days | 30-day readmission indicator |

### diagnoses

Stores diagnosis reference information.

| Column | Description |
|---|---|
| diagnosis_code | Unique diagnosis code |
| diagnosis_name | Diagnosis description |
| diagnosis_category | Broad clinical category |

### follow_ups

Stores post-discharge follow-up activity.

| Column | Description |
|---|---|
| follow_up_id | Unique follow-up identifier |
| encounter_id | Related encounter |
| follow_up_date | Date of follow-up |
| follow_up_type | Type of follow-up |
| completed | Follow-up completion indicator |

## 4. Table Relationships

- One patient can have multiple encounters.
- One encounter can have follow-up activity.
- Diagnoses provide reference information used to categorize encounters.

## 5. Fact Table Grain

The grain of the `encounters` table is:

> One row represents one healthcare encounter.

This distinction is important because patient-level and encounter-level metrics must be calculated differently.

For example:

- Total Patients = COUNT(DISTINCT patient_id)
- Total Encounters = COUNT(DISTINCT encounter_id)

## 6. Data Privacy

This project uses synthetic data for portfolio and learning purposes.

No real patient names, medical record numbers, addresses, phone numbers, Social Security numbers, or other direct patient identifiers are used.
