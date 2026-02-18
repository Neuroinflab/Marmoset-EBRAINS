import pandas as pd

df = pd.read_excel("meta.xlsx")
df.columns = ["case_id", "hemisphere", "sex", "weight", "age", "no_areas"]

results = []
#[Out]# 0   CJ114, R          M        409   3 years, 4 months        19
#[Out]# 1   CJ115, R          F        387  2 years, 11 months        18
#[Out]# 2   CJ116, R          F        339   3 years, 2 months        18
#[Out]# 3   CJ153, L          F        336    1 year, 7 months        18
#[Out]# 4   CJ174, R          F        342   2 years, 8 months        18
#[Out]# 5   CJ111, L          M        334    3 years, 1 month        18
#[Out]# 6   CJ108, R          M        349   3 years, 2 months        17
#[Out]# 7   CJ102, L          F        350     4 year, 12 days        17
#[Out]# 8    CJ56, L          M        350    1 year, 8 months        17
#[Out]# 9   CJ180, R          M        374   2 years, 9 months        17
#[Out]# 10  CJ112, L          M        377   3 years, 2 months        16
#[Out]# 11  CJ157, L          F        364    1 year, 7 months        16
#[Out]# 12  CJ164, L          F        304    1 year, 7 months        15
#[Out]# 13  CJ110, L          M        357    3 years, 1 month        15
#[Out]# 14   CJ81, L          F        419   2 years, 5 months        15
#[Out]# 15   CJ71, R          M        412    1 year, 6 months        15
#[Out]# 16  CJ122, R          M        318  2 years, 11 months        15
#[Out]# 17   CJ78, L          M        394    2 years, 1 month        13
#[Out]# 18  CJ181, R          M        368   2 years, 3 months        11

header = ["subject", "sex", "age_category", "species", "age", "weight",
          "strain", "pathology", "phenotype", "handedness", "laterality",
          "origin", "sampletype", "brain_area", "file_1", "file_2", "file_3",
          "technique_1", "technique_2", "technique_3"]

print(df)
for idx, row in df.iterrows():
    if row.sex == "M":
        _sex = "male"
    if row.sex == "F":
        _sex = "female"

    print(row.hemisphere)
    if row.hemisphere.strip() == "R":
        _laterality = "right"
    if row.hemisphere.strip() == "L":
        _laterality = "left"

    results.append([str(row.case_id),         # subject
                    _sex,                    # sex
                    "Adult",                 # age_category
                    "Callithrix jacchus",    # species
                    str(row.age),             # age
                    str(row.weight) + "g",    # weight
                    "none",                  # strain
                    "none",                  # pathology
                    "Wildtype",              # phenotype
                    "none",                  # handedness
                    _laterality,             # laterality
                    "brain",                 # origin
                    "tissue slice",          # sampletype
                    "cerebral cortex",       # brain_area
                    "N/A",                   # file_1
                    "N/A",                   # file_2
                    "N/A",                   # file_3
                    "light microscopy",      # technique_1
                    "image registration",    # technique_2
                    "Nissl staining",        # technique_3
                    ])
vf=pd.DataFrame(results, columns=header)
print(vf)

vf.to_excel("nencki_monash_case_metadata.xlsx")

#df.columns#[Out]# Index(['case_id', 'hemisphere', 'sexweight', 'age', 'no_areas'], dtype='object')
