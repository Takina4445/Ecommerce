import pandas as pd
import random
df=pd.read_excel("TQC-電商考題.xlsx",sheet_name="工作表2",usecols="C:I,K")
random.seed()
while True:
    dfRandomChoiceColum=random.randint(1,df.shape[0])#0是欄位名稱
    dfGetQuestionNumber=df.iat[dfRandomChoiceColum,0]
    print(dfRandomChoiceColum+2)
    dfGetQuestionAnswer=df.iat[dfRandomChoiceColum,1]#答案
    dfGetQuestionTopic=df.iat[dfRandomChoiceColum,2]
    dfGetQuestionOption1=df.iat[dfRandomChoiceColum,3]
    dfGetQuestionOption2=df.iat[dfRandomChoiceColum,4]
    dfGetQuestionOption3=df.iat[dfRandomChoiceColum,5]
    dfGetQuestionOption4=df.iat[dfRandomChoiceColum,6]
    dfGetQuestionType=df.iat[dfRandomChoiceColum,7]#1:單選;2:複選
    if dfGetQuestionType==1:
        print(f"{dfRandomChoiceColum+2}.{dfGetQuestionTopic}(單選)")
    else:
        print(f"{dfRandomChoiceColum+2}.{dfGetQuestionTopic}(複選)")
    print(f"1.{dfGetQuestionOption1}")
    print(f"2.{dfGetQuestionOption2}")
    print(f"3.{dfGetQuestionOption3}")
    print(f"4.{dfGetQuestionOption4}")
    userInputAnswer=input("請作答:")
    if userInputAnswer==str(dfGetQuestionAnswer):
        print("答案正確!!")
    else:
        print(f"錯誤答案，正確答案為:{dfGetQuestionAnswer}")
    print("*"*20)