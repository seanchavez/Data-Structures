class Heap:
    def __init__(self):
        self.storage = []
  
    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)
  
    def delete(self):
      pass
  
    def get_max(self):
      pass
  
    def get_size(self):
      pass
  
    def _bubble_up(self, index):
        i = index
        while i // 2 > 0:
            if self.storage[i] < self.storage[i // 2]:
                tmp = self.storage[i // 2]
                self.storage[i // 2] = self.storage[i]
                self.storage[i] = tmp
            i = i // 2
  
    def _sift_down(self, index):
      pass
