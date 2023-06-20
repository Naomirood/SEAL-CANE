
## MSc Thesis - Naomi Rood
### Information Studies, Track Data Science

Welcome to the GitHub page of Link Prediction based on Graph Neural Networks using Textual Data for Recommending Dutch News Articles. 
<br />

## Project Folder Structure

- [``Code``](Code/): The Python code and the data folder. 
- [``Literature``](Literature/): The two most important articles.
- [``Thesis``](Thesis/): The final thesis.

## Requirements and Installation
To clone this repository 
```
git clone https://github.com/Naomirood/Thesis
```
Use the following line to install the required software and libraries, run the line in the [Code](Code/) folder. It will download and install the default graph neural network software of Zhang et al. (2018) [pytorch_DGCNN](https://github.com/muhanzhang/pytorch_DGCNN) to the same level as the root folder (only suitable for MacOS and Linux).
```
bash ./install.sh
```
<br />
The code is last tested on the versions of the following dependencies:
<br />
Python == 3.7.9 <br />
TensorFlow == 2.12.2 <br />

## Usage
To train the model and predict scores. 


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
