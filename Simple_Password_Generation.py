import random
import Password_Keyword_Table as Table

print("密码生成器")

File_Name = 'Password_Keywords.txt'

Random_Time_Least=3 #最少随机抽取的“密码组成值”的数量。

Random_Time_Most=8 #最多随机抽取的“密码组成值”的数量。



key3=Table.T_key4#key3列表记录所有.txt文件中的数据。

Label_C_Group=Table.T_List_Group_2#Label_C_Group列表用记录单一"密码标签"被包含的的组号。

Grade_C_Group=Table.T_List_Group_1#Grade_C_Group列表用记录单一"密码等级"被包含的的组号。

Label_Input_List=[]#用户输入的Label_C_Group列表中对应的标签序号。并非key3组号。

Grade_Input_List=[]#用户输入的Grade_C_Group列表中对应的等级序号。并非key3组号。

Label_Group_List=[]#所有用户选中的"密码标签"对应的组号。

Grade_Group_List=[]#所有用户选中的"密码等级"对应的组号。

Final_Group_List=[]#筛选后用户最终选中的组号。


#----------分割线，以上用于记录全局变量。----------
#----------分割线，该部分用于文件内容读取。----------


#该函数用于读取.txt文件内的数据，生成key3数组。
def File_Input(File_Name):
    with open(File_Name,encoding='UTF-8') as File_Object:
        Group_Counter=0 #组计数器，用于计数共有多少组数据。
        for Line_All in File_Object:
            First_Char=Line_All[0]
            Line=Line_All[1:-1]

            if First_Char=='@':
                key3[Group_Counter][0][0]=str(Group_Counter) #记录组数

            if First_Char=='=':
                Word=''
                Word_Counter=0
                for One_Char in Line:

                    if One_Char != ',':
                        Word=Word+One_Char
                    elif One_Char == ',':
                        key3[Group_Counter][1][Word_Counter]=Word
                        Word_Counter=Word_Counter+1
                        Word=''
                    elif One_Char =='/n':
                        continue

            elif First_Char=='#':
                Word=''
                Word_Counter=0
                for One_Char in Line:
                    if One_Char != ',':
                        Word=Word+One_Char
                    elif One_Char == ',':
                        key3[Group_Counter][2][Word_Counter]=Word
                        Word_Counter=Word_Counter+1
                        Word=''
                    elif One_Char =='/n':
                        continue

            elif First_Char=='&':
                for One_Char in Line:
                    if One_Char != ',':
                        Word=Word+One_Char
                    elif One_Char == ',':
                        key3[Group_Counter][3][0]=Word
                Group_Counter=Group_Counter+1#最后一项记录完成后组号计数器自增1。


#----------分割线，该部分用于处理文件中的密码标签。----------


#这个函数将从key3数组中抽取所有"密码标签"，并记录组号。
def Label_Link_Group_Loop_Part():
    Loop_1st_Counter=0#即为组号的记录。
    Loop_2nd_Check=0
    for Loop_1st in key3:#第一层循环，用于遍历整组“组号——密码生成值——密码标签——密码等级”对应关系
        for Loop_2nd in Loop_1st:#第二层循环，单组内部的每一种数值的列表。
            if Loop_2nd_Check==2:#用于判断是否为第三列“密码标签”。
                for Loop_3rd in Loop_2nd:#第三层循环，用于将密码标签存放至Label_C_Group列表。
                    if Loop_3rd=='':continue
                    Label_Link_Group_Link_Part(Loop_3rd,Loop_1st_Counter)
            Loop_2nd_Check=Loop_2nd_Check+1
            if Loop_2nd_Check==4:
                Loop_2nd_Check=0
        Loop_1st_Counter=Loop_1st_Counter+1


