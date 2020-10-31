import numpy as np
from scipy.sparse.linalg import norm
import sklearn.preprocessing as pp
import pandas as pd

def cos_sim(a, b):
  A = norm(a)
  B = norm(b)
  if A == 0 or B == 0:
    return 0
  return np.dot(a, b.T)/(A * B)

# calculates cosine similarities matrix (symmterical matrix)
def cos_sims(mat):
  '''
  mat: unnormalized csr_matrix
  '''
  # 単位ベクトルとなるように正規化する
  mat_normalized = pp.normalize(mat, axis=1)
  return mat_normalized * mat_normalized.T

def jaccard_sims(mat):
  pass

# 指定したindexのアイテムの類似度を計算する
def get_similar_item(sim_mat, index, n=5):
  '''
  sim_mat: 類似度行列
  indices: 類似アイテム推薦対象のindexのリスト
  n: 類似度上位n件を取得する
  return 各アイテムの類似度上位n件のアイテムindex
  '''
  sim_items = np.argsort(-sim_mat[index].todense())[:,:n]
  return np.asarray(sim_items)[0]  

# extract similar items
def get_similar_items(sim_mat, indices=[], n=5):
  '''
  sim_mat: 類似度行列
  indices: 類似アイテム推薦対象のindexのリスト
  n: 類似度上位n件を取得する
  return 各アイテムの類似度上位n件のアイテムindex
  '''
  if indices:
    sim_items = np.argsort(-sim_mat[indices].todense())[:,:n]
  else:
    sim_items = np.argsort(-sim_mat.todense())[:,:n]

  return sim_items
  # for sim, m in zip(sim_mat, sim_items):
  #   print(sim.todense().take(m))

# 指定したタグの類似アイテム上位n件の情報を取得する
def get_similar_item_by_name(sim_mat, name, mapper, n=5):
  '''
  sim_mat: 類似度行列
  name: 推薦対象のアイテム
  mapper: idとアイテム名のBidiMapオブジェクト
  n: 類似度上位何件を取得するか
  '''
  index = mapper.vk[name]
  return get_similar_item_info(sim_mat, index, mapper, n=5)

def calc_two_item_similarity(sim_mat, item1, item2, mapper):
  return [item1, item2, sim_mat[mapper.vk[item1], mapper.vk[item2]]]

# 類似アイテムの情報をdataframe形式で取得します
def get_similar_item_info(sim_mat, index, mapper, n=5):
  target = sim_mat[index]
  sim_items = get_similar_item(sim_mat, index, n=n)
  items = [[mapper.kv[index], mapper.kv[sim_idx], target.todense().tolist()[0][sim_idx] ] for sim_idx in sim_items]
  df = pd.DataFrame(items, columns=['target', 'item', 'similarity'])
  return df