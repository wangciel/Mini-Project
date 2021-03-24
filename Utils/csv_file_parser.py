import pandas as pd
import os
from Utils.timezone_converter_utils import convert_timestamp_with_coordinates

# hyper parameter could use config.ini file in further
if os.path.isfile('./Input_csv_files/timezone.csv'):
    original_csv_file_dir = './Input_csv_files/timezone.csv'
    modified_csv_file_dir = './Input_csv_files/timezone_modified.csv'
else:
    original_csv_file_dir = '../Input_csv_files/timezone.csv'
    modified_csv_file_dir = '../Input_csv_files/timezone_modified.csv'


def load_csv_to_df(csv_file=original_csv_file_dir):
    """ load modified file if exist otherwise load original file"""
    if os.path.isfile(modified_csv_file_dir):
        df = pd.read_csv(modified_csv_file_dir)
    else:
        df = pd.read_csv(csv_file)
    return df


def add_converted_column_on_df(target_df, col_name='local_time'):
    target_df[col_name] = target_df.apply(
        lambda row: convert_timestamp_with_coordinates(row['lat'], row['lng'], row["timestamp_utc"]), axis=1)
    return target_df


def output_df_to_csv(target_df, output_dir=modified_csv_file_dir):
    target_df.to_csv(output_dir, index=False)


def retrieve_all_converted_time():
    """ for request GET ALL """
    df = load_csv_to_df()

    target_df = add_converted_column_on_df(df)

    return {row["id"]: row["local_time"] for index, row in target_df.iterrows()}


def retrieve_converted_time_by_id(id):
    """ for request GET ID """
    df = load_csv_to_df()

    target_df = add_converted_column_on_df(df)

    target_row = target_df.loc[target_df['id'] == str(id)]
    return target_row['local_time'].values


def add_collection_by_id(id, row):
    """ for request POST with ID """
    df = load_csv_to_df()

    if df.loc[df['id'] == str(id)].empty:
        new_row_df = pd.DataFrame.from_dict(row)
        df = pd.concat([df, new_row_df])
        output_df_to_csv(df)
    else:
        output_df_to_csv(df)
        return {}

    target_df = add_converted_column_on_df(df)

    return {row["id"]: row["local_time"] for index, row in target_df.iterrows()}


def update_all_column_by_id(id, row):
    """ for request PUT with ID """
    df = load_csv_to_df()

    if df.loc[df['id'] == str(id)].empty:
        new_row_df = pd.DataFrame.from_dict(row)
        df = pd.concat([df, new_row_df])
        output_df_to_csv(df)

        return False
    else:
        for key in row.keys():
            df.loc[df['id'] == str(id)][key] = row.get(key)

        output_df_to_csv(df)
        return True


def delete_collection_by_id(id):
    """ for request DELETE with ID """

    df = load_csv_to_df()

    if not df.loc[df['id'] == str(id)].empty:
        df = df.drop(df[df['id'] == str(id)].index)
        output_df_to_csv(df)

        return True

    output_df_to_csv(df)
    return False
