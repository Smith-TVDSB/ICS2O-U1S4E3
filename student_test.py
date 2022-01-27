import pytest
import student 



def test_one():
    input_values=['Ollie','nap','library']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert 'Ollie likes to nap' in output[3] and "often nap all the way to library" in output[3]

def test_two():
    input_values=['Rose','sing','the mall']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert 'Rose likes to sing' in output[3] and "often sing all the way to the mall" in output[3]
    
def test_one():
    input_values=['Kara','send','daycare']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert 'Kara likes to send' in output[3] and "often send all the way to daycare" in output[3]
