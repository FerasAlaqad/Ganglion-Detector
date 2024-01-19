#!/bin/bash
#SBATCH -p palamut-cuda                 # Kuyruk adi: Uzerinde GPU olan kuyruk olmasina dikkat edin.
#SBATCH -A proj3                        # Kullanici adi
#SBATCH -J out                        # Gonderilen isin ismi
#SBATCH -o out.out                    # Ciktinin yazilacagi dosya adi
#SBATCH --gres=gpu:1                    # Her bir sunucuda kac GPU istiyorsunuz? Kumeleri kontrol edin.
#SBATCH -N 1                            # Gorev kac node'da calisacak?
#SBATCH -n 1                            # Ayni gorevden kac adet calistirilacak?
#SBATCH -c 16                        # Her bir gorev kac cekirdek kullanacak? Kumeleri kontrol edin.
#SBATCH --time=23:55:00   



cd /truba/home/proj3/feras/Hirschsprung/github_repo

module load centos7.3/lib/cuda/10.1

source /truba/home/proj3/feras/miniconda3/etc/profile.d/conda.sh
conda activate ai-ffpe


python inference.py