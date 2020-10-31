import numpy as np
from collections import defaultdict
from scipy import sparse



def make_sparse_array(key_item_dic, n_rows, n_cols, save_path):
  '''
  key_item_dic: key（行要素）に関係するitem（列要素）リストのペアの辞書
  ※全てID（配列のインデックス）に対応するよう変換しておくこと
  '''

  # 疎行列作成
  item_sparse_matrix = sparse.lil_matrix( (n_rows, n_cols) )

  print('make sparse array')
  for index, items in list(key_item_dic.items()):
      item_sparse_matrix[index, [item_col for item_col in items] ] = 1
  print('complete!')
  print('sparse array shape:', item_sparse_matrix.shape)
  print('save mat:', save_path)
  #疎行列の保存
  np.save(save_path, item_sparse_matrix)
  print('saved')

def make_sparse_array_by_item_dic(key_item_weight_dic, n_rows, n_cols, save_path):
  '''
  key_item_weight_dic: key（行要素）に関係するitem（各列要素とその重みのペアの辞書）のペアの辞書
  {key: {val1: w1, val2:w2 .....}, key: {val1: w1 ...}}
  ※全てID（配列のインデックス）に対応するよう変換しておくこと
  '''

  # 疎行列作成
  item_sparse_matrix = sparse.lil_matrix( (n_rows, n_cols) )

  print('make sparse array')
  for index, item_weight_dic in key_item_dic.items():
    for item_col, weight in item_weight_dic.items():
      item_sparse_matrix[index,  item_col] = weight
  print('complete!')
  print('sparse array shape:', item_sparse_matrix.shape)
  print('save mat:', save_path)
  #疎行列の保存
  np.save(save_path, item_sparse_matrix)
  print('saved')
