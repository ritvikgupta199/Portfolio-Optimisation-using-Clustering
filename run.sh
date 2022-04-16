YEAR = 2017
QTR = 3

cd BallMapper
g++ ball.cpp -o ball
./ball $YEAR $QTR
cd ..
cd MeanVariance
python3 max_sharpe.py --year $YEAR --quarter $QTR
python3 mean_variance.py --year $YEAR --quarter $QTR
python3 eval_portfolio.py --year $YEAR --quarter $QTR