# Chương trình MoMo Talents 2021 - Tech Superheroes
## Installation
```
git clone https://github.com/BinhPhamQuang/MoMo_Talents_2021.git
cd MoMo_Talents_2021
pip3 install -r requirements.txt
```
## Usage
### Excercies 1
```
python3 trans_analytic_1.py run --input=[path] --output=[path]
```
Required arguments:
```
--input : Path to CSV file.
--output: Path to export data.
```
Example:
```
python3 trans_analytic_1.py run --input="input/input_data.csv" --output="output/output_1.csv"
```
### Excercies 2
```
python3 trans_analytic_2.py run --input=[path] --output=[path]
```
Required arguments:
```
--input : Path to CSV file.
--output: Path to export data.
```
Example:
```
python3 trans_analytic_2.py run --input="input/input_data.csv" --output="output/output_2.csv"
```
### Excercies 3
```
python3 trans_analytic_3.py run --input=[path] --output=[path]
```
Required arguments:
```
--input : Path to CSV file.
--output: Path to export data.
```
Optional arguments:
| Parameter                 | Default       | Description   |	
| :------------------------ |:-------------:| :-------------|
| -na 	       |	True           | Remove all rows with null values in the data set.
| -fail          | True         | Allow to get ALL transactions (success and NOT Success transactions).

Example 1:
```
python3 trans_analytic_3.py run --input="input/input_data.csv" --output="output/output_3.csv"
```
Example 2: Not allow to drop null value:
```
python3 trans_analytic_3.py run  --input="input/input_data.csv" --output="output/output_3.csv" -na
```
### Excercies 4
```
python3 trans_analytic_4.py run --input=[path] --output=[path]
```
Required arguments:
```
--input : Path to CSV file.
--output: Path to export data.
```
Optional arguments:
| Parameter                 | Default       | Description   |	
| :------------------------ |:-------------:| :-------------|
| -na 	       |	True           | Remove all rows with null values in the data set.
| -fail          | True         | Allow to get ALL transactions (success and NOT Success transactions).

Example 1:
```
python3 trans_analytic_4.py run --input="input/input_data.csv" --output="output/output_4.csv"
```
Example 2: Not allow to get FAILED transactions:
```
python3 trans_analytic_4.py run  --input="input/input_data.csv" --output="output/output_4.csv" -fail
```