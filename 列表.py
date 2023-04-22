'''
shopping_list = []
# 往购物清单里添加两个商品
shopping_list.append("键盘")
shopping_list.append("键帽")
# 往购物清单里移除一个商品
shopping_list.remove("键帽")
# 往购物清单里移除两个商品
shopping_list.append("音响")
shopping_list.append("电竞椅")
# 更改购物清单的第二个商品
shopping_list[1] = "硬盘"

# print(shopping_list)
# print(len(shopping_list))
# print(shopping_list[0])

# 定义一个价格列表
price = [799, 1024, 200, 800]
# 获取最高的价格
max_price = max(price)
# 获取最低的价格
min_price = min(price)
# 获取从低到高排序好的价格列表
sorted_price = sorted(price)
print(max_price)
print(min_price)
print(sorted_price)
'''

list01 = [21,25,21,23,22,20]
list01.append(31)   #用append()方法追加一个数字31到列表尾部
print(list01)

lsit02 = [29,33,30] #用extend()方法追加一个新的列表到列表的尾部
list01.extend(lsit02)
print(list01)

print(list01[0])    #查找第一个元素，正向索引
print(list01[-1])   #查找最后一个元素，反向索引

#用index()方法查找下标（索引位置）
print(list01.index(31)) #查找31元素的下标（索引位置）
list01.insert(2,'09')   #将元素’09‘，插入到lise01中索引为2的位置
print(list01)

#删除列表元素
list03 = ['p','y','t','h','o','n']
#用del()方法删除指定元素，
del list03[0]   #删除索引为0的元素
print(list03)
list03.remove('y')  #移除匹配到的第一个’e‘
print(list03)
#pop()方法用于移除列表的某个元素，若未指定具体元素就移除最后一个元素
print(list03.pop()) #移除列表中的最后一个元素，并返回。
print(list03.pop(1))    #移列表中索引为1的元素
print(list03)
#clear()用法用于清空列表
list03.clear()
print(list03)