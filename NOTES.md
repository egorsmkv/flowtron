My GPU: NVIDIA RTX A4000

torch is installed:

    pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html

Using dataset:

    URL: https://github.com/egorsmkv/ukrainian-tts-datasets/tree/main/lada
    Archive: dataset_lada_trimmed_22khz.zip

Install Ukrainian G2P:

    pip install -U git+https://github.com/egorsmkv/ukro_g2p
