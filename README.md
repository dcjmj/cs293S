# CS293S PROJECT
#### Tao Huang, Huanhua Xu
This is our CS293S PROJECT, based on Pytorch implementation of paper "Efficient Document Retrieval by End-to-End Refining and Quantizing BERT Embedding with Contrastive Product Quantization"(EMNLP 2022).
We introduced multi-teacher distillation on this Bert-Base model to reduce the time consumption on fine-tuning and inference. Moreover, to improve the individuality of codewords for keeping
the sematic information of documents soundly, we proposed to minimize the similarity between different codebooks.

### Main Dependencies

- pytorch 1.7.1
- transformers 4.24.0

### How to Run

```shell
# An example. 
# Run on the NYT Ddataset, 16-bit setting.
python main.py nyt16 ./data/nyt --train --cuda --seed 0 --prob_weight 0.1 --cond_ent_weight 0.1 --L_word 24 --N_books 4 --N_words 16 --batch_size 64 --epochs 100 --lr 0.001 --encode_length 16 --max_length 400  --gumbel_temperature 10.0 --dist_metric euclidean --code_weight 1.0
```
