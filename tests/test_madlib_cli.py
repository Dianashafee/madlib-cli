
from madlib_cli import __version__
from madlib_cli.madlib_cli import *

def test_version():
    assert __version__ == '0.1.0'


def test_read():
    actual = read('assets/madlib_source.txt')
    expected = open('assets/madlib_source.txt','r').read()
    assert expected == actual 

def test_parse():
    actual = parse('assets/madlib_source.txt')
    expected = ['0','1', '2', '3', '4']
    assert expected == actual 


def test_merge():
    actual = merge('Guess things about me  ^.^! \n My name is Diana i love {0} and {1}, However i am studying {2} \n but you know i can never stop {3}, and i always {4} Big ^.^', ['singing', 'painting', 'translation', 'dreaming', 'dream'])
    expected = 'Guess things about me  ^.^! \n My name is Diana i love singing and painting, However i am studying translation \n but you know i can never stop dreaming, and i always dream Big ^.^'
    assert expected == actual



