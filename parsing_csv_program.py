from Utils.csv_file_parser import load_csv_to_df, add_converted_column_on_df, output_df_to_csv

if __name__ == '__main__':
    df = load_csv_to_df()
    df = add_converted_column_on_df(df)
    output_df_to_csv(df)

    print('successful output')
