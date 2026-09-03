---
layout: post
title: "Economizando espaço com fotos"
author: "Davi"
categories: blog
tags: [blog,ia,python,automacao]
image: compare.png
---

# Como Criar um Comparador de Imagens usando IA em Python

## Introdução

Você já se pegou com milhares de fotos espalhadas em diferentes pastas e subpastas do seu computador, muitas delas duplicadas ou muito similares? Este artigo apresenta uma solução completa em Python para organizar suas imagens e identificar duplicadas usando inteligência artificial.

Nosso objetivo é criar um sistema que:
- Vasculhe recursivamente todos os arquivos e subpastas
- Encontre e organize todas as imagens em uma única pasta
- Renomeie arquivos duplicados para evitar sobreposição
- Use IA para comparar imagens e detectar similaridade (98%-100%)
- Exclua automaticamente imagens de menor qualidade

## Requisitos e Bibliotecas

Antes de começar, vamos instalar as bibliotecas necessárias[1][2]:

```bash
pip install pillow imagehash opencv-python sentence-transformers torch torchvision faiss-cpu numpy pandas
```

**Principais bibliotecas utilizadas:**
- **PIL (Pillow)**: Manipulação de imagens
- **ImageHash**: Hashing perceptual para detecção de duplicatas
- **OpenCV**: Processamento de imagens
- **Sentence-Transformers**: Modelo CLIP para embeddings de imagens
- **FAISS**: Busca eficiente de similaridade
- **OS/Shutil**: Manipulação de arquivos e diretórios

## Etapa 1: Encontrar e Organizar Todas as Imagens

Primeiro, vamos criar uma função para vasculhar recursivamente todos os diretórios e encontrar imagens[3][4]:

```python
import os
import shutil
from pathlib import Path
from PIL import Image
import hashlib
from collections import defaultdict

def encontrar_todas_imagens(diretorio_origem):
    """
    Encontra todas as imagens em um diretório e suas subpastas
    """
    extensoes_imagem = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}
    imagens_encontradas = []
    
    for root, dirs, files in os.walk(diretorio_origem):
        for arquivo in files:
            if Path(arquivo).suffix.lower() in extensoes_imagem:
                caminho_completo = os.path.join(root, arquivo)
                imagens_encontradas.append(caminho_completo)
                print(f"Encontrada: {caminho_completo}")
    
    return imagens_encontradas
```

## Etapa 2: Mover Imagens para Pasta Única com Renomeação

Agora vamos mover todas as imagens para uma pasta única, evitando sobrescrever arquivos[5][6]:

```python
def mover_imagens_com_sufixo(lista_imagens, pasta_destino):
    """
    Move todas as imagens para uma pasta única, renomeando duplicatas
    """
    # Criar pasta de destino se não existir
    Path(pasta_destino).mkdir(parents=True, exist_ok=True)
    
    contador_nomes = defaultdict(int)
    imagens_organizadas = []
    
    for caminho_origem in lista_imagens:
        nome_arquivo = Path(caminho_origem).name
        nome_base = Path(caminho_origem).stem
        extensao = Path(caminho_origem).suffix
        
        # Verificar se já existe arquivo com mesmo nome
        caminho_destino = os.path.join(pasta_destino, nome_arquivo)
        
        # Se existir, adicionar sufixo numérico
        if os.path.exists(caminho_destino):
            contador_nomes[nome_base] += 1
            novo_nome = f"{nome_base}_{contador_nomes[nome_base]}{extensao}"
            caminho_destino = os.path.join(pasta_destino, novo_nome)
        
        try:
            shutil.copy2(caminho_origem, caminho_destino)
            imagens_organizadas.append(caminho_destino)
            print(f"Movido: {caminho_origem} -> {caminho_destino}")
        except Exception as e:
            print(f"Erro ao mover {caminho_origem}: {e}")
    
    return imagens_organizadas
```

## Etapa 3: Detecção de Similaridade usando IA

### Método 1: Hashing Perceptual (Rápido)

Para uma primeira triagem rápida, usamos hashing perceptual[7][8]:

