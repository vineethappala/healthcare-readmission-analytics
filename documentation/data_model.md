# Healthcare Readmission Analytics — Data Model

## Purpose

This project analyzes synthetic healthcare encounter data to identify
patterns associated with 30-day hospital readmissions.

The analytical model is designed to support repeatable KPI reporting
and dashboard development.

## Data Grain

The primary analytical grain is:

> One row per healthcare encounter.

## Source Tables

### patients

One row per patient.

Key:
- patient_id

Attributes:
- date_of_birth
- gender
- race
- insurance_type
- zip_code

### encounters

One row per healthcare encounter.

Key:
- encounter_id

Foreign keys:
- patient_id
- diagnosis_code

Key analytical fields:
- admission_date
- discharge_date
- admission_type
- department
- length_of_stay
- total_charges
- discharge_disposition
- readmitted_30_days

### diagnoses

One row per diagnosis code.

Key:
- diagnosis_code

Attributes:
- diagnosis_name
- diagnosis_category

### follow_ups

Potentially multiple records per encounter.

Key:
- follow_up_id

Foreign key:
- encounter_id

Attributes:
- follow_up_date
- follow_up_type
- completed

## Analytical Model

The raw encounter data is transformed into:

### fact_encounter

One row per healthcare encounter.

### dim_patient

One row per patient.

### dim_diagnosis

One row per diagnosis code.

### follow_up_summary

One row per encounter.

This table aggregates multiple follow-up events before joining them
to encounter-level data.

### analytics_encounter

One row per healthcare encounter.

This is the primary analytics-ready table used by the KPI layer.

## KPI Layer

The project produces the following reusable KPI tables:

- kpi_readmission_summary
- kpi_department
- kpi_diagnosis
- kpi_insurance
- kpi_follow_up
- kpi_monthly_trend

## Data Quality Controls

The pipeline validates:

- Duplicate patient IDs
- Duplicate encounter IDs
- Duplicate diagnosis codes
- Duplicate follow-up IDs
- Missing values
- Invalid patient references
- Invalid diagnosis references
- Invalid encounter references
- Admission/discharge date consistency
- Length-of-stay consistency

## Technology

- Python
- Pandas
- DuckDB
- SQL
- CSV
- GitHub
- Power BI (dashboard layer)

## Data Classification

The dataset used in this project is synthetic and contains no real
patient information.ord numbers, addresses, phone numbers, Social Security numbers, or other direct patient identifiers are used.
