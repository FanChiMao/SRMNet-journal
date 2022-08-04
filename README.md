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



## Visual results  

| Task | Training Set | Testing Set | SRMNet's Visual Results|
|:---:|:---:|:---:|:---:|
|Denoising (Synthesized gaussian noise)| |CBSD68 | [Dowmload](https://console.cloud.google.com/storage/browser/gresearch/maxim/results/Denoising/SIDD/) |
|Denoising (Synthesized gaussian noise)| |Kodak24| [Dowmload](https://console.cloud.google.com/storage/browser/gresearch/maxim/results/Denoising/DND/) |
|Denoising (Real-world noise)| | SIDD  | [Dowmload](https://console.cloud.google.com/storage/browser/gresearch/maxim/results/Denoising/DND/) |
|Denoising (Real-world noise)| | DND   | [Dowmload](https://console.cloud.google.com/storage/browser/gresearch/maxim/results/Denoising/DND/) |
|Deraining (Synthesized rainstreak)| Rain13k | Rain100L | [Dowmload](https://console.cloud.google.com/storage/browser/gresearch/maxim/results/Denoising/SIDD/) |
|Deraining (Synthesized rainstreak)| Rain13k | Rain100H | [Dowmload](https://console.cloud.google.com/storage/browser/gresearch/maxim/results/Denoising/SIDD/) |
|Deraining (Synthesized rainstreak)| Rain13k | Test100 | [Dowmload](https://console.cloud.google.com/storage/browser/gresearch/maxim/results/Denoising/SIDD/) |
|Deraining (Synthesized rainstreak)| Rain13k | Test1200 | [Dowmload](https://console.cloud.google.com/storage/browser/gresearch/maxim/results/Denoising/SIDD/) |
|Deraining (Real-world raindrop)|RainDrop train|RainDrop TestA| [Dowmload](https://console.cloud.google.com/storage/browser/gresearch/maxim/results/Denoising/SIDD/) |

