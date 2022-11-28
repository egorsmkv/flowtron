My GPU: NVIDIA RTX A4000
Python: 3.8.13

torch is installed:

    pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html

Using dataset:

    URL: https://github.com/egorsmkv/ukrainian-tts-datasets/tree/main/lada
    Archive: dataset_lada_trimmed_22khz.zip

Install Ukrainian G2P:

    pip install -U git+https://github.com/egorsmkv/ukro_g2p

Fix error "ModuleNotFoundError: No module named 'numba.decorators'" by :

    pip install numba==0.48

Fix error "TypeError: guvectorize() missing 1 required positional argument: 'signature'" by :

    pip install resampy==0.3.1

Export MELs:

    python data.py -c config.json -f filelists/lada_ukrainian_train_filelist.txt -o outdir_train_mels


Run the tesorboard:

tensorboard --logdir outdir/logs

====


TRAIN

1) python train.py -c config.json -p train_config.output_directory=outdir data_config.use_attn_prior=1

