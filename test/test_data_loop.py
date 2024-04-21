from data_loop import DataLoop

def test_data_loop_size():
    dl = DataLoop()    
    assert dl.size() == 5

def test_data_loop_popleft_first():
    dl = DataLoop()
    assert dl.popleft() == "a@@@@A00000   F2"

def test_data_loop_popleft_second():
    dl = DataLoop()
    dl.popleft()
    
    assert dl.popleft() == "b@@@@A   00  0D3"

def test_data_loop_popleft_last():
    dl = DataLoop()
    
    for i in range (0,4):
        dl.popleft()
    
    assert dl.popleft() == "e@@@@A000000 w5D"

def test_data_loop_popleft_repeat_first():
    dl = DataLoop()
    
    for i in range (0,5):
        dl.popleft()
    
    assert dl.popleft() == "a@@@@A00000   F2"
    
def test_data_loop_popleft_repeat_second():
    dl = DataLoop()
    
    for i in range (0,6):
        dl.popleft()
    
    assert dl.popleft() == "b@@@@A   00  0D3"
