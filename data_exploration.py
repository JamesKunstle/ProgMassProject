import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    police_df = pd.read_csv("./Court Overtime 2014 - 2019 - 2019.csv")
    police_df.columns = ["ID", "NAME" , "RANK" ," ASSIGNED", "CHARGED", "OTDATE", "DESCRIPTIONS", "OTCODE", "DESCRIPTION", "STARTTIME", "ENDTIME", "WRKDHRS", "OTHOURS"]
    
    police_df = police_df.drop([19149]) # remove the row that contained the categories

    police_df['OTHOURS'] = pd.to_numeric( police_df['OTHOURS'])
    police_df['WRKDHRS'] = pd.to_numeric( police_df['WRKDHRS'])

    officer_OT = police_df.groupby('NAME')["OTHOURS"].sum() #get just the total yearly overtime that an office worked
    highOT = officer_OT[ officer_OT > 500  ] #find those individuals with a numerically high OT
    names = list(highOT.index.values) #get a list of the names of these officers

    police_df_high_OT = police_df[ police_df["NAME"].isin(set(names))] # backtrack to narrow DB down to just those previous officers

    officer_worked = police_df_high_OT.groupby('NAME')['WRKDHRS'].sum() #get the sum of the worked hours of these officers

    zipped_hours = pd.DataFrame(zip(names, highOT, officer_worked), columns=["NAME", "OT", "WORKED"])
    print(zipped_hours.dtypes)

    sns.barplot(x="NAME", y="OT", data=zipped_hours )
    plt.xticks(rotation=90)
    plt.show()

if __name__ == "__main__":
    main()
