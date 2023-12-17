"""
    Generate test data with a specified distribution of data types.
    
    :param num_files: The number of files to generate.
    :param file_format: The file format to save the data to. Can be 'csv', 'xlsx', or 'xlsb'.
    :param data_distribution: A dictionary with the data types as keys and the percentage of columns that should be
    
    that data type as values. The percentages should add up to 100.
    :param shape: A tuple with the number of rows and columns to generate.
    
    :return: None

    GIT COMMITS:

    V1.1 (2023-12-17)
    1) Built Profiler
    2) Obtained Output Report

    V1.0.0 (2023-12-17)
    1) Built v1 Data Engine

"""

import pandas as pd
from faker import Faker
import os
import datetime
from profiler import Profiler


@Profiler
class DataGenerator:
    def __init__(self):
        self.fake = Faker()
        self.num_files = input("Enter the number of files to generate (default: 30): ") or 30
        self.file_format = input("Enter file format (default: 'csv'): ") or 'csv'
        self.data_distribution = input("Enter data distribution (default: {'integer': 50, 'string': 30, 'date': 20}): ") or {'integer': 50, 'string': 30, 'date': 20}
        self.shape_rows = int(input("Enter number of rows (default: 10000): ") or 10000)
        self.shape_cols = int(input("Enter number of columns (default: 40): ") or 40)
        
        self.shape = (self.shape_rows, self.shape_cols)

        self.generate_data(self, self.num_files, self.file_format, self.data_distribution, self.shape_rows, self.shape_cols)


    @Profiler
    def generate_distribution_data(self, data_distribution, shape_rows, shape_cols):
        data = {}
        total_columns = shape_cols
        data_types = ['integer', 'string', 'date']
        data_generators = [self.fake.random_int, self.fake.word, self.fake.date]

        for data_type, proportion in data_distribution.items():
            generator = data_generators[data_types.index(data_type)]
            num_columns = round(proportion * total_columns / 100)
            for j in range(num_columns):
                data[f'{data_type}_{j}'] = [generator() for _ in range(shape_rows)]

        return data


    @Profiler
    def generate_data(self, num_files, file_format, data_distribution, shape_rows, shape_cols):
        fake = Faker()
        data_types = ['integer', 'string', 'date']
        data_generators = [fake.random_int, fake.word, fake.date]

        for i in range(num_files):
            data = self.generate_distribution_data(self, self.data_distribution, self.shape_rows, self.shape_cols)
            df = pd.DataFrame(data)

            # If there are more columns in the DataFrame than specified in the shape, drop the extra columns
            if df.shape[1] > shape_cols:
                df = df.iloc[:, :shape_cols]

            # Save the DataFrame to a file in the specified format
            directory = 'data_analysis\\data'
            if not os.path.exists(directory):
                os.makedirs(directory)
            date_string = datetime.datetime.now().strftime("_%Y%m%d")
            filename = os.path.join(directory, f'test_data_{i+1}{date_string}.{file_format}')
            if file_format == 'csv':
                df.to_csv(filename, index=False)
            elif file_format == 'xlsx':
                df.to_excel(filename, index=False)
            elif file_format == 'xlsb':
                df.to_excel(filename, index=False, engine='pyxlsb')


def main():
    DataGenerator()


if __name__ == "__main__":
    main()
