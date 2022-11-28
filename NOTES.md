My GPU: NVIDIA RTX A4000
Python: 3.8.13

torch is installed:

    pip install torch==1.7.1+cu110 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html

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

====

TRAIN FROM A CHECKPOINT

python train.py -c config.json -p train_config.ignore_layers=["speaker_embedding.weight"] train_config.checkpoint_path="models/flowtron_ljs.pt"

====

INFERENCE

0) Download waveglow_256channels_ljs_v3.pt

cd models
curl -LO 'https://api.ngc.nvidia.com/v2/models/nvidia/waveglow_ljs_256channels/versions/3/files/waveglow_256channels_ljs_v3.pt'

1) Download https://drive.google.com/file/d/1rpK8CzAAirq9sWZhe9nlfvxMF1dRgFbF/view

2) Copy the checkpoint to models folder

cp outdir/model_1000 models/flowtron_lada.pt

3) Run it

python inference.py --eng 0 -c config.json -f models/flowtron_lada.pt -w models/waveglow_256channels_ljs_v3.pt -t "Добрий день!" -i 0

---

Original:

python inference.py -c config.json -f models/flowtron_ljs.pt -w models/waveglow_256channels_ljs_v3.pt -t "You initialise a random tenor at the start of" -i 0
