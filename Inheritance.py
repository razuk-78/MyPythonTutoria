class parent:
    def __init__(self):
        self.name = "parent"
    def getName(self):
        return self.name
class chiled(parent):
    def __init__(self):
        #if comment self.name will cast an error:"the self.id not define"
        self.name = "chiled"
def main():
    print("inheritance example")
    print(chiled().getName())
    print("end inheritance example")
if __name__ == "__main__":
    main()