```python
import imagehash

def calcular_hash_perceptual(caminho_imagem, tamanho_hash=16):
    """
    Calcula hash perceptual da imagem usando dHash
    """
    try:
        with Image.open(caminho_imagem) as img:
            # Usar dHash (difference hash) - mais robusto
            dhash = imagehash.dhash(img, hash_size=tamanho_hash)
            return str(dhash)
    except Exception as e:
        print(f"Erro ao processar {caminho_imagem}: {e}")
        return None

def encontrar_duplicatas_hash(lista_imagens, threshold=5):
    """
    Encontra duplicatas usando hashing perceptual
    """
    hash_para_imagens = defaultdict(list)
    
    # Calcular hashes para todas as imagens
    for imagem in lista_imagens:
        hash_img = calcular_hash_perceptual(imagem)
        if hash_img:
            hash_para_imagens[hash_img].append(imagem)
    
    # Encontrar grupos de duplicatas
    grupos_duplicatas = []
    for hash_val, imagens in hash_para_imagens.items():
        if len(imagens) > 1:
            grupos_duplicatas.append(imagens)
            
    return grupos_duplicatas
```

### Método 2: IA com CLIP (Mais Preciso)

Para comparação mais sofisticada, usamos o modelo CLIP da OpenAI[9][10]:

```python
import torch
from sentence_transformers import SentenceTransformer, util
from PIL import Image
import numpy as np

class ComparadorImagensIA:
    def __init__(self):
        """
        Inicializa o modelo CLIP para comparação de imagens
        """
        print("Carregando modelo CLIP...")
        self.modelo = SentenceTransformer('clip-ViT-B-32')
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
    def extrair_features(self, lista_imagens):
        """
        Extrai features das imagens usando CLIP
        """
        features = []
        imagens_validas = []
        
        for caminho_imagem in lista_imagens:
            try:
                with Image.open(caminho_imagem).convert('RGB') as img:
                    # Redimensionar se muito grande (otimização)
                    if img.size[0] > 512 or img.size[1] > 512:
                        img.thumbnail((512, 512), Image.Resampling.LANCZOS)
                    
                    feature = self.modelo.encode(img)
                    features.append(feature)
                    imagens_validas.append(caminho_imagem)
                    
            except Exception as e:
                print(f"Erro ao processar {caminho_imagem}: {e}")
                
        return np.array(features), imagens_validas
    
    def encontrar_similares(self, features, imagens, threshold=0.98):
        """
        Encontra imagens similares usando cosine similarity
        """
        print(f"Comparando {len(imagens)} imagens com threshold {threshold}")
        
        # Calcular matriz de similaridade
        similarity_matrix = util.cos_sim(features, features)
        
        grupos_similares = []
        processadas = set()
        
        for i in range(len(imagens)):
            if i in processadas:
                continue
                
            grupo_atual = [i]
            processadas.add(i)
            
            # Encontrar todas as imagens similares a esta
            for j in range(i + 1, len(imagens)):
                if j in processadas:
                    continue
                    
                similaridade = similarity_matrix[i][j].item()
                if similaridade >= threshold:
                    grupo_atual.append(j)
                    processadas.add(j)
            
            # Se encontrou similares, adicionar ao grupo
            if len(grupo_atual) > 1:
                grupo_imagens = [imagens[idx] for idx in grupo_atual]
                grupos_similares.append(grupo_imagens)
                
        return grupos_similares
```

## Etapa 4: Determinação de Qualidade da Imagem

Vamos criar uma função para determinar qual imagem tem melhor qualidade[11][12]:

```python
def avaliar_qualidade_imagem(caminho_imagem):
    """
    Avalia a qualidade de uma imagem baseada em múltiplos critérios
    """
    try:
        with Image.open(caminho_imagem) as img:
            # Critérios de qualidade
            largura, altura = img.size
            total_pixels = largura * altura
            
            # Tamanho do arquivo
            tamanho_arquivo = os.path.getsize(caminho_imagem)
            
            # Formato da imagem (PNG > TIFF > JPG em qualidade)
            formato = img.format.lower() if img.format else 'unknown'
            peso_formato = {'png': 3, 'tiff': 2, 'jpg': 1, 'jpeg': 1}
            score_formato = peso_formato.get(formato, 0)
            
            # Score combinado (resolução + tamanho + formato)
            score_qualidade = (total_pixels * 0.6) + (tamanho_arquivo * 0.3) + (score_formato * 100000 * 0.1)
            
            return {
                'caminho': caminho_imagem,
                'resolucao': (largura, altura),
                'pixels': total_pixels,
                'tamanho_mb': tamanho_arquivo / (1024 * 1024),
                'formato': formato,
                'score': score_qualidade
            }
            
    except Exception as e:
        print(f"Erro ao avaliar {caminho_imagem}: {e}")
        return None

def selecionar_melhor_qualidade(grupo_imagens):
    """
    Seleciona a imagem de melhor qualidade de um grupo
    """
    avaliacoes = []
    
    for imagem in grupo_imagens:
        avaliacao = avaliar_qualidade_imagem(imagem)
        if avaliacao:
            avaliacoes.append(avaliacao)
    
    if not avaliacoes:
        return None
        
    # Ordenar por score de qualidade (maior = melhor)
    avaliacoes.sort(key=lambda x: x['score'], reverse=True)
    return avaliacoes[0]['caminho']
```

