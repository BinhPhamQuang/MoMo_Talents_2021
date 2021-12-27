# author: Pham Quang Binh
# phone: 0947 454 059
# email: bnh.quang@gmail.com

import click
import pandas as pd
PATH = ''
#PATH = 'input/test.csv'
OUTPUT = ''
SUCCESS = 2
LIMIT = 10


def find_top_users(df: pd.DataFrame, limit=LIMIT, accept_failed=True) -> pd.DataFrame:
    """
    Find N (default 10) users with  the most transactions (Accept FAILED transactions )
    If check only SUCCESS transactions, please make accept_failed = False
    """
    if accept_failed:
        data = df.groupby(df['user'])\
            .id.count()\
            .reset_index(name="count")\
            .sort_values(by=['count'], ascending=False)\
            .head(limit)
    else:
        data = df[df.status == SUCCESS]\
            .groupby(df['user'])\
            .id.count()\
            .reset_index(name="count")\
            .sort_values(by=['count'], ascending=False)\
            .head(limit)
    return data


def find_product_by_user(df: pd.DataFrame, user_id: str) -> pd.DataFrame:
    """
    Get All DISTICNT products bought by user (Order by timestamp ASC)
    """
    products = df[df['user'] == user_id]
    # order by timestamp
    products = products.sort_values(by=['timestamp'], ascending=True)\
        # select DISTICNT product
    products = products.drop_duplicates(subset='product')
    # return result
    return products


@click.group()
def commands():
    pass


@commands.command()
@click.option('--input', help='Path to csv')
@click.option('--output', help='Path to write data')
@click.option('-na', is_flag=True, help='Drop null value in dataset', default=True)
@click.option('-fail', is_flag=True, help='Allow to get all transaction (Not only for success transaction)', default=True)
def run(input, output, na, fail):
    # put your logic here
    PATH = input
    OUTPUT = output

    # read csv
    try:
        df = pd.read_csv(PATH)
    except:
        print("Can not read csv !")
        return
    # drop na value
    if na:
        print("Drop null value !")
        df = df.dropna()

    top_10_users = find_top_users(df, accept_failed=fail)

    # get first product of each user
    result = pd.DataFrame()
    for _, row in top_10_users.iterrows():
        first_product = find_product_by_user(df, row['user'])[
            ['user', 'product', 'timestamp']].iloc[:1]
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
