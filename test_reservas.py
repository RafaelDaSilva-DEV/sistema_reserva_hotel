

import pytest
from reservas import processar_reservas

def test_todas_confirmadas():
    quartos = [101, 102, 103]
    reservas = [101, 102]
    confirmadas, recusadas = processar_reservas(quartos, reservas)
    assert confirmadas == [101, 102]
    assert recusadas == []

def test_todas_recusadas():
    quartos = [201, 202]
    reservas = [203, 204]
    confirmadas, recusadas = processar_reservas(quartos, reservas)
    assert confirmadas == []
    assert recusadas == [203, 204]

def test_mistas():
    quartos = [301, 302]
    reservas = [301, 303, 302, 304]
    confirmadas, recusadas = processar_reservas(quartos, reservas)
    assert confirmadas == [301, 302]
    assert recusadas == [303, 304]

def test_reserva_duplicada():
    quartos = [401, 402]
    reservas = [401, 401, 402]
    confirmadas, recusadas = processar_reservas(quartos, reservas)
    assert confirmadas == [401, 402]
    assert recusadas == [401]

def test_sem_quartos():
    quartos = []
    reservas = [101, 102]
    confirmadas, recusadas = processar_reservas(quartos, reservas)
    assert confirmadas == []
    assert recusadas == [101, 102]
