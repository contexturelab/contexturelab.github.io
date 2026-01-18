# %% Load the data
import pandas as pd

file_list = {
    "SSIE641-20_FALL23.csv": ("SSIE 641", "20", "Fall 23"),
    "SSIE641-90_FALL23.csv": ("SSIE 641", "90", "Fall 23"),
    "SSIE519-01_SPG24.csv": ("SSIE 519", "01", "Spring 24"),
}

focal_score = ["High"]
focal_ques = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

dflist = []
for filename, (course, section, term) in file_list.items():
    df = pd.read_csv(filename)
    df["QUES"] = df["QUES"].fillna(0).astype(int)
    df["Course"] = course  + f" {section}"
    df["Term"] = term
    df = df.dropna().query("ANS_TEXT in @focal_score and QUES in @focal_ques")
    df["QUES"] = df["QUES"].astype(str).apply(lambda x: "Q" + x)
    df.set_index("QUES", inplace=True)

    dflist+= [df[["Course", "Term", "ANS_PCT"]]]
df = pd.concat(dflist)
df = df.groupby(["Course", "Term"]).apply(lambda x: x[["ANS_PCT"]].rename(columns={"ANS_PCT": ""}).T)

# Remove multirow columns from the DataFrame
df = df.reset_index().drop(columns=["level_2"])
#.drop(columns=["QUES"])

df.columns
df.to_latex("soot_score_table.tex", float_format="%d", longtable=False, column_format = "p{3cm}p{2cm}p{1cm}p{1cm}p{1cm}p{1cm}p{1cm}p{1cm}p{1cm}p{1cm}p{1cm}p{1cm}p{1cm}p{1cm}p{1cm}p{1cm}p{1cm}p{1cm}p{1cm}p{1cm}p{1cm}p{1cm}", index=False)

# %%
