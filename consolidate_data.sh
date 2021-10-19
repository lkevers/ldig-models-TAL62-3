#!/bin/bash

cat corsican/corsicanCorp_cos_LEARN1_max.txt > data/set01_learn_max.txt
cat tatoeba/tatoeba_*_LEARN1_max.txt >> data/set01_learn_max.txt

cat corsican/corsicanCorp_cos_LEARN1_min.txt > data/set01_learn_min.txt
cat tatoeba/tatoeba_*_LEARN1_min.txt >> data/set01_learn_min.txt

cp corsican/corsicanCorp_cos_TEST1_*.txt data/
cp tatoeba/tatoeba_*_TEST1_*.txt data/

cat corsican/corsicanCorp_cos_LEARN2_max.txt > data/set02_learn_max.txt
cat tatoeba/tatoeba_*_LEARN2_max.txt >> data/set02_learn_max.txt

cat corsican/corsicanCorp_cos_LEARN2_min.txt > data/set02_learn_min.txt
cat tatoeba/tatoeba_*_LEARN2_min.txt >> data/set02_learn_min.txt

cp corsican/corsicanCorp_cos_TEST2_*.txt data/
cp tatoeba/tatoeba_*_TEST2_*.txt data/

cat corsican/corsicanCorp_cos_LEARN3_max.txt > data/set03_learn_max.txt
cat tatoeba/tatoeba_*_LEARN3_max.txt >> data/set03_learn_max.txt

cat corsican/corsicanCorp_cos_LEARN3_min.txt > data/set03_learn_min.txt
cat tatoeba/tatoeba_*_LEARN3_min.txt >> data/set03_learn_min.txt

cp corsican/corsicanCorp_cos_TEST3_*.txt data/
cp tatoeba/tatoeba_*_TEST3_*.txt data/

cat corsican/corsicanCorp_cos_LEARN4_max.txt > data/set04_learn_max.txt
cat tatoeba/tatoeba_*_LEARN4_max.txt >> data/set04_learn_max.txt

cat corsican/corsicanCorp_cos_LEARN4_min.txt > data/set04_learn_min.txt
cat tatoeba/tatoeba_*_LEARN4_min.txt >> data/set04_learn_min.txt

cp corsican/corsicanCorp_cos_TEST4_*.txt data/
cp tatoeba/tatoeba_*_TEST4_*.txt data/

cat corsican/corsicanCorp_cos_LEARN5_max.txt > data/set05_learn_max.txt
cat tatoeba/tatoeba_*_LEARN5_max.txt >> data/set05_learn_max.txt

cat corsican/corsicanCorp_cos_LEARN5_min.txt > data/set05_learn_min.txt
cat tatoeba/tatoeba_*_LEARN5_min.txt >> data/set05_learn_min.txt

cp corsican/corsicanCorp_cos_TEST5_*.txt data/
cp tatoeba/tatoeba_*_TEST5_*.txt data/

sed -i -e 's/\t/\t\t/' data/*.txt
