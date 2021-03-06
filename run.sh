YEAR=2017
QTR=1
SELECT_NUM=2
EPS=0.2
# MODEL="max_sharpe"
MODEL="min_vol"

while [ $QTR -le 4 ]
do
    while [ $YEAR -le 2021 ]
    do 
        DIR=select_"$SELECT_NUM"_eps_"$EPS"

        mkdir -p graphs/"$DIR"

        cd BallMapper
        g++ ball.cpp -o ball
        ./ball $YEAR $QTR $EPS
        cd ..
        cd MeanVariance
        python3 max_sharpe.py --year $YEAR --quarter $QTR --select_num $SELECT_NUM
        python3 meanvar.py --year $YEAR --quarter $QTR --model $MODEL
        python3 eval_portfolio.py --year $YEAR --quarter $QTR --dir $DIR --model $MODEL
        ((YEAR++))
        cd ..
    done
    YEAR=2017
    ((QTR++))
done