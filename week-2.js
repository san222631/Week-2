//TASK 1
function findAndPrint(messages, current_station) {
    // 將 messages 裡面的 value 轉換成數字，數字代表在 green_line 的 value 裡面的數字
    for (let friend in messages) {
        for (let station in green_line) {
            if (messages[friend].includes(station)) {
                messages[friend] = green_line[station];
                break; // 超級重要的一個打斷!!!!!!!這個可以區分 messages 裡面的新店跟新店市政府
            }
        }
    }
    // console.log(messages); // 確認新的 messages dictionary

    // 確認我在的車站，現在在 list 的數字
    let my_num = parseInt(green_line[current_station]);
    // console.log(my_num); // 確認我這個車站現在在 list 的數字

    // 狀況1: 有朋友在小碧潭 + 有朋友在七張 + 我在新店或新店市政府
    let friend_xiaobitan = false;
    let friend_qizhang = false;
    let me_xindian = current_station === "Xindian City Hall" || current_station === "Xindian";

    let key_closest_friend = null; // 靠我最近的朋友，先假設 None
    let min_difference = 100; // 我和朋友最短的差距，先假設無窮大

    for (let station_value of Object.values(messages)) {
        if (station_value.includes("17")) {
            friend_xiaobitan = true;
        }
        if (station_value.includes("16")) {
            friend_qizhang = true;
        }
    }

    // 狀況1: 有朋友在小碧潭 + 有朋友在七張 + 我在新店或新店市政府
    if (friend_xiaobitan && friend_qizhang && me_xindian) {
        // console.log("special-1");
        for (let [key, value] of Object.entries(messages)) {
            if (value === "16") {
                messages[key] = "18";
            }
        }

        for (let [key, value] of Object.entries(messages)) {
            let difference = Math.abs(parseInt(value) - my_num); // 計算我和朋友車站的數字差
            if (difference < min_difference) {
                min_difference = difference;
                key_closest_friend = key;
            }
        }
    } else {
        // console.log("normal");
        for (let [key, value] of Object.entries(messages)) {
            let difference = Math.abs(parseInt(value) - my_num); // 計算我和朋友車站的數字差
            if (difference < min_difference) {
                min_difference = difference;
                key_closest_friend = key;
            }
        }
    }

    console.log(key_closest_friend);
    return key_closest_friend;
}

let green_line = {
    "Songshan": "0",
    "Nanjing Sanmin": "1",
    "Taipei Arena": "2",
    "Nanjing Fuxing": "3",
    "Songjiang Nanjing": "4",
    "Zhongshan": "5",
    "Beimen": "6",
    "Ximen": "7",
    "Xiaonanmen": "8",
    "Chiang Kai-Shek Memorial Hall": "9",
    "Guting": "10",
    "Taipower Building": "11",
    "Gongguan": "12",
    "Wanlong": "13",
    "Jingmei": "14",
    "Dapinglin": "15",
    "Qizhang": "16",
    "Xiaobitan": "17",
    "Xindian City Hall": "19",
    "Xindian": "20"
};

let messages = {
    "Leslie": "I'm at home near Xiaobitan station.",
    "Bob": "I'm at Ximen MRT station.",
    "Mary": "I have a drink near Jingmei MRT station.",
    "Copper": "I just saw a concert at Taipei Arena.",
    "Vivian": "I'm at Xindian station waiting for you."
};

findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bob
findAndPrint(messages, "Xindian City Hall"); // print Vivian


// task 2
let schedule = {};

function book(consultants, hour, duration, criteria) {
    // 客戶要的時間段
    let hours_to_check = Array.from({ length: duration }, (_, i) => hour + i);

    // 確認大家現有的時間表
    let available_pp = {};
    for (let consultant in schedule) {
        if (!hours_to_check.some(hour => schedule[consultant].includes(hour))) {
            available_pp[consultant] = schedule[consultant];
        }
    }

    // 確認到底有沒有人有空
    if (Object.keys(available_pp).length > 0) {
        let max_rate = 0;
        let min_price = 5000;
        let chosen_one = null;

        for (let person in available_pp) {
            let consultant = consultants.find(c => c.name === person);
            if (!consultant) continue;

            if (criteria === "rate") {
                if (consultant.rate > max_rate) {
                    max_rate = consultant.rate;
                    chosen_one = person;
                }
            } else if (criteria === "price") {
                if (consultant.price < min_price) {
                    min_price = consultant.price;
                    chosen_one = person;
                }
            }
        }

        if (chosen_one !== null) {
            console.log(chosen_one);
            schedule[chosen_one] = [...(schedule[chosen_one] || []), ...hours_to_check];
        }

    } else {
        console.log("No Service");
    }
}

// 這個不能改
let consultants = [{
    "name": "John",
    "rate": 4.5,
    "price": 1000
}, {
    "name": "Bob",
    "rate": 3,
    "price": 1200
}, {
    "name": "Jenny",
    "rate": 3.8,
    "price": 800
}];

// 把consultants的資料更新到schedule上面
consultants.forEach(info => {
    let checking_new_name = info.name;
    if (!(checking_new_name in schedule)) {
        schedule[checking_new_name] = [];
    }
});


book(consultants, 15, 1, "price"); // Jenny
book(consultants, 11, 2, "price"); // Jenny
book(consultants, 10, 2, "price"); // John
book(consultants, 20, 2, "rate"); // John
book(consultants, 11, 1, "rate"); // Bob
book(consultants, 11, 2, "rate"); // No Service
book(consultants, 14, 3, "price"); // John



// TASK 3
function func(...data) {
    let middleName = [];
    //使用 for (let string of data)也可，但下面這個比較能精確控制index
    for (let i = 0; i < data.length; i++) {
        let string = data[i];
        if (string.length === 2 || string.length === 3) {
            middleName.push(string[1]);
        } else if (string.length === 4 || string.length === 5) {
            middleName.push(string[2]);
        }
    }

    let uniqueNameIndex = [];
    let sum = 0;
    for (let i = 0; i < middleName.length; i++) {
        let string = middleName[i];
        sum += middleName.filter(item => item === string).length;
        //暫時不理解為什麼不能改成 (sum === 1)，如果改成這樣"林花花"跟"夏曼藍波安"印不出來
        if (middleName.filter(item => item === string).length === 1) {
            uniqueNameIndex.push({ string, index: i });
            console.log(data[uniqueNameIndex[0].index]);
        }
    }

    if (sum % 2 === 0) {
        console.log("沒有");
    }
}

func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安




// TASK 4
function getNumber(index) {
    //在JS，最好declare variables before using them, 不先declare也可以用，但在strict mode會有問題，而且加了會讓code比較好懂
    let result; 
    //建議使用===來避免JS強制轉換類型
    if (index % 3 === 1){
        result = Math.floor(((index - 1) / 3) * 7 + 4); //Math.floor()是取整數
        console.log(result);        
    }else if (index % 3 === 2){
        result = Math.floor(((index - 2) / 3) * 7 + 8);
        console.log(result); 
    }else if (index % 3 === 0){
        result = Math.floor((index / 3) * 7);
        console.log(result); 
    }    
}

getNumber(1)
getNumber(5); // print 15
getNumber(10); // print 25
getNumber(30); // print 70






