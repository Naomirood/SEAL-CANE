
## MSc Thesis - Naomi Rood
### Information Studies, Track Data Science

Welcome to the GitHub page of Link Prediction based on Graph Neural Networks using Textual Data for Recommending Dutch News Articles. 
<br />

## Project Folder Structure

- [``Code``](Code/): The Python code, the data folder(no data) and the EDA notebook. 
- [``Literature``](Literature/): The two papers of SEAL and CANE.
- [``Thesis``](Thesis/): The final thesis.

## Requirements and Installation
To clone this repository 
```
git clone https://github.com/Naomirood/Thesis
```
Use the following line to install the required software and libraries, run the line in the [``Code``](Code/) folder. It will download and install the default graph neural network software of Zhang et al. (2018) [pytorch_DGCNN](https://github.com/muhanzhang/pytorch_DGCNN) to the same level as the root folder (only suitable for MacOS and Linux).
```
bash ./install.sh
```
<br />
The code is last tested on the versions of the following dependencies:
<br />
Python == 3.7.9 <br />
TensorFlow == 2.12.2 <br />

## Usage
To train the model and predict scores, run one of the following lines in the the [``Python``](Code/Python) folder. <br />

To run the code, it is necessary to have a .mat file in the [``data``](Code/Python/data) folder. It must contain a *net* variable with all the links in the original network, it is optional to have a *group* variable with the atrributes of the nodes. If the nodes have correponding text, these must be in the *text* variable. <br />

To run the model and have a try of the framework, type:
```
python3 Main.py --data-name links_1m --use-cane-embedding --hop 'auto' 
```
this will automatically output the AUC score and uses the default test split of 10% (append "--test-ratio" to change this ratio). To use the SEAL method with only subgraphs, don't use embedding. Instead of using CANE embedding, it is also possible to use Node2vec embedding (for example when having no *text* in the .mat file. Use then: --use-n2v-embedding. Hop number set atuotmatically from {1,2}, if you want to select a specific hop number, set "--hop 1". Instead of using CANE embeddings, it is possible to use node2vec embedding, this does not require *text* in the .mat file, use "--use-n2v-embedding". <br />

To try SEAL + CANE on a custom split of the links, it is necessery to make txt files of the train and valiation set. <br />
If you want to output the link existence probablities on the test set, first type:
```
 python3 Main.py --data-name links_1m --use-cane-embedding --hop 'auto' --train-name links_1m_train.txt --test-name links_1m_val.txt --save-model
```
here, the "--save-model" saves the final model to "data/data_name.pth". To predict link existence probablities to the test set (may contain both positive and negative links), type to load the save model and output predictions to "data/test_name_pred.txt":
```
 python3 Main.py --data-name links_1m --use-cane-embedding --hop 'auto' --train-name links_1m_train.txt --test-name links_1m_val.txt --only-predict
```
The only-predict argument will automatically print the recall scores (treshold of 0.5, 0.7 and 0.9) for the test set. If you want what the model learns from node attributes as well, append "--use-attribute". This is only possible when there is a *group* within the .mat file.

To change the number of epochs, layers of the GNN or a different parameter for the SEAL training process, you can update the paramters in [``Main.py``](Code/Python/Main.py) <br />
To change the number of epochs, max_len of the text or a different parameter for the CANE training process, you can update [``config.py``](Code/Python/config.py) <br />

<br /> 
For a full overview of the arugments, take a look at the [``Main.py``](Code/Python/Main.py) file. <br /> 


## Acknowledgements

This research was conducted as a master thesis information studies: data science at the University of Amsterdam. This work is written in colaboration with the NOS (the Dutch Public Broadcasting Foundation). 
<br />
Code has been used from the [CANE](https://github.com/thunlp/CANE/tree/master/code) and [SEAL](https://github.com/muhanzhang/SEAL/tree/master/Python) GitHub repository. The PyTorch implementation of DGCNN is also used from the [PyTorch DGCNN](https://github.com/muhanzhang/pytorch_DGCNN) GitHub repository. 
<br />

References of the papers of those repositories: <br />
Cunchao Tu, Han Liu, Zhiyuan Liu, Maosong Sun. *CANE: Context-Aware Network Embedding for Relation Modeling.* The 55th Annual Meeting of the Association for Computational Linguistics (ACL 2017).
<br />
Zhang, M., & Chen, Y. (2018). *Link prediction based on graph neural networks. Advances in neural information processing systems*, 31.
<br />
Zhang, M., Cui, Z., Neumann, M., & Chen, Y. (2018, April). *An end-to-end deep learning architecture for graph classification*. In Proceedings of the AAAI conference on artificial intelligence (Vol. 32, No. 1).
