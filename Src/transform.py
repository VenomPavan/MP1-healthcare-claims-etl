def transform(df):

    required_columns = [
        "claim_id",
        "patient_id",
        "provider_id",
        "claim_amount"
    ]

    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    df = df.dropna(subset=["claim_amount"])

    df = df[df["claim_amount"] > 0]

    return df