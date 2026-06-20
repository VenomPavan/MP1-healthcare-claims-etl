def validate(df):

    required_columns = [
        "claim_id",
        "patient_id",
        "provider_id",
        "claim_amount",
        "claim_date"
    ]

    # Column Check
    for col in required_columns:
        if col not in df.columns:
            raise Exception(f"Missing required column: {col}")

    # Null Check
    if df["claim_amount"].isnull().any():
        raise Exception("Null Claim Amount Found")

    # Negative Amount Check
    if (df["claim_amount"] < 0).any():
        raise Exception("Negative Claim Amount Found")

    # Duplicate Check
    if df["claim_id"].duplicated().any():
        raise Exception("Duplicate Claim IDs Found")

    print("Validation Passed")

    return df