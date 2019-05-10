import os, io, json, math, re, importlib
import pytest
mod = importlib.import_module('main')


@pytest.mark.parametrize("args,esperado", [
    ([], "ayuda: use 'hola <nombre>'"),
    (["hola","Luis"], "Hola, Luis!"),
    (["x"], "comando no reconocido"),
])
def test_run(args, esperado):
    assert mod.run(args) == esperado
