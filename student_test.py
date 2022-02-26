import pytest
import student 

def string_builder(output):
    text = ''
    for i in range(3,len(output)):
        text+=output[i]
    return text

def test_one():
    try:
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

    except:
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
        student.print = lambda s1,s2,s3,s4,s5,s6,s7 : output.extend([s1,s2,s3,s4,s5,s6,s7])

        student.main()
        
        test_out = string_builder(output)

        assert 'Ollielikes tonap' in test_out and "oftennapall the way tolibrary" in test_out

def test_two():
    try:
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
    except:
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
        student.print = lambda s1,s2,s3,s4,s5,s6,s7 : output.extend([s1,s2,s3,s4,s5,s6,s7])

        student.main()
        
        test_out = string_builder(output)

        assert 'Roselikes tosing' in test_out and "oftensingall the way tothe mall" in test_out
    
def test_three():
    try:
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
    except:
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
        student.print = lambda s1,s2,s3,s4,s5,s6,s7 : output.extend([s1,s2,s3,s4,s5,s6,s7])

        student.main()
        
        test_out = string_builder(output)

        assert 'Karalikes tosend' in test_out and "oftensendall the way todaycare" in test_out
