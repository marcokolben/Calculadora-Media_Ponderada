from calculadora import calcula_media, situacao
import pytest


def test_media_simples():
    #ARRANGE
    n1, n2, n3 = 8.0, 7.0, 9.0

    #ACT
    resultado = calcula_media(n1, n2, n3)

    #ASSERT
    assert resultado == 8.25


    def test_aluno_aprovado():
        assert situacao(7.0) == "Aprovado"
        assert situacao(8.5) == "Aprovado"
        assert situacao(10.0) == "Aprovado"


    def test_aluno_recuperacao():
        assert situacao(4.0) == "Recuperação"
        assert situacao(6.9) == "Recuperação"
        

    def test_aluno_reprovado(): 
        assert situacao(3.9) == "Reprovado"
        assert situacao(0.0) == "Reprovado"

def test_nota_acima_dez():
    with pytest.raises(ValueError):
        calcula_media(11.0, 7.0, 8.0)

def test_nota_negativa():
    with pytest.raises(ValueError):
        calcula_media(7.0, -1.0, 8.0)