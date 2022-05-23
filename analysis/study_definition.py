from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv  # NOQA
from codelists import *


study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
    },
    
    index_date = "2021-12-31",
    
    population = patients.satisfying("""
                                     registered AND (pat_age < 85 AND pat_age >= 19) AND (pat_sex = 'M' OR pat_sex = 'F')
                                     """,
                                     registered = patients.registered_as_of("last_day_of_year(index_date)"),
                                     pat_age = patients.age_as_of("last_day_of_year(index_date)"),
                                     pat_sex = patients.sex()
                                     ),

    age=patients.age_as_of(
        "last_day_of_year(index_date)",
        return_expectations={
            "rate": "universal",
            "int": {"distribution": "population_ages"},
        },
    ),

    sex = patients.sex(
        return_expectations = {
            "rate": "universal",
            "category": {"ratios": {"M": 0.49, "F": 0.51}}
            }
    ),

    CVD_assess_latest_number = patients.with_these_clinical_events(
        CVD_assess_codes,
        on_or_before = "last_day_of_year(index_date)",
        returning = "numeric_value",
        find_last_match_in_period = True,
        return_expectations = {"float": {"distribution": "normal", "mean": 35, "stddev": 15}, "incidence": 0.3}
        ),
        
    CVD_assess_latest_date = patients.with_these_clinical_events(
        CVD_assess_codes,
        on_or_before = "last_day_of_year(index_date)",
        returning = "date",
        date_format = "YYYY-MM-DD",
        find_last_match_in_period = True,
        return_expectations = {"date": {"earliest": "2017-01-01", "latest": "2022-01-01"}, "rate": "uniform", "incidence": 0.1}
        ),
        
    CVD_assess_comparator = patients.comparator_from("CVD_assess_latest_number", 
                                                    return_expectations = {"category": {"ratios": {">": 0.1, "<": 0.2, "~": 0.7}}, "incidence" : 0.1}
                                                    ),
    
    cvdprevent_statins_issued_last_6m = patients.with_these_medications(cvd_prevent_statin_codes,
                                                         between = ["2021-07-01",
                                                                    "last_day_of_year(index_date)"],
                                                         returning = "date",
                                                         date_format = "YYYY-MM-DD",
                                                         return_last_date_in_period = True,
                                                         return_expectations = {"date": {"earliest": "2017-01-01", "latest": "2022-01-01"}, "rate" : "uniform", "incidence": 0.2}
        ),
        
    lipid_modifier_primary = patients.with_these_medications(lipid_modifier_primary,
                                                         between = ["2021-07-01",
                                                                    "last_day_of_year(index_date)"],
                                                         returning = "date",
                                                         date_format = "YYYY-MM-DD",
                                                         return_last_date_in_period = True,
                                                         return_expectations = {"date": {"earliest": "2017-01-01", "latest": "2022-01-01"}, "rate" : "uniform", "incidence": 0.2}
        ),
        
    lipid_modifier_secondary = patients.with_these_medications(lipid_modifier_secondary,
                                                         between = ["2021-07-01",
                                                                    "last_day_of_year(index_date)"],
                                                         returning = "date",
                                                         date_format = "YYYY-MM-DD",
                                                         return_last_date_in_period = True,
                                                         return_expectations = {"date": {"earliest": "2017-01-01", "latest": "2022-01-01"}, "rate" : "uniform", "incidence": 0.2}
        ),
        
    CKD_code = patients.with_these_clinical_events(CKD_codes,
                                                   on_or_before = "last_day_of_year(index_date)",
                                                   returning = "binary_flag",
                                                   return_expectations = {"incidence": 0.1}
                                                   ),
    
    CVD_code_CVD_prevent = patients.with_these_clinical_events(cvd_prevent_cvd_definition,
                                                   on_or_before = "last_day_of_year(index_date)",
                                                   returning = "binary_flag",
                                                   return_expectations = {"incidence": 0.2}
                                                   ),
                                                   
    T1D_code = patients.with_these_clinical_events(T1D_codes,
                                                   on_or_before = "last_day_of_year(index_date)",
                                                   returning = "binary_flag",
                                                   return_expectations = {"incidence": 0.1}
                                                   ),
                                                  
                                                  
)