## Etapa 5: Sistema Principal

Agora vamos integrar tudo em um sistema principal:

```python
def main():
    # Configurações
    DIRETORIO_ORIGEM = "/caminho/para/suas/fotos"
    PASTA_ORGANIZADA = "/caminho/para/pasta/organizada"
    THRESHOLD_SIMILARIDADE = 0.98  # 98% de similaridade
    
    print("=== INICIANDO ORGANIZADOR DE IMAGENS COM IA ===")
    
    # Etapa 1: Encontrar todas as imagens
    print("\n1. Buscando todas as imagens...")
    todas_imagens = encontrar_todas_imagens(DIRETORIO_ORIGEM)
    print(f"Encontradas {len(todas_imagens)} imagens")
    
    # Etapa 2: Organizar em pasta única
    print("\n2. Organizando imagens em pasta única...")
    imagens_organizadas = mover_imagens_com_sufixo(todas_imagens, PASTA_ORGANIZADA)
    print(f"Organizadas {len(imagens_organizadas)} imagens")
    
    # Etapa 3: Primeira triagem com hash (rápido)
    print("\n3. Primeira triagem com hashing perceptual...")
    grupos_hash = encontrar_duplicatas_hash(imagens_organizadas)
    print(f"Encontrados {len(grupos_hash)} grupos de possíveis duplicatas")
    
    # Etapa 4: Análise detalhada com IA
    print("\n4. Análise detalhada com IA...")
    comparador = ComparadorImagensIA()
    
    # Extrair features de todas as imagens
    features, imagens_validas = comparador.extrair_features(imagens_organizadas)
    
    # Encontrar similares
    grupos_similares = comparador.encontrar_similares(
        features, imagens_validas, THRESHOLD_SIMILARIDADE
    )
    
    print(f"IA encontrou {len(grupos_similares)} grupos de imagens similares")
    
    # Etapa 5: Remover duplicatas mantendo melhor qualidade
    print("\n5. Removendo duplicatas...")
    total_removidas = 0
    
    for i, grupo in enumerate(grupos_similares):
        print(f"\nGrupo {i+1}: {len(grupo)} imagens similares")
        
        # Mostrar similaridades do grupo
        for img in grupo:
            print(f"  - {os.path.basename(img)}")
        
        # Selecionar melhor qualidade
        melhor_imagem = selecionar_melhor_qualidade(grupo)
        
        if melhor_imagem:
            print(f"  Mantendo: {os.path.basename(melhor_imagem)}")
            
            # Remover as outras
            for img in grupo:
                if img != melhor_imagem:
                    try:
                        os.remove(img)
                        print(f"  Removida: {os.path.basename(img)}")
                        total_removidas += 1
                    except Exception as e:
                        print(f"  Erro ao remover {img}: {e}")
    
    print(f"\n=== PROCESSO CONCLUÍDO ===")
    print(f"Total de imagens processadas: {len(imagens_organizadas)}")
    print(f"Imagens duplicadas removidas: {total_removidas}")
    print(f"Imagens finais: {len(imagens_organizadas) - total_removidas}")

if __name__ == "__main__":
    main()
```

## Otimizações Avançadas

### Usando FAISS para Datasets Grandes

Para conjuntos muito grandes de imagens, podemos usar FAISS para busca mais eficiente[13][14]:

