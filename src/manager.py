import json
import os

class MedicationManager:
    def __init__(self, storage_path='data/medications.json'):
        # Define onde os dados serão salvos
        self.storage_path = storage_path
        self.meds = self._load_data()

    def _load_data(self):
        # Se o arquivo existir, lê os dados. Se não, retorna uma lista vazia.
        if os.path.exists(self.storage_path):
            with open(self.storage_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []

    def add_medication(self, name, dosage, time):
        # Cria um dicionário com os dados do remédio
        if not name or not time:
            return False
        
        med = {"name": name, "dosage": dosage, "time": time}
        self.meds.append(med)
        self._save() # Salva no arquivo imediatamente
        return True

    def _save(self):
        # Garante que a pasta 'data' exista e salva o JSON
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        with open(self.storage_path, 'w', encoding='utf-8') as f:
            json.dump(self.meds, f, indent=4, ensure_ascii=False)

    def list_medications(self):
        # Retorna a lista organizada por horário
        return sorted(self.meds, key=lambda x: x['time'])