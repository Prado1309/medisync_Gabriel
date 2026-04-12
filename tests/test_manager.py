import os
import pytest
from src.manager import MedicationManager

def test_add_medication_success():
    # Usamos um caminho de teste para não misturar com dados reais
    test_db = 'data/test_db.json'
    manager = MedicationManager(storage_path=test_db)
    
    # 1. Tenta adicionar um remédio
    resultado = manager.add_medication("Vitamina C", "1g", "09:00")
    
    # 2. Verifica se retornou True (sucesso)
    assert resultado is True
    
    # 3. Verifica se a lista agora tem 1 item
    assert len(manager.list_medications()) == 1
    
    # Limpeza: Deleta o arquivo de teste após terminar
    if os.path.exists(test_db):
        os.remove(test_db)

def test_add_medication_invalid():
    manager = MedicationManager(storage_path='data/tmp.json')
    # Tenta adicionar sem nome (deve falhar conforme nossa lógica)
    resultado = manager.add_medication("", "", "10:00")
    assert resultado is False