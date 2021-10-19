#!/bin/bash

echo "Model 01 min"
python3 ../ldig-python3/ldig.py -m models/set01/min -x ../ldig-python3/maxsubst/maxsubst --init data/set01_learn_min.txt
python3 ../ldig-python3/ldig.py -m models/set01/min --learn data/set01_learn_min.txt -e 0.5
python3 ../ldig-python3/ldig.py -m models/set01/min --shrink

#echo "Model 01 max"
#python3 ../ldig-python3/ldig.py -m models/set01/max -x ../ldig-python3/maxsubst/maxsubst --init data/set01_learn_max.txt
#python3 ../ldig-python3/ldig.py -m models/set01/max --learn data/set01_learn_max.txt -e 0.5
#python3 ../ldig-python3/ldig.py -m models/set01/max --shrink

echo "Model 02 min"
python3 ../ldig-python3/ldig.py -m models/set02/min -x ../ldig-python3/maxsubst/maxsubst --init data/set02_learn_min.txt
python3 ../ldig-python3/ldig.py -m models/set02/min --learn data/set02_learn_min.txt -e 0.5
python3 ../ldig-python3/ldig.py -m models/set02/min --shrink

#echo "Model 02 max"
#python3 ../ldig-python3/ldig.py -m models/set02/max -x ../ldig-python3/maxsubst/maxsubst --init data/set02_learn_max.txt
#python3 ../ldig-python3/ldig.py -m models/set02/max --learn data/set02_learn_max.txt -e 0.5
#python3 ../ldig-python3/ldig.py -m models/set02/max --shrink

echo "Model 03 min"
python3 ../ldig-python3/ldig.py -m models/set03/min -x ../ldig-python3/maxsubst/maxsubst --init data/set03_learn_min.txt
python3 ../ldig-python3/ldig.py -m models/set03/min --learn data/set03_learn_min.txt -e 0.5
python3 ../ldig-python3/ldig.py -m models/set03/min --shrink

#echo "Model 03 max"
#python3 ../ldig-python3/ldig.py -m models/set03/max -x ../ldig-python3/maxsubst/maxsubst --init data/set03_learn_max.txt
#python3 ../ldig-python3/ldig.py -m models/set03/max --learn data/set03_learn_max.txt -e 0.5
#python3 ../ldig-python3/ldig.py -m models/set03/max --shrink

echo "Model 04 min"
python3 ../ldig-python3/ldig.py -m models/set04/min -x ../ldig-python3/maxsubst/maxsubst --init data/set04_learn_min.txt
python3 ../ldig-python3/ldig.py -m models/set04/min --learn data/set04_learn_min.txt -e 0.5
python3 ../ldig-python3/ldig.py -m models/set04/min --shrink

#echo "Model 04 max"
#python3 ../ldig-python3/ldig.py -m models/set04/max -x ../ldig-python3/maxsubst/maxsubst --init data/set04_learn_max.txt
#python3 ../ldig-python3/ldig.py -m models/set04/max --learn data/set04_learn_max.txt -e 0.5
#python3 ../ldig-python3/ldig.py -m models/set04/max --shrink

echo "Model 05 min"
python3 ../ldig-python3/ldig.py -m models/set05/min -x ../ldig-python3/maxsubst/maxsubst --init data/set05_learn_min.txt
python3 ../ldig-python3/ldig.py -m models/set05/min --learn data/set05_learn_min.txt -e 0.5
python3 ../ldig-python3/ldig.py -m models/set05/min --shrink

#echo "Model 05 max"
#python3 ../ldig-python3/ldig.py -m models/set05/max -x ../ldig-python3/maxsubst/maxsubst --init data/set05_learn_max.txt
#python3 ../ldig-python3/ldig.py -m models/set05/max --learn data/set05_learn_max.txt -e 0.5
#python3 ../ldig-python3/ldig.py -m models/set05/max --shrink

