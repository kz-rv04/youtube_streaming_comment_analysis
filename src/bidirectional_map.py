class BidiMap():

  def __init__(self, dic:dict):  
    self.kv = {}
    self.vk = {}
    if dic:
      self.kv = dic
      self.vk = {v: k for k, v in dic.items()}

  def __str__(self):
    return str(self.kv)

  def __len__(self):
    return len(self.kv)

  def ktov(self, args):
    '''
    args: list or tuple
    '''
    if len(args) < 1:
      return []
    return [self.kv.get(k) for k in args]
  
  def vtok(self, args):
    '''
    args: list or tuple
    '''
    if len(args) < 1:
      return []
    return [self.vk.get(k) for k in args]
    