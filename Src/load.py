def load(df):

    df.to_csv(
        "../Data/cleaned_claims.csv",
        index=False
    )

    print("Cleaned file saved")