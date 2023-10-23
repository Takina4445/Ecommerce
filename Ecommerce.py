import pandas as pd
import random
import json
#初始化讀取變數
df=pd.read_excel("TQC-電商考題.xlsx",sheet_name="工作表2",usecols="C:I,K")#test excel file
AnswerRecord_json_name="AnswerRecord.json"
#初始化參數
random.seed()
userTotalCorrectAnswer=0
userTotalAnswer=0
#主程式循環
while True:
    #初始化區域
    with open(AnswerRecord_json_name,"r",encoding='utf8') as AnsRd_jsfile:
        AnsRd_json=json.load(AnsRd_jsfile)
    #主程式區域
    userTotalAnswer+=1#使用者答題總數+1
    dfRandomChoiceColum=random.randint(1,df.shape[0])#0是欄位名稱
    # dfRandomChoiceColum=30
    dfGetQuestionNumber=df.iat[dfRandomChoiceColum,0]
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
        print("答題正確!!!")
        userTotalCorrectAnswer+=1#使用者正確答題數量+1
        #正確的題號出現json錯誤清單中，則將在答題正確次數+1
        if f"{dfGetQuestionNumber}" in AnsRd_json["WrongQuestion"]:
            AnsRd_json["WrongQuestion"][f"{dfGetQuestionNumber}"]["ReAnswerCorrectTimes"]+=1
    else:
        print(f"錯誤答案，正確答案為:{dfGetQuestionAnswer}")
        #錯誤的題號在json資料庫中便將錯誤次數+1;否則將該題號加入錯誤清單中
        if f"{dfGetQuestionNumber}" in AnsRd_json["WrongQuestion"]:
            AnsRd_json["WrongQuestion"][f"{dfGetQuestionNumber}"]["WrongTimes"]+=1
        else:
            AnsRd_json["WrongQuestion"][f"{dfGetQuestionNumber}"]={"QuestionNumber":f"{dfGetQuestionNumber}","WrongTimes":1,"ReAnswerCorrectTimes":0,"UserNeedTest":True}
    #答題正確率計算與顯示
    print("*"*20+f"({userTotalCorrectAnswer}/{userTotalAnswer}，正確率:{round(userTotalCorrectAnswer/userTotalAnswer*100,2)}%)\n")
    
    #json檔案儲存
    with open(AnswerRecord_json_name,"w",encoding='utf8')as update_AnsRd_json:
        json.dump(AnsRd_json,update_AnsRd_json,ensure_ascii=False, indent=4)