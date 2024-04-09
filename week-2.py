# TASK-1 (尚未加入小碧潭)
def find_and_print(messages, current_station):

    #List
    green_line = [
        "Songshan", "Nanjing Sanmin", "Taipei Arena", "Nanjing Fuxing",
        "Songjiang Nanjing", "Zhongshan", "Beimen", "Ximen", "Xiaonanmen",
        "Chiang Kai-Shek Memorial Hall", "Guting", "Taipower Building",
        "Gongguan", "Wanlong", "Jingmei", "Dapinglin", "Qizhang",
        "Xindian City Hall", "Xindian"
    ]

    #將messages裡面的value轉換成數字，數字代表在green_line的list裡面的數字
    friend_num = -1
    for station in green_line:
        friend_num += 1
        if any(station in value for value in messages.values()):
            for key, value in messages.items():
                if station in value:
                    messages[key] = str(friend_num)

    print(messages)  #確認新的messages dictionary

    my_num = 0
    for my_location in green_line:
        if current_station != my_location:
            my_num += 1
        else:
            break  #green_line[my_num] = current_station
    print(my_num)  #確認我這個車站現在在list的數字

    key_closest_friend = None  #先假設沒有最近的朋友
    min_difference = float('inf')  #無窮大的浮點數，用的時機要再查
    for key, value in messages.items():
        difference = abs(int(value) - my_num)  #計算我和朋友車站的數字差
        if difference < min_difference:
            min_difference = difference
            key_closest_friend = key

    print(key_closest_friend)
    return key_closest_friend

messages = {
    #"Leslie":"I'm at home near Xiaobitan station.",先假設沒有小碧潭
    "Bob": "I'm at Ximen MRT station.",
    "Mary": "I have a drink near Jingmei MRT station.",
    "Copper": "I just saw a concert at Taipei Arena.",
    "Vivian": "I'm at Xindian station waiting for you."
}

find_and_print(messages, "Wanlong")  # print Mary
find_and_print(messages, "Songshan")  # print Copper
#find_and_print(messages, "Qizhang") # print Leslie 還要加入小碧潭!!!!
find_and_print(messages, "Ximen")  # print Bob
find_and_print(messages, "Xindian City Hall")  # print Vivian





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