```python
import faiss

class ComparadorImagensFAISS:
    def __init__(self):
        self.modelo = SentenceTransformer('clip-ViT-B-32')
        self.index = None
        self.imagens = []
        
    def construir_indice(self, features):
        """
        Constrói índice FAISS para busca eficiente
        """
        dimension = features.shape[1]
        
        # Usar IndexFlatIP para cosine similarity
        self.index = faiss.IndexFlatIP(dimension)
        
        # Normalizar features para cosine similarity
        faiss.normalize_L2(features)
        self.index.add(features.astype(np.float32))
        
    def buscar_similares_faiss(self, features, threshold=0.98, k=10):
        """
        Busca imagens similares usando FAISS
        """
        grupos_similares = []
        processadas = set()
        
        for i in range(len(features)):
            if i in processadas:
                continue
                
            # Buscar k vizinhos mais próximos
            query = features[i:i+1].astype(np.float32)
            faiss.normalize_L2(query)
            
            scores, indices = self.index.search(query, k)
            
            # Filtrar por threshold
            grupo_atual = []
            for score, idx in zip(scores[0], indices[0]):
                if score >= threshold and idx not in processadas:
                    grupo_atual.append(idx)
                    processadas.add(idx)
            
            if len(grupo_atual) > 1:
                grupo_imagens = [self.imagens[idx] for idx in grupo_atual]
                grupos_similares.append(grupo_imagens)
                
        return grupos_similares
```

## Monitoramento e Logs

Adicione um sistema de logs para acompanhar o processo:

```python
import logging
from datetime import datetime

def configurar_logs():
    """
    Configura sistema de logs
    """
    log_filename = f"organizador_imagens_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filename),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger(__name__)
```

## Conclusão

Este sistema completo oferece uma solução robusta para organizar e deduplificar grandes coleções de imagens usando inteligência artificial. As principais vantagens incluem:

- **Busca recursiva**: Encontra imagens em qualquer subdiretório
- **Organização segura**: Nunca sobrescreve arquivos, usa sufixos numéricos
- **IA avançada**: Usa CLIP para detecção precisa de similaridade
- **Preservação de qualidade**: Mantém automaticamente as imagens de melhor qualidade
- **Escalabilidade**: Suporta milhares de imagens com otimizações FAISS

**Considerações importantes:**
- Sempre faça backup antes de executar o script
- Ajuste o threshold de similaridade conforme necessário (0.95-0.99)
- Para datasets muito grandes (>10k imagens), use a versão FAISS
- Monitore o uso de memória RAM durante o processamento

Com esta solução, você pode finalmente ter suas fotos organizadas de forma inteligente, eliminando duplicatas e mantendo apenas as melhores versões de cada imagem.

