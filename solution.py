import pandas as pd
import numpy as np
from scipy.stats import cramervonmises_2samp

chat_id = 1067114867 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    result = cramervonmises_2samp(x, y)
    p_value = result.pvalue
    alpha = 0.03
    return p_value < alpha

