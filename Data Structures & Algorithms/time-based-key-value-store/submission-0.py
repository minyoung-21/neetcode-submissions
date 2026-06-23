class TimeMap:

    def __init__(self):
        self.ht = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.ht.keys():
            self.ht[key].append((value, timestamp))
        else:
            self.ht[key] = [(value, timestamp)]
        # print(self.ht[key])
        

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        if key in self.ht.keys():
            arr = self.ht[key]
        else:
            return ""
        r = len(arr) - 1
        res = ""

        while l <= r:
            m = l + (r - l) // 2

            if arr[m][1] == timestamp:
                return arr[m][0]
            else:
                # print(arr[m][1])
                if arr[m][1] < timestamp:
                    res = arr[m][0]
                    l = m + 1
                elif arr[m][1] > timestamp:
                    # if m != 0:
                    r = m - 1
                    # else:
                    #     return res

        return res
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)