#这个函数用于单个标签的所有组号链接记录。
def Label_Link_Group_Link_Part(Label_Name,Group_Number_Transmission):
    Label_Same_Check=Label_Link_Group_Link_Part_Same_Check(Label_Name)

    if Label_Same_Check==-1:#收录值为-1，没有相同重合。
        Empty_Element_Check_1_Counter=0
        Empty_Element_Check_2_Counter=0
        Break_Flag=0
        for Empty_Element_Check_1 in Label_C_Group:
            for Empty_Element_Check_2 in Empty_Element_Check_1:
                if Empty_Element_Check_2_Counter==0 and Empty_Element_Check_2=='':
                    Label_Number=Empty_Element_Check_1_Counter
                    Label_C_Group[Label_Number][0]=str(Label_Name)
                    Label_C_Group[Label_Number][1]=str(Group_Number_Transmission)
                    Break_Flag=1
                    break
                Empty_Element_Check_2_Counter=Empty_Element_Check_2_Counter+1
            if Break_Flag==1:break
            Empty_Element_Check_2_Counter=0
            Empty_Element_Check_1_Counter=Empty_Element_Check_1_Counter+1

    elif Label_Same_Check!=-1:#收录值为重复的数组序号，有相同重合。
        Label_Number=Label_Same_Check
        Empty_Element_Number=Label_Link_Group_Link_Part_Same_Check_Empty(Label_Number)
        Label_C_Group[Label_Number][Empty_Element_Number]=str(Group_Number_Transmission)
        Label_C_Group[Label_Number][0]=str(Label_Name)


#该函数用于检测输入的"密码标签"是否与Label_C_Group中已有的标签重合。
#若没有重合，则返回-1。若有重合，则返回重合的组号。
def Label_Link_Group_Link_Part_Same_Check(Label_Name):
    Loop_1st_Counter=0
    Label_Same_Check=0
    for Loop_1st in Label_C_Group:#遍历[密码标签,组号]的每一列。
        if Loop_1st[0]==Label_Name:
            Label_Same_Check=1
            Label_Number=Loop_1st_Counter
            break
        Loop_1st_Counter=Loop_1st_Counter+1

    if Label_Same_Check==0:
        return -1
    else:
        return Label_Number

#该函数用于检索已有标签的最小的空字符串列表索引。
def Label_Link_Group_Link_Part_Same_Check_Empty(Label_Number):
    Empty_Element_Check_List=Label_C_Group[Label_Number]
    for Empty_Element_Check_Loop in range(len(Empty_Element_Check_List)-1):
        if Empty_Element_Check_List[Empty_Element_Check_Loop] == '' and Empty_Element_Check_Loop!= 0:
            Empty_Element_Number = Empty_Element_Check_Loop
            break
    return Empty_Element_Number

#输出Labe_C_Group列表中的标签，让用户进行选择。
def Output_Label_Number():
    print("从以下密码标签中输入期望的标签序号，以回车分隔，输入0代表结束输入。")
    Loop_Label_Number_Counter=0
    for Output_Loop in Label_C_Group:
        if Output_Loop[0]!='':
            print(str(Loop_Label_Number_Counter))
            print(Output_Loop)
            Loop_Label_Number_Counter=Loop_Label_Number_Counter+1

def Input_Label_Number():
    Label_Input_Check=1
    while Label_Input_Check==1:
        Label_Input=eval(input())
        if Label_Input==0:
            break
        Label_Input_List.append(Label_Input)


#----------分割线，该部分用于处理文件中的密码等级。----------


#这个函数将从key3数组中抽取所有"密码等级"，并记录组号。
def Grade_Link_Group_Loop_Part():
    Loop_1st_Counter=0#即为组号的记录。
    Loop_2nd_Check=0
    for Loop_1st in key3:#第一层循环，用于遍历整组“组号——密码生成值——密码等级”对应关系
        for Loop_2nd in Loop_1st:#第二层循环，单组内部的每一种数值的列表。
            if Loop_2nd_Check==3:#用于判断是否为第三列“密码等级”。
                for Loop_3rd in Loop_2nd:
                    if Loop_3rd=='':continue
                    Grade_Link_Group_Link_Part(Loop_3rd,Loop_1st_Counter)
            Loop_2nd_Check=Loop_2nd_Check+1
        if Loop_2nd_Check==4:
            Loop_2nd_Check=0
        Loop_1st_Counter=Loop_1st_Counter+1

