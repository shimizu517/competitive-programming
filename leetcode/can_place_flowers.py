from typing import List
import math

class Solution:
  count_zero = 0
  is_first_or_last = False
  can_plant_num = 0
  def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    for idx, item in enumerate(flowerbed):
      if idx == 0:
        self.is_first_or_last = True
        if len(flowerbed)-1 == idx:
          return True if item == 0 or n ==0 else False
      if item == 0:
        self.count_zero += 1
        if idx == len(flowerbed)-1:
          self.is_first_or_last = True
          self.add_can_plant_num()
      elif item == 1:
        self.add_can_plant_num()
        self.count_zero = 0
        self.is_first_or_last = False
      if self.can_plant_num >= n:
        return True
    return self.can_plant_num >= n
  def add_can_plant_num(self):
    if self.is_first_or_last:
      self.can_plant_num += math.floor(self.count_zero/2)
    else:
      self.can_plant_num += math.floor((self.count_zero-1) / 2)

sol = Solution()
print(sol.canPlaceFlowers([0,1,0],1))