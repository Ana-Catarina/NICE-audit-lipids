library('tidyverse')
library(here)

## Load data from cohort extractor
df_input <- read_csv(
  here::here("output", "input.csv")
  )

# Check format of data
head(df_input)

colnames(df_input)

nrow(df_input)



## select patients with CVD

df_cvd <- df_input[df_input$CVD_code == 1, ]

nrow(df_cvd)


## select patients with CKD

df_ckd <- df_input[df_input$CKD_code == 1, ]

nrow(df_ckd)


## exclude patients under 40 yo

df_input <- df_input[df_input$age >= 40, ]

summary(df_input$age)

nrow(df_input)


## exclude patients with CVD, CKD or T1D

df_input <- df_input[df_input$CVD_code == 0 & df_input$CKD_code == 0 & df_input$T1D_code == 0, ]

nrow(df_input)


## exclude patients with risk assessment more than 5 years ago

summary(df_input$CVD_assess_latest_date)

df_input_2 <- df_input[df_input$CVD_assess_latest_date >= "2017-01-01", ]

summary(df_input_2$CVD_assess_latest_date)

nrow(df_input)


## calculate % patients with CVD assessment in past 5 years

summary(df_input_2$CVD_assess_latest_number)

df_input_2$CVD_assess_cat <- ifelse(is.na(df_input_2$CVD_assess_latest_number), 0, 1)

cvd.risk <- summary(as.factor(df_input_2$CVD_assess_cat))

write.csv(cvd.risk, here("output", "cvd.risk.5years.csv"))


## calculate % patients with CVD risk over 10 on statins (NA means not on statins)

data_risk10 <- df_input_2[df_input_2$CVD_assess_latest_number >= 10, ]

summary(data_risk10$statins_prescribed)

data_risk10$statin_cat <- ifelse(is.na(data_risk10$statins_prescribed), 0, 1)

statin.risk10 <- summary(as.factor(data_risk10$statin_cat))

write.csv(statin.risk10, here("output", "statin.risk10.csv"))


## calculate % patients with CVD risk over 20 on statins (NA means not on statins)

data_risk20 <- df_input_2[df_input_2$CVD_assess_latest_number >= 20, ]

summary(data_risk20$statins_prescribed)

data_risk20$statin_cat <- ifelse(is.na(data_risk20$statins_prescribed), 0, 1)

statin.risk20 <- summary(as.factor(data_risk20$statin_cat))

write.csv(statin.risk20, here("output", "statin.risk20.csv"))


## calculate % patients with pre-existing CVD on statins (NA means not on statins)

summary(df_cvd$statins_prescribed)

df_cvd$statin_cat <- ifelse(is.na(df_cvd$statins_prescribed), 0, 1)

statin.cvd <- summary(as.factor(df_cvd$statin_cat))

write.csv(statin.cvd, here("output", "statin.cvd.csv"))


## calculate % patients with CKD on statins (NA means not on statins)

summary(df_ckd$statins_prescribed)

df_ckd$statin_cat <- ifelse(is.na(df_ckd$statins_prescribed), 0, 1)

statin.ckd <- summary(as.factor(df_ckd$statin_cat))

write.csv(statin.ckd, here("output", "statin.ckd.csv"))
