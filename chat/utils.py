import csv
import pandas as pd

def load_qa_from_csv(file_path):
    rows = []
    try:
        with open(file_path, mode='r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            headers = next(reader)
            if len(headers) != 2 or headers[0].strip().lower() != 'question' or headers[1].strip().lower() != 'answer':
                raise ValueError("CSV file must contain 'question' and 'answer' columns")
            for row in reader:
                if len(row) != 2:
                    raise ValueError(f"Row has an incorrect number of fields: {row}")
                rows.append(row)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return {}

    df = pd.DataFrame(rows, columns=['question', 'answer'])

    # Strip whitespace from column names and values
    df.columns = df.columns.str.strip()
    df['question'] = df['question'].str.strip()
    df['answer'] = df['answer'].str.strip()

    # Create dictionary from the DataFrame
    qa_dict = {row['question']: row['answer'] for _, row in df.iterrows()}
    return qa_dict
