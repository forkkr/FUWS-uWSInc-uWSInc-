from Parameters.ProgramVariable import ProgramVariable


class ProbabilityAssign():

    dataFile = None
    probsFile = None
    whereToWrite = None

    def __init__(self, datafile, probsfile, where):
        self.whereToWrite = open(where, 'w')
        self.probsFile = open(probsfile, 'r')
        self.dataFile = open(datafile, 'r')

        pass

    def Assigning(self):
        previous = self.probsFile.tell()
        cnt = 0
        for data in self.dataFile:
            print(data)
            seq = '('
            item = ''
            for ch in data:
                if ch == ' ' or ch == '\n':
                    if len(item) > 0:
                        item = int(item)
                        # print(item == -2)
                        if item == -1:
                            seq = seq[:len(seq)-1]+')'+'('
                        elif item == -2:
                            print(seq)
                            seq = seq[:len(seq)-1]
                            self.whereToWrite.write(seq)
                            self.whereToWrite.write('\n')
                            break
                        else:
                            self.probsFile.seek(previous)
                            prb = self.probsFile.readline().strip()
                            # print(self.probsFile.tell())
                            previous = self.probsFile.tell()
                            seq += str(item)+':'+str(prb)+','
                            cnt += 1
                        item = ''
                else:
                    item += ch


class WeightAssign():
    wgt_file = open('weights.csv','r')
    current_point = wgt_file.tell()

    @staticmethod
    def assign(itms):
        WeightAssign.wgt_file.seek(WeightAssign.current_point)
        for itm in itms:
            if itm not in ProgramVariable.wgt_dic:
                ProgramVariable.wgt_dic[itm] = float(WeightAssign.wgt_file.readline().strip())
