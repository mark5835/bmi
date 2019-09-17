# BMI 計算程式
hight = input('請輸入身高cm： ')
hight = float(hight)
weight = input('請輸入體重kg: ')
weight = float(weight)
bmi = weight / (( hight / 100) * (hight / 100))
if bmi < 18.5:
    print('你的BMI值是： ', bmi , '屬於體重過輕')
elif bmi >= 18.5 and bmi < 24:
    print('你的BMI值是： ', bmi , '屬於正常範圍')
elif bmi >=24 and bmi < 27:
    print('你的BMI值是： ', bmi , '屬於體重過重')
elif bmi >= 27 and bmi < 30:
    print('你的BMI值是： ', bmi , '屬於輕度肥胖')
elif bmi >= 30 and bmi < 35:
    print('你的BMI值是： ', bmi , '屬於中度過輕')
else:
	print('你的BMI值是： ', bmi , '屬於重度肥胖')
