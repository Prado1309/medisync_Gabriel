from manager import MedicationManager

def main():
    manager = MedicationManager()
    
    while True:
        print("\n=== MediSync: Controle de Saúde ===")
        print("1. Cadastrar novo remédio")
        print("2. Listar todos os remédios")
        print("3. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do medicamento: ")
            dose = input("Dosagem (ex: 1 comprimido / 500mg): ")
            hora = input("Horário (ex: 08:00): ")
            if manager.add_medication(nome, dose, hora):
                print("\n✅ Medicamento salvo com sucesso!")
        
        elif opcao == "2":
            meds = manager.list_medications()
            print("\n--- LISTA DE MEDICAMENTOS ---")
            if not meds:
                print("Nenhum remédio cadastrado.")
            for m in meds:
                print(f"⏰ {m['time']} - {m['name']} ({m['dosage']})")
        
        elif opcao == "3":
            print("Saindo... Cuide-se bem!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()