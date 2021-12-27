# author: Pham Quang Binh
# phone: 0947 454 059
# email: bnh.quang@gmail.com


import click
from trans_analytic_3 import find_product_by_user, find_top_users
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
@click.option('-na', is_flag=True,
              help='Drop null value in dataset', default=True)
@click.option('-fail', is_flag=True,
              help='Allow to get ALL transactions (Not only check SUCCESS transactions)',
              default=True)
def run(input, output, na, fail):
    PATH = input
    OUTPUT = output

    # read csv
    try:
        df = pd.read_csv(PATH)
    except:
        print("Can not read csv !")
        return
    if na:
        print("Drop null value !")
        df = df.dropna()

    top_10_users = find_top_users(df, accept_failed=fail)

    # get second product of each user
    result = pd.DataFrame()
    for _, row in top_10_users.iterrows():
        first_product = find_product_by_user(df, row['user'])[
            ['user', 'product', 'timestamp']][1:2]
        result = result.append(first_product)

    # check empty row
    if top_10_users.shape[0] > 0:
        result = top_10_users.merge(result, on='user', how='left')
        result.to_csv(OUTPUT)
        print("Success !")
    else:
      print("Empty !")


if __name__ == '__main__':
    commands()