#这个函数用于单个密码等级的所有组号链接记录。
def Grade_Link_Group_Link_Part(Grade_Name,Group_Number_Transmission):
    Grade_Same_Check=Grade_Link_Group_Link_Part_Same_Check(Grade_Name)

    if Grade_Same_Check==-1:#收录值为-1，没有相同重合。
        Empty_Element_Check_1_Counter=0
        Empty_Element_Check_2_Counter=0
        Break_Flag=0
        for Empty_Element_Check_1 in Grade_C_Group:
            for Empty_Element_Check_2 in Empty_Element_Check_1:
                if Empty_Element_Check_2_Counter==0 and Empty_Element_Check_2=='':
                    Grade_Number=Empty_Element_Check_1_Counter
                    Grade_C_Group[Grade_Number][0]=str(Grade_Name)
                    Grade_C_Group[Grade_Number][1]=str(Group_Number_Transmission)
                    Break_Flag=1
                    break
                Empty_Element_Check_2_Counter=Empty_Element_Check_2_Counter+1
            if Break_Flag==1:break
            Empty_Element_Check_2_Counter=0
            Empty_Element_Check_1_Counter=Empty_Element_Check_1_Counter+1

    elif Grade_Same_Check!=-1:#收录值为重复的数组序号，有相同重合。
        Grade_Number=Grade_Same_Check
        Empty_Element_Number=Grade_Link_Group_Link_Part_Same_Check_Empty(Grade_Number)
        Grade_C_Group[Grade_Number][Empty_Element_Number]=str(Group_Number_Transmission)
        Grade_C_Group[Grade_Number][0]=str(Grade_Name)


#该函数用于检测输入的"密码标签"是否与Grade_C_Group中已有的标签重合。
#若没有重合，则返回-1。若有重合，则返回重合的组号。
def Grade_Link_Group_Link_Part_Same_Check(Grade_Name):
    Loop_1st_Counter=0
    Grade_Same_Check=0
    for Loop_1st in Grade_C_Group:#遍历[密码等级,组号]的每一列。
        if Loop_1st[0]==Grade_Name:
            Grade_Same_Check=1
            Grade_Number=Loop_1st_Counter
            break
        Loop_1st_Counter=Loop_1st_Counter+1

    if Grade_Same_Check==0:
        return -1
    else:
        return Grade_Number

#该函数用于检索已有标签的最小的空字符串列表索引。
def Grade_Link_Group_Link_Part_Same_Check_Empty(Grade_Number):
    Empty_Element_Check_List=Grade_C_Group[Grade_Number]
    for Empty_Element_Check_Loop in range(len(Empty_Element_Check_List)-1):
        if Empty_Element_Check_List[Empty_Element_Check_Loop] == '' and Empty_Element_Check_Loop!= 0:
            Empty_Element_Number = Empty_Element_Check_Loop
            break
    return Empty_Element_Number

#输出Labe_C_Group列表中的等级，让用户进行选择。
def Output_Grade_Number():
    print("从以下密码标签中输入期望的等级序号，以回车分隔，输入0代表结束输入。")
    Loop_Grade_Number_Counter=0
    for Output_Loop in Grade_C_Group:
        if Output_Loop[0]!='':
            print(str(Loop_Grade_Number_Counter))
            print(Output_Loop)
            Loop_Grade_Number_Counter=Loop_Grade_Number_Counter+1

def Input_Grade_Number():
    Grade_Input_Check=1
    while Grade_Input_Check==1:
        Grade_Input=eval(input())
        if Grade_Input==0:
            break
        Grade_Input_List.append(Grade_Input)


#----------分割线，该部分用于最终生成结果的处理。----------

