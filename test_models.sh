#!/bin/bash

# $1 : model dir
# $2 : set number

echo "cos T"
python3 ../ldig-python3/ldig.py -m $1 data/corsicanCorp_cos_TEST$2_50.txt
echo "cos S"
python3 ../ldig-python3/ldig.py -m $1 data/corsicanCorp_cos_TEST$2_300.txt
echo "cos M"
python3 ../ldig-python3/ldig.py -m $1 data/corsicanCorp_cos_TEST$2_3000.txt
echo "cos L"
python3 ../ldig-python3/ldig.py -m $1 data/corsicanCorp_cos_TEST$2_greater.txt

echo "eng T"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_eng_TEST$2_50.txt
echo "eng S"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_eng_TEST$2_300.txt
echo "eng M"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_eng_TEST$2_3000.txt
echo "eng L"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_eng_TEST$2_greater.txt

echo "ita T"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_ita_TEST$2_50.txt
echo "ita S"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_ita_TEST$2_300.txt
echo "ita M"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_ita_TEST$2_3000.txt
echo "ita L"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_ita_TEST$2_greater.txt

echo "deu T"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_deu_TEST$2_50.txt
echo "deu S"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_deu_TEST$2_300.txt
echo "deu M"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_deu_TEST$2_3000.txt
echo "deu L"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_deu_TEST$2_greater.txt

echo "fra T"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_fra_TEST$2_50.txt
echo "fra S"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_fra_TEST$2_300.txt
echo "fra M"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_fra_TEST$2_3000.txt
echo "fra L"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_fra_TEST$2_greater.txt

echo "por T"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_por_TEST$2_50.txt
echo "por S"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_por_TEST$2_300.txt
echo "por M"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_por_TEST$2_3000.txt
echo "por L"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_por_TEST$2_greater.txt

echo "spa T"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_spa_TEST$2_50.txt
echo "spa S"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_spa_TEST$2_300.txt
echo "spa M"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_spa_TEST$2_3000.txt
echo "spa L"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_spa_TEST$2_greater.txt

echo "hun T"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_hun_TEST$2_50.txt
echo "hun S"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_hun_TEST$2_300.txt
echo "hun M"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_hun_TEST$2_3000.txt
echo "hun L"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_hun_TEST$2_greater.txt

echo "nld T"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_nld_TEST$2_50.txt
echo "nld S"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_nld_TEST$2_300.txt
echo "nld M"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_nld_TEST$2_3000.txt
echo "nld L"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_nld_TEST$2_greater.txt

echo "fin T"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_fin_TEST$2_50.txt
echo "fin S"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_fin_TEST$2_300.txt
echo "fin M"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_fin_TEST$2_3000.txt
echo "fin L"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_fin_TEST$2_greater.txt

echo "pol T"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_pol_TEST$2_50.txt
echo "pol S"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_pol_TEST$2_300.txt
echo "pol M"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_pol_TEST$2_3000.txt
echo "pol L"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_pol_TEST$2_greater.txt

echo "lit T"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_lit_TEST$2_50.txt
echo "lit S"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_lit_TEST$2_300.txt
echo "lit M"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_lit_TEST$2_3000.txt
echo "lit L"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_lit_TEST$2_greater.txt

echo "ces T"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_ces_TEST$2_50.txt
echo "ces S"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_ces_TEST$2_300.txt
echo "ces M"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_ces_TEST$2_3000.txt
echo "ces L"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_ces_TEST$2_greater.txt

echo "dan T"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_dan_TEST$2_50.txt
echo "dan S"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_dan_TEST$2_300.txt
echo "dan M"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_dan_TEST$2_3000.txt
echo "dan L"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_dan_TEST$2_greater.txt

echo "swe T"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_swe_TEST$2_50.txt
echo "swe S"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_swe_TEST$2_300.txt
echo "swe M"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_swe_TEST$2_3000.txt
echo "swe L"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_swe_TEST$2_greater.txt

echo "ell T"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_ell_TEST$2_50.txt
echo "ell S"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_ell_TEST$2_300.txt
echo "ell M"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_ell_TEST$2_3000.txt
echo "ell L"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_ell_TEST$2_greater.txt

echo "ron T"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_ron_TEST$2_50.txt
echo "ron S"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_ron_TEST$2_300.txt
echo "ron M"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_ron_TEST$2_3000.txt
echo "ron L"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_ron_TEST$2_greater.txt

echo "bul T"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_bul_TEST$2_50.txt
echo "bul S"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_bul_TEST$2_300.txt
echo "bul M"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_bul_TEST$2_3000.txt
echo "bul L"
python3 ../ldig-python3/ldig.py -m $1 data/tatoeba_bul_TEST$2_greater.txt

