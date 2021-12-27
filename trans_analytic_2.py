# author: Pham Quang Binh
# phone: 0947 454 059
# email: bnh.quang@gmail.com

import click
from typing import List
import pandas as pd

PATH = ''
#PATH = 'input/test.csv'
OUTPUT = ''
SUCCESS = 2
LIMIT = 10


@click.group()
def commands():
    pass


@commands.command()
@click.option('--input', help='Path to csv')
@click.option('--output', help='Path to write data')
def run(input, output):
    # put your logic here
    PATH = input
    OUTPUT = output

    # read csv
    try:
        df = pd.read_csv(PATH)
    except:
        print("Can not read csv !")
        return
    # Do not drop null columns in this excerices !
    # Group by product and count transaction
    result = df.groupby(df['product'])\
        .id.count()\
        .reset_index(name="count")\
        .sort_values(by=['count'], ascending=False)\
        .head(LIMIT)
    # Export to csv
    result.to_csv(OUTPUT)
    print("Success !")


if __name__ == '__main__':
    commands()
