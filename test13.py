class sentence:

    def __init__(self,value,min,max,sent):
        self.min=min
        self.max=max
        self.sent = sent
        self.value = value
        print("the value of sent is",self.sent)

    def __iter__(self):
        return self

    def __next__(self):
        val = self.min
        abcd = self.sent.split(" ")
        #print("the value of abcd is",abcd)
        if self.min >= self.max:
            raise StopIteration
        else:
            val = self.value
            data = abcd[val]
            self.value = self.value + 1
            self.min+=1
            return data

a = sentence(0,0,5,"one two thre four tive")     

for abcd in a:
    print(abcd)

# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

