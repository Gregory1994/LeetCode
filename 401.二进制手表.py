#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        hour = 0
        minute = num - hour
        res = []

        while 0 <= hour <= 3:
            if minute >= 6:
                hour += 1
                minute -= 1
            elif minute < 0:
                break
            else:
                hours = self.Hours(hour)
                minutes = self.Minutes(minute)

                for i in hours:
                    for j in minutes:
                        res.append(i +':' + j)
                hour += 1
                minute -= 1
        
        return res

    def Hours(self, hour):
        if hour == 0:
            return ['0']
        elif hour == 1:
            return ['1', '2', '4', '8']
        elif hour == 2:
            return ['3', '5', '6', '9', '10']
        elif hour == 3:
            return ['7', '11']

    def Minutes(self, minutes):
        res = []
        for i in range(60):
            m = i
            n = 0
            while m != 0:
                n += m & 1
                m >>= 1
            if n == minutes:
                if i < 10:
                    res.append('0' + str(i))
                else:
                    res.append(str(i))
        return res