## Fontes
- [1] idealo/imagededup: Finding duplicate images made easy! - GitHub https://github.com/idealo/imagededup
- [2] elisemercury/Duplicate-Image-Finder: difPy - GitHub https://github.com/elisemercury/Duplicate-Image-Finder
- [3] Want to get desired Image path using os.walk in python https://stackoverflow.com/questions/70295047/want-to-get-desired-image-path-using-os-walk-in-python
- [4] os.walk() in Python - GeeksforGeeks https://www.geeksforgeeks.org/python/os-walk-python/
- [5] File Organizing with Python https://www.python-engineer.com/posts/file-organization/
- [6] Move Files Or Directories in Python - PYnative https://pynative.com/python-move-files/
- [7] mattpodolak/duplicate-img-detection - GitHub https://github.com/mattpodolak/duplicate-img-detection
- [8] Removing Duplicate or Similar Images in Python https://towardsdatascience.com/removing-duplicate-or-similar-images-in-python-93d447c1c3eb/
- [9] python - Find near duplicate and faked images - Stack Overflow https://stackoverflow.com/questions/71514124/find-near-duplicate-and-faked-images
- [10] How to calculate image similarity of given 2 images by using open AI ... https://stackoverflow.com/questions/75709193/how-to-calculate-image-similarity-of-given-2-images-by-using-open-ai-clip-model
- [11] Change image resolution using Pillow in Python - GeeksforGeeks https://www.geeksforgeeks.org/python/change-image-resolution-using-pillow-in-python/
- [12] JPEG Image Quality in PIL - jdhao's digital space https://jdhao.github.io/2019/07/20/pil_jpeg_image_quality/
- [13] Welcome to Faiss Documentation — Faiss documentation https://faiss.ai/index.html
- [14] Understanding FAISS for efficient similarity search of dense vectors https://www.youtube.com/watch?v=0jOlZpFFxCE
- [15] retkowsky/spot_the_difference: Spot the difference between ... - GitHub https://github.com/retkowsky/spot_the_difference
- [16] Image Similarity: Understanding and Implementing Methods https://www.geeksforgeeks.org/computer-vision/image-similarity-understanding-and-implementing-methods/
- [17] A Beginner's Guide to Image Comparison in Python - Cloudinary https://cloudinary.com/guides/image-effects/beginners-guide-to-image-comparison-in-python
- [18] duplicate_images - PyPI https://pypi.org/project/duplicate_images/
- [19] image-similarity-measures - PyPI https://pypi.org/project/image-similarity-measures/
- [20] How to implement Image Similarity Search with Python - Eden AI https://www.edenai.co/post/how-to-implement-image-similarity-search-with-python
- [21] 348 - Image Similarity Search with VGG16 and Cosine Distance https://www.youtube.com/watch?v=dCcRWdmmgA0
- [22] Algorithms for Image Comparison - GeeksforGeeks https://www.geeksforgeeks.org/computer-vision/algorithms-for-image-comparison/
- [23] image-similarity · GitHub Topics https://github.com/topics/image-similarity
- [24] How to compare 2 image simialrity using OPenAI api https://community.openai.com/t/how-to-compare-2-image-simialrity-using-openai-api/700891
- [25] Detect and Delete Duplicate Photos Using Code From GitHub https://www.youtube.com/watch?v=F2uLzhEZwOc
- [26] python - Image Search using Image Similarity Measures https://stackoverflow.com/questions/64520940/image-search-using-image-similarity-measures
- [27] How to compare how similar two images are in Python? https://stackoverflow.com/questions/72851122/how-to-compare-how-similar-two-images-are-in-python
- [28] Create a Python program to find duplicate images - YouTube https://www.youtube.com/watch?v=658U3o7hlbI
- [29] Image Similarity - Kaggle https://www.kaggle.com/code/mdbadrulislam/image-similarity
- [30] Fast algorithm for finding similar images? : r/compsci - Reddit https://www.reddit.com/r/compsci/comments/1gd2usl/fast_algorithm_for_finding_similar_images/
- [31] Finding near-duplicate images with Python and some maths - Reddit https://www.reddit.com/r/computervision/comments/10rrsc4/finding_nearduplicate_images_with_python_and_some/
- [32] Script to move all images from one folder to another : r/learnpython https://www.reddit.com/r/learnpython/comments/8t5se7/script_to_move_all_images_from_one_folder_to/
- [33] Rename multiple files using Python - GeeksforGeeks https://www.geeksforgeeks.org/python/rename-multiple-files-using-python/
- [34] How to Move Files in Python: Single and Multiple File Examples https://www.learndatasci.com/solutions/python-move-file/
- [35] Python for Beginners: How to Write a Simple File Organizer Code https://blog.devgenius.io/python-for-beginners-how-to-write-a-simple-file-organizer-code-fd6a12eb4b3d
- [36] How to rename files with same string and add suffix - Stack Overflow https://stackoverflow.com/questions/70827477/how-to-rename-files-with-same-string-and-add-suffix
- [37] Master Python: Effortlessly Move Images/Files to Multiple Folders! https://www.youtube.com/watch?v=rW5LSPGLf9E
- [38] How to Auto-Organize Your Files - python - DEV Community https://dev.to/devasservice/streamline-your-downloads-with-python-how-to-auto-organize-your-files-47h8
- [39] How to move specific files and renames only the duplicate names only https://www.reddit.com/r/learnpython/comments/kcwbws/how_to_move_specific_files_and_renames_only_the/
- [40] Organize Files With Python (A Simple Automation Script ... - YouTube https://www.youtube.com/watch?v=z6d2FVHR5X4
- [41] Maya Python: Renaming Duplicate Objects - Erwan Leroy https://erwanleroy.com/maya-python-renaming-duplicate-objects/
- [42] How to move images to different directory? - python - Stack Overflow https://stackoverflow.com/questions/43921443/how-to-move-images-to-different-directory
- [43] How to Organize Files by Extension in Python https://thepythoncode.com/article/organize-files-by-extension-with-python
- [44] How to rename files in Python https://www.python-engineer.com/posts/rename-files/
- [45] Moving 2 photos from each subfolder to another folder - Python Forum https://python-forum.io/thread-35398.html
- [46] Automate Renaming and Organizing Files with Python https://www.geeksforgeeks.org/python/automate-renaming-and-organizing-files-with-python/
- [47] python - Rename, Move, Copy & Delete Files and Folders - YouTube https://www.youtube.com/watch?v=NOvFZamGXXo
- [48] How to move Files and Directories in Python - GeeksforGeeks https://www.geeksforgeeks.org/python/how-to-move-files-and-directories-in-python/
- [49] How do you keep your python files organized : r/learnpython - Reddit https://www.reddit.com/r/learnpython/comments/ujp2yo/how_do_you_keep_your_python_files_organized/
- [50] Python - os.walk() - Method - W3Schools https://www.w3schools.com/python/ref_os_walk.asp
- [51] Duplicate image detection with perceptual hashing in Python https://benhoyt.com/writings/duplicate-image-detection/
- [52] Python Pointer: Find Files with os.walk() | Datapoints https://lippincottlibrary.wordpress.com/2020/02/05/python-find-files-with-os-walk/
- [53] Using PIL (Pillow) and Image but keeping a good resolution https://stackoverflow.com/questions/56278307/using-pil-pillow-and-image-but-keeping-a-good-resolution
- [54] Downsizing PNG image without losing image quality, using Pillow https://www.reddit.com/r/learnpython/comments/cju47e/downsizing_png_image_without_losing_image_quality/
- [55] Near duplicate image detection - NeuML https://neuml.hashnode.dev/near-duplicate-image-detection
- [56] os.walk does not find all the files in an sd card : r/learnpython - Reddit https://www.reddit.com/r/learnpython/comments/1cw6360/oswalk_does_not_find_all_the_files_in_an_sd_card/
- [57] Low color quality in JPG image generated with quality=100 option https://github.com/python-pillow/Pillow/issues/3028
- [58] What is my best bet for detecting duplicate images quickly? : r/Python https://www.reddit.com/r/Python/comments/3ndsj8/what_is_my_best_bet_for_detecting_duplicate/
- [59] Simple script to find directories containing pictures - Python Forum https://python-forum.io/thread-2976.html
- [60] A more efficient way of comparing two images in a python https://discuss.python.org/t/a-more-efficient-way-of-comparing-two-images-in-a-python/3725
- [61] Find all files in a directory with a given extension using Python | Sentry https://sentry.io/answers/find-all-files-in-a-directory-with-a-given-extension-using-python/
- [62] VGG image feature extraction and label prediction with docker https://github.com/DominicBreuker/vgg_docker
- [63] Simple image similarity calculator using the CLIP - GitHub https://github.com/cobanov/clip-image-similarity
- [64] Extract Features from Image using Pretrained Model | Python https://www.youtube.com/watch?v=LGk2SfHLhGo
- [65] How to extract features using VGG16 model and use them as input ... https://stackoverflow.com/questions/71324609/how-to-extract-features-using-vgg16-model-and-use-them-as-input-for-another-mode
- [66] Visualising Similarities Between CLIP Text and Image Embeddings https://dev.to/singlestore/quick-tip-visualising-similarities-between-clip-text-and-image-embeddings-132
- [67] Faiss: A library for efficient similarity search - Engineering at Meta https://engineering.fb.com/2017/03/29/data-infrastructure/faiss-a-library-for-efficient-similarity-search/
- [68] VGG16 and VGG19 - Keras https://keras.io/api/applications/vgg/
- [69] Taited/clip-score: Quick scripts to calculate CLIP text-image similarity https://github.com/Taited/clip-score
- [70] Efficient Similarity Search with FAISS and SQLite in Python https://programmer.ie/post/faiss_db/
- [71] Feature Extraction and Fine Tuning using VGG16 - Kaggle https://www.kaggle.com/code/tolgahancepel/feature-extraction-and-fine-tuning-using-vgg16
- [72] Semantic Image Search with OpenAI CLIP and Meta FAISS https://docs.ultralytics.com/guides/similarity-search/
- [73] Faiss | 🦜️   LangChain https://python.langchain.com/docs/integrations/vectorstores/faiss/
- [74] Feature extraction using VGG16 - GitHub Gist https://gist.github.com/gauravgola96/2ef146bc3b9d4f63a0665f679ec703d1?short_path=9e31afa
- [75] How to implement image similarity search in Elasticsearch https://www.elastic.co/search-labs/blog/implement-image-similarity-search-elastic
- [76] Introduction to Facebook AI Similarity Search (Faiss) - Pinecone https://www.pinecone.io/learn/series/faiss/faiss-tutorial/
- [77] VGG Net Feature Extraction and Visualization - Kaggle https://www.kaggle.com/code/meaninglesslives/vgg-net-feature-extraction-and-visualization
- [78] Image Search in Python with OpenAI CLIP - YouTube https://www.youtube.com/watch?v=S7VZErcTN5Y
