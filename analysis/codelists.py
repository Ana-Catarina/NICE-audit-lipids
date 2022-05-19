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
CVD_assess_codes = codelist_from_csv("codelists/opensafely-cvd-risk-assessment-score-qof.csv", system = "snomed", column = "code")
cvd_prevent_statin_codes = codelist_from_csv("codelists/opensafely-cvd_prevent_statins.csv", system = "snomed", column = "code")
cvd_prevent_cvd_definition = codelist_from_csv("codelists/user-rob_w-cvd_prevent_cvd_definition.csv", system = "snomed", column = "code")
non_statin_lipid_modifier_primary = codelist_from_csv("codelists/user-rob_w-non-statin-lipid-modifying-therapies.csv", system = "snomed", column = "code")
non_statin_lipid_modifier_secondary = codelist_from_csv("codelists/user-rob_w-non-statin-lipid-modifying-therapies-secondary.csv", system = "snomed", column = "code")
lipid_modifier_primary = combine_codelists(non_statin_lipid_modifier_primary, cvd_prevent_statin_codes)
lipid_modifier_secondary = combine_codelists(non_statin_lipid_modifier_secondary, cvd_prevent_statin_codes)
