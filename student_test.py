import pytest
import student 

def test_one(capsys):
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
    student.main()

    out, err = capsys.readouterr()
    assert 'Ollie likes to nap'in out and 'often nap all the way to library' in out, "Careful not to add the word \'the\' to the string"

def test_two(capsys):
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
    student.main()

    out, err = capsys.readouterr()
    assert 'Rose likes to sing' in out and "often sing all the way to the mall" in out, "Careful not to add the word \'the\' to the string"


def test_three(capsys):
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
    student.main()

    out, err = capsys.readouterr()
    assert 'Kara likes to send' in out and 'often send all the way to daycare' in out, "Careful not to add the word \'the\' to the string"
