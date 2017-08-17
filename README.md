# Deep Speaker from Baidu Research
[![license](https://img.shields.io/badge/License-Apache_2.0-brightgreen.svg)](https://github.com/philipperemy/keras-attention-mechanism/blob/master/LICENSE) 
[![dep2](https://img.shields.io/badge/Keras-2.0+-brightgreen.svg)](https://keras.io/) 
[![dep1](https://img.shields.io/badge/Status-Work_In_Progress-orange.svg)](https://www.tensorflow.org/) 

Deep Speaker: an End-to-End Neural Speaker Embedding System https://arxiv.org/pdf/1705.02304.pdf

Work accomplished so far:
- [x] Triplet loss
- [x] Triplet loss test
- [x] Model implementation
- [x] Data pipeline implementation. We're going to use the [LibriSpeech dataset](http://www.openslr.org/12/) with 2300+ different speakers.
- [ ] Train the models 

<p align="center">
  <img src="assets/1.png" width="400">
  <br><i>Visualization of a possible triplet (Anchor, Positive, Negative) in the cosine similarity space</i>
</p>

## Contributing

Please message me if you want to contribute. I'll be happy to hear your ideas. There are a lot of undisclosed things in the paper, such as:

- Input size to the network? Which inputs exactly?
- How many filter banks do we use?
- Sample Rate?

## LibriSpeech Dataset

Available here: http://www.openslr.org/12/

List of possible other datasets: http://kaldi-asr.org/doc/examples.html

Extract of this dataset:

```
                                                                            filenames chapter_id speaker_id dataset_id
0  /Volumes/Transcend/data-set/LibriSpeech/dev-clean/1272/128104/1272-128104-0000.wav     128104       1272  dev-clean
1  /Volumes/Transcend/data-set/LibriSpeech/dev-clean/1272/128104/1272-128104-0001.wav     128104       1272  dev-clean
2  /Volumes/Transcend/data-set/LibriSpeech/dev-clean/1272/128104/1272-128104-0002.wav     128104       1272  dev-clean
3  /Volumes/Transcend/data-set/LibriSpeech/dev-clean/1272/128104/1272-128104-0003.wav     128104       1272  dev-clean
4  /Volumes/Transcend/data-set/LibriSpeech/dev-clean/1272/128104/1272-128104-0004.wav     128104       1272  dev-clean
5  /Volumes/Transcend/data-set/LibriSpeech/dev-clean/1272/128104/1272-128104-0005.wav     128104       1272  dev-clean
6  /Volumes/Transcend/data-set/LibriSpeech/dev-clean/1272/128104/1272-128104-0006.wav     128104       1272  dev-clean
7  /Volumes/Transcend/data-set/LibriSpeech/dev-clean/1272/128104/1272-128104-0007.wav     128104       1272  dev-clean
8  /Volumes/Transcend/data-set/LibriSpeech/dev-clean/1272/128104/1272-128104-0008.wav     128104       1272  dev-clean
9  /Volumes/Transcend/data-set/LibriSpeech/dev-clean/1272/128104/1272-128104-0009.wav     128104       1272  dev-clean
```

## Training example on GPU

<p align="center">
  <img src="assets/run_gpu_1.png">
  <br><i>Training on the GPU.</i>
</p>