#该函数依照用户输入的"密码标签"和"密码等级"选出备选的"密码组成值"。
def Data_Extraction_And_Generation():
    global Label_Group_List
    global Grade_Group_List

    Data_Extraction_List_Group_Extract()

    Data_Extraction_Sift()

    Data_Generation()


def Data_Extraction_List_Group_Extract():#提取用户选中的_C_Link列表中的密码标签与密码等级内组号
    global Label_Group_List
    global Grade_Group_List

    for Label_Select in Label_Input_List:#选出所有输入的"密码标签"对应的组号。
        Label_Group_List = Label_Group_List + Data_Extraction_List_Group_Single_Extract(Label_C_Group[Label_Select])
    
    for Grade_Select in Grade_Input_List:#选出所有输入的"密码等级"对应的组号。
        Grade_Group_List = Grade_Group_List + Data_Extraction_List_Group_Single_Extract(Grade_C_Group[Grade_Select])


#循环生成密码数据
def Data_Generation():
    Loop_Check=1
    while Loop_Check==1:
        Data_Generation_Single_Part()
        print("重新生成则输入1，结束则输入0")
        Loop_Check=eval(input())

#单次密码生成
def Data_Generation_Single_Part():
    Generation_List=['']
    Generation_String=''
    Generation_Times=random.randint(Random_Time_Least,Random_Time_Most)#进行若干次随机筛选"密码组成值"。
    for Loop_1 in range(Generation_Times):
        #随机抽取一个Input_Group_Number数列内的组号。
        One_Time_Number=random.randint(0,len(Final_Group_List)-1)
        Extracted_Group=Final_Group_List[One_Time_Number]
        #在这一组号中的"密码生成值"内随机选出一个。
        Composition_Value_List_Range=len(key3[Extracted_Group][1])
        One_Time_Composition_Value_Number=random.randint(0,Composition_Value_List_Range-1)
        Select_Composition_Value=key3[Extracted_Group][1][One_Time_Composition_Value_Number]
        Generation_List.append(Select_Composition_Value)
    
    for Generation_Loop in Generation_List:
        Generation_String=Generation_String+Generation_Loop

    print(Generation_String)

#该函数用于提取Label_C_Group或者Grade_C_Group中每一列的组号。
def Data_Extraction_List_Group_Single_Extract(List_Transmission):
    Reply_List=List_Transmission
    Return_List=[]

    for Group_Loop in range(1,len(Reply_List)):
        if Reply_List[Group_Loop]=='':
            break
        elif Reply_List[Group_Loop]!='':
            Return_List.append(eval(Reply_List[Group_Loop]))

    return Return_List

#该函数用于从"密码等级"的组号筛选"密码标签"的组号。
def Data_Extraction_Sift():
    global Label_Group_List
    global Grade_Group_List
    
    Processed_Label_Group_List=Label_Group_List
    Number_Same_Check=0
    
    for Loop_1 in range(len(Label_Group_List)):
        for Loop_2 in range(len(Grade_Group_List)):
            if Label_Group_List[Loop_1] != Grade_Group_List[Loop_2]:
                Number_Same_Check=1
        if Number_Same_Check==1:pass
        elif Number_Same_Check==0:#若无该值，则记为0，应被删除。
            Processed_Label_Group_List.remove(Label_Group_List[Loop_1])
        Number_Same_Check=0
    global Final_Group_List
    Final_Group_List=Processed_Label_Group_List




#----------分割线，该部分用于面向用户输入输出、主函数内的子函数调用、调试。----------


File_Input(File_Name)

Label_Link_Group_Loop_Part()

Grade_Link_Group_Loop_Part()

print(key3)
print('-------------------')
print(Label_C_Group)
print('-------------------')
print(Grade_C_Group)


Output_Label_Number()
Input_Label_Number()

print("输入的标签序号为")
print(Label_Input_List)

Output_Grade_Number()
Input_Grade_Number()

print("输入的等级序号为")
print(Grade_Input_List)

Data_Extraction_And_Generation()