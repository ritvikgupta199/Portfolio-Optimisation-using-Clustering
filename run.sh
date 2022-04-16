YEAR=2017
QTR=1
SELECT_NUM=10
EPS=0.3
DIR=select_"$SELECT_NUM"_eps_"$EPS"

mkdir graphs/"$DIR"

cd BallMapper
g++ ball.cpp -o ball
./ball $YEAR $QTR $EPS
cd ..
cd MeanVariance
python3 max_sharpe.py --year $YEAR --quarter $QTR --select_num $SELECT_NUM
python3 meanvar.py --year $YEAR --quarter $QTR
python3 eval_portfolio.py --year $YEAR --quarter $QTR --dir $DIR