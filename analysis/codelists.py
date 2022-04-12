from cohortextractor import (
    StudyDefinition,
    codelist,
    codelist_from_csv,
    combine_codelists,
    filter_codes_by_category,
    patients,
)

CKD_codes = codelist_from_csv("codelists/primis-covid19-vacc-uptake-ckd15.csv", system = "snomed", column = "code")
CVD_codes = codelist_from_csv("codelists/primis-covid19-vacc-uptake-chd_cov.csv", system = "snomed", column = "code")
T1D_codes = codelist_from_csv("codelists/opensafely-type-1-diabetes.csv", system="ctv3", column="CTV3ID")
T2D_codes = codelist_from_csv("codelists/opensafely-type-2-diabetes.csv", system="ctv3", column="CTV3ID")
Overall_diab_codes = codelist_from_csv("codelists/primis-covid19-vacc-uptake-diab.csv", system = "snomed", column = "code")
statin_codes = codelist_from_csv("codelists/opensafely-statin-medication.csv", system = "snomed", column = "id")
CVD_assess_codes = codelist_from_csv("codelists/opensafely-cvd-risk-assessment-score-qof.csv", system = "snomed", column = "code")
cvd_prevent_statin_codes = codelist_from_csv("codelists/opensafely-cvd_prevent_statins.csv", system = "snomed", column = "code")
