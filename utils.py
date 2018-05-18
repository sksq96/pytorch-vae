import imageio
from pathlib import Path


def makegif(folder='reconstructed', name='recon_image', ext='jpg'):
    images = []
    for file in sorted([file for file in Path(folder).glob(f'*.{ext}')]):
        images.append(imageio.imread(str(file)))
    imageio.mimsave(f'{name}.gif', images)
    print("Done!")
