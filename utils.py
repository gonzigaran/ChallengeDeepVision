import pandas as pd
import numpy as np
np.random.seed(123)
import sklearn

def create_df(boxes):
    df = pd.DataFrame(columns=['x', 'y', 'w', 'h', 'score'])
    j = 0
    for box in boxes:
        (x, y, w, h, score) = box
        df.loc[j] = (x, y, w, h, score)
        j += 1
        n = np.random.randint(10,30)
        for i in range(n):
            df.loc[j] = (x + np.random.randint(-15,15), 
                         y + np.random.randint(-15,15), 
                         w + np.random.randint(-15,15), 
                         h + np.random.randint(-15,15),
                         np.random.uniform(0.4,score,1)[0] )
            j += 1 
    df = sklearn.utils.shuffle(df).reset_index(drop=True)
    return df

def nms(boxes, scores, Nt=0.5):
    D = pd.DataFrame(columns=['x', 'y', 'w', 'h', 'score'])
    while not boxes.empty:
        idx = scores.idxmax()
        M = boxes.loc[idx]
        D.loc[idx] = M
        D.loc[idx, 'score'] = scores.loc[idx]
        iou_with_M = lambda x: iou_index(list(x), list(M))
        iou_with_M_df = boxes.apply(iou_with_M, axis=1)
        boxes = boxes[iou_with_M_df < Nt]
        scores = scores[iou_with_M_df < Nt]
    return D

def iou_index(box1, box2):
    return area_overlap(box1, box2) / float(area_union(box1, box2))

def area_overlap(box1, box2):
    xA = max(box1[0], box2[0])
    yA = max(box1[1], box2[1])
    xB = min(box1[0] + box1[2], box2[0] + box2[2])
    yB = min(box1[1] + box1[3], box2[1] + box2[3])
    
    if xA <= xB and yA <= yB:
        return (xB - xA) * (yB - yA)
    else:
        return 0

def area_union(box1, box2):
    box1Area = box1[2] * box1[3]
    box2Area = box2[2] * box2[3]
    
    return box1Area + box2Area - area_overlap(box1, box2)
