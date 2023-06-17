# logoup列表生成程序 生成任意长度的logoup列表函数的程序
# 版权所有(C) 2023 周晟
# 本程序为自由软件：在自由软件基金会发布的GNU通用公共许可证的约束下，你可以对其进行再分发及修改。许可证版本为第三版本。
# 我们希望发布的这款程序有用，但其不带任何担保；甚至不默认保证它有经济价值和适合特定用途。详情参见GNU通用公共许可证。
# 你理当已收到一份GNU通用公共许可证的副本。如果你没有收到它，请查阅 http://www.gnu.org/licenses/ 。

print("欢迎使用给logoup这个垃圾东西擦屁股的列表函数生成器\n1.输入列表序数")
list_th = input()
list_th = str(list_th)
print("2.输入列表长度")
list_len = input()
print("下列为依据上述数据生成的logoup列表函数:\nVAR"+" "+"LIST"+"_"+list_th+"_LEN"+" = "+list_len+"\n")
for i in range(0, int(list_len)):
    print("VAR" + " " + "@list_" + list_th + "_" + str(i) + " = false")
print("\nFUNC LIST_" + list_th + "(@list_number, @out_or_edit, @edit)\n\tIF (@out_or_edit = true) THEN\n\t\tIF (@list_number = 0) THEN\n\t\t\t@list_" + list_th + "_0 = @edit\n\t\t\tRETURN true")
for i in range(1, int(list_len)):
    print("\t\tELSE IF (@list_number = " + str(i) + ") THEN\n\t\t\t@list_" + list_th + "_" + str(i) + " = @edit\n\t\t\tRETURN true")
print("\t\tEND\n\tIF (@list_number = 0) THEN\n\t\tRETURN @list_" + list_th + "_0")
for i in range(1, int(list_len)):
    print("\tELSE IF (@list_number = "+str(i)+") THEN\n\t\tRETURN @list_"+list_th+"_"+str(i))
print("\tEND\nEND")