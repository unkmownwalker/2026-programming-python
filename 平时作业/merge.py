if __name__ == '__main__':
    class section:
        def __init__(self, start, end):
            self.s = start
            self.e = end
        def merge(self, other):
            if self.s > other.e or self.e < other.s:
                return False
            else:
                self.s = min(self.s, other.s)
                self.e = max(self.e, other.e)
                return True
    n = int(input())
    sections = []
    for i in range(0,n):
        s,e = input().split()
        s = int(s)
        e = int(e)
        sec=section(s,e)
        if not sections:
            sections.append(sec)
        else:
            for j in range(0, len(sections)):
                if sections[j].merge(sec):
                    break
            else:
                sections.append(sec)
    sections.sort(key=lambda x: x.s)
    delsect = []
    for sec in sections: 
        if sec in delsect: 
            continue
        for sec2 in sections:
           if sec2!=sec :
                if sec.merge(sec2):
                     delsect.append(sec2)
    for sec in delsect:
        if sec in sections:
            sections.remove(sec)
    for sec in sections:
        print(sec.s, sec.e)