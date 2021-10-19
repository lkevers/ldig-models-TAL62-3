# ldig-models-TAL62-3 : Language identification models for 17 European official languages and Corsican.

These data are related to the article "L'identification de langue, un outil au service du corse et de l'évaluation des ressources linguistiques" ("Language identification, a tool for Corsican and language resource evaluation"), by Laurent Kevers, to be published in the journal TAL 62-3 on linguistic diversity in Natural Language Processing (2022).

The language identification models cannot be distributed in a ready-to-use form due to license incompatibilities (CC BY 2.0 EN, CC BY-SA 3.0 and CC BY-NC-SA 4.0).

We therefore provide the different data under their own licenses, as well as a script to recreate the models. These scripts are available under the MIT license.

To proceed, you will need ldig-python3 (https://github.com/lkevers/ldig-python3), which will also be required for running the models once they are generated.

For more information about NLP and Corsican : https://bdlc.univ-corse.fr/tal/

## Data

Data includes sentences from Tatoeba (https://tatoeba.org/fr/downloads, CC BY 2.0) and Corsican language corpora (https://bdlc.univ-corse.fr/tal/index.php?page=res, CC BY-SA 3.0 and CC BY-NC-SA 4.0).

For Tatoeba, which contains texts for 17 official European Union languages, the data is already pre-processed and split between the learning (LEARN) and test (TEST) sets.

For each Corsican corpus (A Piazzetta, A Sacra Bibbia, Wikipedia), the pre-processed data is available in a single text file which is accompanied by an exclusion list. The division into learning and test sets must be done, using these files and the dedicated script (build_cos_datasets.py).

The specific licence information for each dataset is available in the subdirectory of each corpus.


## Steps to rebuild the models

Five models are built in order to set up a cross validation process.

For each fold, one subset of the data is reserved for training, and another for testing. The training set is available in two versions, one limited to about 500,000 characters ("min"), the other one including all the data, except those dedicated to the test ("max").

1. Build the Corsican data (LEARN/TEST sets)

        python3 build_cos_datasets.py >build_cos_datasets.log

    Input data are located into the "corsican-*" folders.

    Output files are written into the "corsican" folder. They are named as following:
    * corsicanCorp_cos_LEARN[X]_[max|min].txt : is the data selected to train the Xth fold (min or max version).
    * corsicanCorp_cos_TEST[X]_[CAT].txt : is the data selected for testing related to the Xth fold; CAT is a subdivision of the data related to the document's length.

2. Consolidate data from Tatoeba and Corsican Corpus

        bash consolidate_data.sh

    Input data are located into the "tatoeba" folder (already prepared) and corsican (generated during the previous step).

    Output files are written into the "data" directory. They are named as following:
    * set0[X]_learn_[min|max].txt

3. Generate the models

        bash generate_models.sh

    Models are generated into the "model" directory. The following subdirectories are used:
    * set0[X]/[max|min]

    Models based on data restricted to 500,000 characters are generated in minutes. Those based on the entire data are much longer to build (several hours). By default, the lines that trigger the generation of these models have been commented out in the "generate_models.sh" script.


## Using the models on TEST files

The "test_models.sh" script can be used to run the different models on the corresponding test data.

    bash test_models.sh

## Notice

The extraction of relevant features by Ldig does not give exactly the same result at each run. Small differences in performance, up or down, could therefore be observed compared to what is described in the TAL article.
