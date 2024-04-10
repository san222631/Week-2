# TASK-1 (已加入小碧潭)
def find_and_print(messages, current_station):

#將messages裡面的value轉換成數字，數字代表在green_line的value裡面的數字
    for friend, conversation in messages.items():
        for station in green_line:
            if station in conversation:
                messages[friend] = green_line[station]
                break #超級重要的一個打斷!!!!!!!這個可以區分messages裡面的新店跟新店市政府
    print(messages)  #確認新的messages dictionary

    
    #確認我在的車站，現在在list的數字
    my_num = int(green_line[current_station])        
    print(my_num)  #確認我這個車站現在在list的數字

    
    #狀況1:有朋友在小碧潭+有朋友在七張+我在新店或新店市政府
    friend_xiaobitan = False
    friend_qizhang = False
    me_xindian = current_station in ["Xindian City Hall", "Xindian"]

    key_closest_friend = None  #靠我最近的朋友，先假設None
    min_difference = 100 #我和朋友最短的差距，先假設無窮大float('inf')或是自選100
    
    for station_value in messages.values():
        if "17" in station_value:
            friend_xiaobitan = True
        if "16" in station_value:
            friend_qizhang = True
            
    #狀況1:有朋友在小碧潭+有朋友在七張+我在新店或新店市政府
    if friend_xiaobitan and friend_qizhang and me_xindian:
        print("special-1")
        for key, value in messages.items():
            if value == "16":
                messages[key] = "18"
            
        for key, value in messages.items():
            difference = abs(int(value) - my_num)  #計算我和朋友車站的數字差
            if difference < min_difference:
                min_difference = difference
                key_closest_friend = key
                
    else:
        print("normal")
        for key, value in messages.items():
            difference = abs(int(value) - my_num)  #計算我和朋友車站的數字差
            if difference < min_difference:
                min_difference = difference
                key_closest_friend = key    
    
    print(key_closest_friend)
    return key_closest_friend


green_line = {
    "Songshan":"0",
    "Nanjing Sanmin":"1",
    "Taipei Arena":"2",
    "Nanjing Fuxing":"3",
    "Songjiang Nanjing":"4",
    "Zhongshan":"5",
    "Beimen":"6",
    "Ximen":"7",
    "Xiaonanmen":"8",
    "Chiang Kai-Shek Memorial Hall":"9",
    "Guting":"10",
    "Taipower Building":"11",
    "Gongguan":"12",
    "Wanlong":"13",
    "Jingmei":"14",
    "Dapinglin":"15",
    "Qizhang":"16",
    "Xiaobitan":"17", #異數
    "Xindian City Hall":"19",
    "Xindian":"20",
}

messages = {
    "Leslie":"I'm at home near Xiaobitan station.", #異數 
    "Bob": "I'm at Ximen MRT station.", 
    "Mary": "I have a drink near Jingmei MRT station.",
    "Copper": "I just saw a concert at Taipei Arena.",
    "Vivian": "I'm at Xindian station waiting for you." #找出要怎麼區分新店跟新店市政府
}


find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian





# TASK-3
def func(*data):

    middle_name = []
    for string in data:
        if len(string) == 2 or len(string) == 3:
            middle_name.append(string[1])

        elif len(string) == 4 or len(string) == 5:
            middle_name.append(string[2])

    unique_name_index = []
    sum = 0
    for index, string in enumerate(middle_name):
        sum += middle_name.count(string)
        if middle_name.count(string) == 1:  #count顯示這個string出現在list裡面幾次
            unique_name_index.append((string, index))
            print(data[unique_name_index[0][1]])
    if sum % 2 == 0:
        print("沒有")

func("彭大牆", "陳王明雅", "吳明")  # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花")  # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")  # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆")  # print 夏曼藍波安





# TASK-4
def get_number(index):
    if index % 3 == 1:
        result = int(((index - 1) / 3) * 7 + 4)
        print(result)
    elif index % 3 == 2:
        result = int(((index - 2) / 3) * 7 + 8)
        print(result)
    elif index % 3 == 0:
        result = int((index / 3) * 7)
        print(result)

get_number(1)  # print 4
get_number(5)  # print 15
get_number(10)  # print 25
get_number(30)  # print 70