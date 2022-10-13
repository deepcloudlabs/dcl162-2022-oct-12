# data -> information (data + metadata) -> knowledge (AI)
import pandas as pd

df = pd.DataFrame([
    ["1", "jack bauer", 100000.0, "tr1"],
    ["2", "kate austen", 200000.0, "tr2"],
    ["3", "james sawyer", 300000.0, "tr3"],
    ["4", "sun kwon", 400000.0, "tr4"]
], columns=["identity", "fullname", "salary", "iban"])

df.to_csv("employees_pandas.csv")
