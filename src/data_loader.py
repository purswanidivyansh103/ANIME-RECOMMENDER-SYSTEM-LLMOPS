# import pandas as pd

# class AnimeDataLoader:
#     def __init__(self, original_csv: str, processed_csv: str):
#         self.original_csv = original_csv
#         self.processed_csv = processed_csv

#     def load_and_process(self) -> pd.DataFrame:
#         """Load anime data from a CSV file."""
#         df = pd.read_csv(self.original_csv, encoding='utf-8', on_bad_lines='skip').dropna()
#         required_columns = {'Name', 'Genres', 'sypnopsis'}
#         missing_columns = required_columns - set(df.columns) 
#         if missing_columns:
#             raise ValueError(f"Missing required columns: {missing_columns}")
#         df['combined_info'] = (
#             "Title: " + df['Name'] + " Overview: " + df['sypnopsis'] + " Genres: " + df['Genres']
#         )
#         df = df[['combined_info']]
#         df.to_csv(self.processed_csv, index=False, encoding='utf-8')
#         return self.processed_csv

import pandas as pd

class AnimeDataLoader:
    def __init__(self,original_csv:str,processed_csv:str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_and_process(self):
        df = pd.read_csv(self.original_csv , encoding='utf-8' , on_bad_lines='skip').dropna()

        required_cols = {'Name' , 'Genres','sypnopsis'}

        missing = required_cols - set(df.columns)
        if missing:
            raise ValueError("Missing column  in CSV File")
        
        df['combined_info'] = (
            "Title: " + df["Name"] + " Overview: " +df["sypnopsis"] + "Genres : " + df["Genres"]
        )

        df[['combined_info']].to_csv(self.processed_csv , index=False,encoding='utf-8')

        return self.processed_csv
