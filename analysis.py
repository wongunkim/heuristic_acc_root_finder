def analyze_results(results_df, test_type="I"):
    test_data = results_df[results_df["test_type"] == test_type].copy()
    test_data["correct"] = (test_data["m"] == 0) == (test_data["result"] == 0)
    test_data["incorrect"] = ~test_data["correct"]
    summary = (
        test_data.groupby(["d", "m", "sigma","isolation"])
        .agg(
            {
                #"isolation": "isolation",
                "incorrect": "sum",
                "num_NIR_evals": "max",
                "h": "max",
            }
        )
        .rename(columns={"num_NIR_evals": "max_evals", "h": "max_h"})
        .reset_index()
    )
    return summary[["d", "m", "sigma", "isolation", "incorrect", "max_evals", "max_h"]]
