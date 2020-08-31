def fetchDataId(seq):

    otherDataId_list = ['F-C0032-001'] # 今明36小時天氣預報
    
    
    if seq < len(otherDataId_list):
        return otherDataId_list[seq]
    else:
        return ''