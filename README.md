# Image Restoration by Selective Residual Block on Improved Hierarchical Encoder-Decoder Networks  

## [Chi-Mao Fan](https://github.com/FanChiMao), Tsung-Jung Liu, Kuan-Hsien Liu  

> Abstract : Image Restoration is a compute vision task which
restoring from the degraded images to clean images. With the
rapid development of both hardware and software equipment,
convolution neural network (CNN) which needs higher equipment
requirements gradually replaces the traditional algorithm-based
restoration methods, and shine in each domain of compute vision
and achieve the impressive performance. However, with the rapid
development of hardware equipment, the trend of convolution
neural network gradually becomes a clammy situation which
stacking huge complex network structures to achieve excellent
performances, while ignoring the efficiency of model. In this
paper, we based on light hierarchical network architecture: UNet,
and improve from Residual Dense Block (RDB) which is
good at image restoration tasks but memory-consuming to an
efficient block called Selective Residual Block (SRB). We also
improve the hierarchical network structure U-Net by adding
the gatepost feature paths which enrich more spatial feature
information comparing with the traditional U-Net and have
the synergy with SRB. Besides this, we also proposed a loss
function which is based on two important metrics in image
restoration: peak signal-to-noise (PSNR) and structural similarity
index to optimize our model. Finally, proposed network could
handle the several restoration tasks such as denoising and
deraining. Furthermore, the performances are promising in terms
of quantitative metrics and visual quality.

## Network Architecture  
<table>
  <tr>
    <td colspan="2"><img src = "https://i.imgur.com/SbUotcA.png" alt="SRMNet" width="800"> </td>  
  </tr>
  <tr>
    <td colspan="2"><p align="center"><b>Overall Framework of SRMNet</b></p></td>
  </tr>
  
  <tr>
    <td> <img src = "https://i.imgur.com/z6Vds87.png" width="400"> </td>
    <td> <img src = "https://i.imgur.com/WlhzTdx.png" width="400"> </td>
  </tr>
  <tr>
    <td><p align="center"><b>Selective Residual Block (SRB)</b></p></td>
    <td><p align="center"> <b>Wavelet Thresholding Feature Fusion (WTFF)</b></p></td>
  </tr>
</table>


## Installation
The model is built in PyTorch 1.8.0 and tested on Windows10 environment  
(Python: 3.8, CUDA: 10.2, cudnn: 7.6).  

For installing, follow these intructions (download correct version of pytorch!)
```
conda create -n pytorch python=3.8  
conda activate pytorch  
conda install pytorch=1.8 torchvision cudatoolkit=10.2 -c pytorch  
conda install -c conda-forge tensorboardx
pip install -r requirements.txt
```
## Prepare datasets  
The preparation of dataset in more detail, see [**datasets/README.md**](datasets/README.md).  
In our experiments, we crop both training & testing data with the size of `256x256` by the preprocess codes in `./datasets`.  

## Train  
To train the restoration models of SRMNet. You should check the following components are correct:  
<details>  
<summary>training.yaml (Take real-world defoucs blur for example)  </summary>   
  
 ```
  # Training configuration
    GPU: [0,1,2,3]

    VERBOSE: False

    MODEL:
      MODE: 'Deblurring_DPDD_5e-4to1e-4_L1DCTEdge'
      SESSION: 'CMFNet'

    # Optimization arguments.
    OPTIM:
      BATCH: 1
      EPOCHS: 100
      # NEPOCH_DECAY: [10]
      LR_INITIAL: 5e-4
      LR_MIN: 1e-4
      # BETA1: 0.9

    TRAINING:
      VAL_AFTER_EVERY: 1
      RESUME: True
      TRAIN_PS: 256
      VAL_PS: 256
      TRAIN_DIR: './dataset/Deblur/REDS_patch/train'       # path to training data
      VAL_DIR: './dataset/Deblur/REDS_patch/test' # path to validation data
      SAVE_DIR: './checkpoints'           # path to save models and images
  ```
</details>  

If the data path and above configuration are all correctly setting, just simply run:  
```
python train.py
```  

## Demo
To demo the deblurring models and acquire the visual results, please check the parameters in [**demo.py**](demo.py) and run: 
```
python demo.py
```  

## Test  
To test (evaluate) the quantitative scores of different datasets, see [**`evaluation_codes`**](evaluation_codes).  

## Visual results  

| Task | Training Set | Testing Set | SRMNet's Visual Results|
|:---:|:---:|:---:|:---:|
|Denoising (Synthesized gaussian noise)|DIV2K train|CBSD68 | [Download](https://drive.google.com/drive/folders/1yXzUa6E4MAspijBz_rdCvvG55b6dovAt?usp=sharing) |
|Denoising (Synthesized gaussian noise)|DIV2K train|Kodak24| [Download](https://drive.google.com/drive/folders/1qKabGPr3G09xO07DoHIEQ9yJaGNHjfmk?usp=sharing) |
|Denoising (Real-world noise)  |SIDD medium | SIDD|[Download](https://drive.google.com/drive/folders/1LFbHBuV5Xh_shPcksTi2GIrkvsnA2xaE?usp=sharing) |
|Denoising (Real-world noise)  |SIDD medium| DND  | [Download](https://drive.google.com/drive/folders/1-KHHKxaB5HX8AcJA7IDR4w5YLQKEihJ-?usp=sharing) |
|Deraining (Synthesized rainstreak)| Rain13k | Rain100L | [Download](https://drive.google.com/drive/folders/1nvSOPpWPbZbP1ynWW7k__oaJKg6GLYBT?usp=sharing/) |
|Deraining (Synthesized rainstreak)| Rain13k | Rain100H | [Download](https://drive.google.com/drive/folders/1ISZS48gtDELwo7ZoIukrJ5lxeK9rnqqd?usp=sharing) |
|Deraining (Synthesized rainstreak)| Rain13k | Test100 | [Download](https://drive.google.com/drive/folders/1d9JeN3fhor6heCEV_eqPhdSck6RUnwpV?usp=sharing) |
|Deraining (Synthesized rainstreak)| Rain13k | Test1200 | [Download](https://drive.google.com/drive/folders/18pdWHLME-3V9cjfAXDX0-beD2H4Bx64w?usp=sharing) |
|Deraining (Real-world raindrop)|RainDrop train|RainDrop TestA| [Download](https://drive.google.com/drive/folders/1aJcRGjurK2PbgdFbTL6vSI3Xu3p2Nry-?usp=sharing) |


## Contact  
If you have any question, feel free to contact qaz5517359@gmail.com.  
