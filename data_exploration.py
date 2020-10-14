import pandas as pd
import matplotlib.pyplot as plt


def main():
    police_df = pd.read_csv("./Court Overtime 2014 - 2019 - 2019.csv")
    police_df.columns = ["ID", "NAME" , "RANK" ," ASSIGNED", "CHARGED", "OTDATE", "DESCRIPTIONS", "OTCODE", "DESCRIPTION", "STARTTIME", "ENDTIME", "WRKDHRS", "OTHOURS"]
    
    police_df = police_df.drop([19149]) # remove the row that contained the categories

    police_df['OTHOURS'] = pd.to_numeric( police_df['OTHOURS'])

    print( police_df.groupby('NAME').OTHOURS.sum() )

    plt.plot( police_df.groupby('NAME')["OTHOURS"].sum() )
    plt.xticks(rotation=90)
    plt.yticks(rotation=45)
    plt.show()
    
if __name__ == "__main__":
    main()
