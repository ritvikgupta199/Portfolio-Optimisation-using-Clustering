# Two stage Portfolio Optimisation using Ball Mapper Algorithm
[Report](https://github.com/ritvikgupta199/Portfolio-Optimisation-using-Clustering/blob/dba9f14a8691b4b802e836974fa14ec275279f0b/MTD350_Final_Report.pdf)

## For Clustering
```
cd BallMapper
g++ ball.cpp -o ball
./ball <year> <qtr> <eps>
```
where \<year> and \<qtr> are the quarter for which clustering is to be done and \<eps> is the epsilon parameter for the Ball Mapper Algorithm.

## For Portfolio Optimisation
```
cd MeanVariance
python3 max_sharpe.py --year <year> --quarter <qtr> --select_num <select_num>
python3 meanvar.py --year <year> --quarter <qtr> --model <model>
python3 eval_portfolio.py --year <year> --quarter <qtr> --dir <dir> --model <model>
```
Here,
- \<year> and \<qtr> are the quarter using which the clusters have been created
- \<select_num> is the number of stocks to be picked from each cluster based on Sharpe ratio
- \<model> is "max_sharpe" or "min_vol" based on the optimisation objective
- \<dir> is the location where the evaluation graphs are saved

For evaluating the method for each of the avaliable quarters, run `run.sh`.

## Data sources
- Company Financials and stock prices from [AlphaVantage API](https://www.alphavantage.co/)
- S&P 500 Index values from [FRED](https://fred.stlouisfed.org/series/SP500)
