import pandas as pd

df = pd.read_csv("heart_2020_cleaned.csv")
by_heart=df.query("HeartDisease == 'Yes'").groupby("AgeCategory").count()[["HeartDisease"]]
by_stroke=df.query("Stroke == 'Yes'").groupby("AgeCategory").count()[["Stroke"]]
final=by_heart.join(by_stroke)

by_biabetic=df.query("Diabetic == 'Yes'").groupby("AgeCategory").count()[["Diabetic"]]
final=final.join(by_biabetic)

by_asthma=df.query("Asthma == 'Yes'").groupby("AgeCategory").count()[["Asthma"]]
final=final.join(by_asthma)

by_kidneyDisease=df.query("KidneyDisease == 'Yes'").groupby("AgeCategory").count()[["KidneyDisease"]]
final=final.join(by_kidneyDisease)

by_skinCancer=df.query("SkinCancer == 'Yes'").groupby("AgeCategory").count()[["SkinCancer"]]
final=final.join(by_skinCancer)
final.to_csv("by_age.csv")
#########
by_heart=df.query("HeartDisease == 'Yes'").groupby("SleepTime").count()[["HeartDisease"]]
by_stroke=df.query("Stroke == 'Yes'").groupby("SleepTime").count()[["Stroke"]]
final=by_heart.join(by_stroke)

by_biabetic=df.query("Diabetic == 'Yes'").groupby("SleepTime").count()[["Diabetic"]]
final=final.join(by_biabetic)

by_asthma=df.query("Asthma == 'Yes'").groupby("SleepTime").count()[["Asthma"]]
final=final.join(by_asthma)

by_kidneyDisease=df.query("KidneyDisease == 'Yes'").groupby("SleepTime").count()[["KidneyDisease"]]
final=final.join(by_kidneyDisease)

by_skinCancer=df.query("SkinCancer == 'Yes'").groupby("SleepTime").count()[["SkinCancer"]]
final=final.join(by_skinCancer)
final.to_csv("by_sleepTime.csv")