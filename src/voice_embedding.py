import pickle
import numpy as np

def load_embedding(embedding_path):
    """
    Загружает векторное представление голоса из файла.
    
    :param embedding_path: Путь к файлу с embedding.
    :return: Векторное представление голоса.
    """
    with open(embedding_path, 'rb') as f:
        embedding = pickle.load(f)
    return embedding

def save_embedding(embedding, output_path):
    """
    Сохраняет векторное представление голоса в файл.
    
    :param embedding: Векторное представление голоса.
    :param output_path: Путь к выходному файлу.
    """
    with open(output_path, 'wb') as f:
        pickle.dump(embedding, f)

def compute_similarity(embedding1, embedding2):
    """
    Вычисляет схожесть между двумя векторными представлениями голоса.
    
    :param embedding1: Первое векторное представление голоса.
    :param embedding2: Второе векторное представление голоса.
    :return: Значение схожести.
    """
    embedding1 = np.array(embedding1)
    embedding2 = np.array(embedding2)
    similarity = np.dot(embedding1, embedding2) / (np.linalg.norm(embedding1) * np.linalg.norm(embedding2))
    return similarity

