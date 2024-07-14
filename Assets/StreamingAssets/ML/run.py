import os
import pickle
import pandas as pd
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class RunModel():
    def __init__(self, model, input):
        self.model = model
        self.input = input
        self.input_df = None
        self.colums = ['품종', '색', '성별', '중성화유무', '나이', '지역', '크기']
        
    def make_dataframe(self):
        age = int(self.input[4])
        area = int(self.input[6])

        if age <=1 :
            self.input[4] = '유년'
        elif  age > 1 and age <= 7 :
            self.input[4] = '성년'
        elif age >= 7 :
            self.input[4] = '노년'

        if area <= 6 :
            self.input[6] = '소형'
        elif area > 6 and area <= 14 :
            self.input[6] = '중형'
        elif area > 14 :
            self.input[6] = '대형'
             
        self.input_df = pd.DataFrame(self.input, index = self.colums).T

    def encoding(self, feature, label):
        self.input_df[feature] = self.input_df[feature].map(label)

    def encoding_groups(self):
        kinds = {
            '기타품종견' : 0, '말티즈' : 1, '믹스견' : 2, '비숑 프리제' : 3, '시바' : 4, 
            '시츄' : 5, '진도견' : 6,'치와와' : 7, '포메라니안' : 8, '푸들' : 9
            }
        colors = {'갈' : 0, '기타' : 1, '백' : 2, '황' : 3, '회' : 4, '흑' : 5}
        sex = {'수컷' : 0, '암컷' : 1}
        goja = {'미상' : 0, '아니오' : 1, '예' : 2}
        age = {'노년' : 0, '성년' : 1, '유년' : 2}
        area = {'관동' : 0, '수도권' : 1, '영남' : 2, '제주' : 3, '호남' : 4, '호서' : 5}
        size = {'대형' : 0, '소형' : 1, '중형' : 2}
        
        groups = [kinds, colors, sex, goja, age, area, size]

        return groups
    
    def make_encoding(self):
        groups = self.encoding_groups()
        
        for idx in range(7):
            self.encoding(self.colums[idx], groups[idx])

    def classification(self):
        self.make_dataframe()
        self.make_encoding()

        result = self.model.predict_proba(self.input_df)

        if result[0][0] > result[0][1] :
            print('{:.2%}의 확률로 미입양'.format(result[0][0]))
        else:
            print('{:.2%}의 확률로 입양'.format(result[0][1])) 


input_line = sys.stdin.read().strip()
input_list = input_line.split()

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = script_dir + '\\model\\dog_adopt_classifier.model'
dog_adopt_model = pickle.load(open(file_path, 'rb'))
run_model = RunModel(dog_adopt_model, input_list)
run_model.classification()