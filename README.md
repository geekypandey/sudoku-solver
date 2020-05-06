# Sudoku Solver
Python code to solve sudoku. The solution makes use of backtracking.

Problem: Solve the soduku puzzle

Constraints:
   - Every row must have all digits[0-9]
   - Every column must have all digits[0-9]
   - The sectors made of 3x3 square must have all digits[0-9]


### Dataset
The dataset used is downloaded from [here](https://www.kaggle.com/bryanpark/sudoku) which contains 1 million datapoints in a csv file.

```console
$ head -n 5 sudoku.csv
quizzes,solutions
004300209005009001070060043006002087190007400050083000600000105003508690042910300,864371259325849761971265843436192587198657432257483916689734125713528694542916378
040100050107003960520008000000000017000906800803050620090060543600080700250097100,346179258187523964529648371965832417472916835813754629798261543631485792254397186
600120384008459072000006005000264030070080006940003000310000050089700000502000190,695127384138459672724836915851264739273981546946573821317692458489715263562348197
497200000100400005000016098620300040300900000001072600002005870000600004530097061,497258316186439725253716498629381547375964182841572639962145873718623954534897261
```

For testing of the solution a subset of 1000 randomly selected games were used. Random selection was done as:

`head -n 1 sudoku.csv >> sudoku_small.csv && tail -1000000 sudoku.csv | shuf -n 1000 >> sudoku_small.csv`


### Running Tests
Create a virtual environment and install requirements.txt
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

To run test:
```
$ pytest tests.py
```

