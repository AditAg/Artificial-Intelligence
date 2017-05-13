#!/bin/bash
hunpos-train mytagger -t 2 <train.txt
hunpos-tag mytagger < devdata.txt>outputlabelsdev.txt
python accuracypredictdev.py 2 >predictedmeasuresdev.txt
python tuning.py
hunpos-train mytagger -t 3 <train.txt
hunpos-tag mytagger < devdata.txt>outputlabelsdev.txt
python accuracypredictdev.py 3 >predictedmeasuresdev.txt
python tuning.py
echo "The final FScore for development dataset is:"
cat finalpredictedmeasure.txt
echo -e "\n"

z=$(cat predictedt.txt)
echo "Finally the value for the parameter t is:"$z
hunpos-train mytagger -t $z <train.txt
hunpos-tag mytagger < testdata.txt>outputlabels.txt
python accuracypredict.py $z >predictedmeasures.txt
echo "The final scores are for test dataset :"
cat predictedmeasures.txt
echo -e "\n"




