# author: Pham Quang Binh
# phone: 0947 454 059
# email: bnh.quang@gmail.com
import click
import pandas as pd

PATH = ''
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
    # read data
    try:
        df = pd.read_csv(PATH)
    except:
        print("Can not read csv !")
        return
    # Check null columns
    df.isnull().sum(axis=0)
    """
  Because Row 'users' has 3816 null columns. 
  So drop null columns of this row. (For this exercise)
  """
    df = df.dropna()

    # Group by user and count transactions
    result = df[df.status == SUCCESS]\
        .groupby(df.user)\
        .status.count()\
        .reset_index(name="count")\
        .sort_values(by=['count'], ascending=False)\
        .head(LIMIT)
    # Export to csv
    result.to_csv(OUTPUT)
    print("Success !")


if __name__ == '__main__':
    commands()
