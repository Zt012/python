#字符串查找
word = 't'
str_01 = 'python'
zfc = str_01.find(word)
print(zfc)

#字符串替换
str_02 ='All things Are difficilt before they Are easy.'
tihuan = str_02.replace('Are','are')   #不指定替换次数（全部替换）
print(tihuan)

#字符串的分割
str_02 ='All things Are difficilt before they Are easy.'
print(str_02.split())       #以空格作为分隔符
print(str_02.split('a'))    #以字母a作为分隔符
print(str_02.split('e',2))  #以字母e作为分隔符，并分割2次

#字符串的拼接
symbol = '*'
world = 'python'
print(symbol.join(world))
#加号拼接法
a = 'py'
b = 'thon'
print(a+b)

#计算字符串中小写字母的数量
shuru = str(input('请输入一行字符：'))
sum_zimu = 0    #统计英文字母个数
for i in range(len(shuru)):     #利用字符在ASCLL码中的位置逐个统计
    if 'a' <=shuru[i] <= 'z':
        sum_zimu +=1
print('小写字母个数为：%d' % sum_zimu)
