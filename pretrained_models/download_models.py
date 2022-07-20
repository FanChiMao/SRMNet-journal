import wget
from tqdm import tqdm

def main():
    print('It will cost about 4-5 minutes to download...')
    with tqdm(total=4) as bar:
        wget.download('https://github.com/FanChiMao/SRMNet-journal/releases/download/v0.0/model_denoising_gaussian.pth')
        bar.update(1)
        wget.download('https://github.com/FanChiMao/SRMNet-journal/releases/download/v0.0/model_denoising_realworld.pth')
        bar.update(1)
        wget.download('https://github.com/FanChiMao/SRMNet-journal/releases/download/v0.0/model_deraining_raindrop.pth')
        bar.update(1)
        wget.download('https://github.com/FanChiMao/SRMNet-journal/releases/download/v0.0/Denoise_realworld.pth')
        bar.update(1)

if __name__ == '__main__':
    print('Start downloading pretrained models from https://github.com/FanChiMao/SRMNet-journal/releases/tag/v0.0')
    main()
    print('Done !!')