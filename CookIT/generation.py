import pandas as pd
from fridge_util import Fridge
class Generator():
    def __init__(self):
        self.correlation_matrix=pd.read_csv("correlations.csv", delimiter=',').to_numpy()
        self.fridge=Fridge()
    def topnrecipes(self, ingredients:list, n:int):
        ingredients_indexes = self.fridge.ings2indexes(ingredients)
        recipes_scores=[]
        for kit in range(1, 2**len(ingredients)):
            kit_mask=str(bin(kit))[2:]
            kit_mask="0"*(len(ingredients)-len(kit_mask))+kit_mask
            totake=[]
            for i in range(len(ingredients)):
                if kit_mask[i]=="1":
                    totake.append(ingredients_indexes[i])
            score=self.count_correlation(totake)
            recipes_scores.append((score, totake))
        recipes_scores.sort(reverse=True)
        topn=[self.fridge.indexes2ings(recipes_scores[i][1]) for i in range(min(n, len(recipes_scores)))]
        return topn

    def count_correlation(self, indexes):
        if len(indexes)==1:
            return 100
        correlations=[]
        for inda in range(len(indexes)):
            for indb in range(inda+1, len(indexes)):
                if self.correlation_matrix[indexes[inda]][indexes[indb]+1]<100:
                    return 0
                correlations.append(self.correlation_matrix[indexes[inda]][indexes[indb]+1])
        return sum(correlations)/len(correlations)

