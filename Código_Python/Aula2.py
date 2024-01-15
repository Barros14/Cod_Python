class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

if __name__ == "__main__":
    linked_list = LinkedList()

    while True:
        print("\nEscolha uma operação:")
        print("1. Inserir")
        print("2. Consultar")
        print("3. Alterar")
        print("4. Remover")
        print("5. Sair")
        
        choice = int(input("Digite o número da operação desejada: "))

        if choice == 1:
            data = input("Digite o valor a ser inserido: ")
            linked_list.insert(data)
            print(f"{data} foi inserido na lista.")
        elif choice == 2:
            data = input("Digite o valor a ser consultado: ")
            if linked_list.search(data):
                print(f"{data} está na lista.")
            else:
                print(f"{data} não está na lista.")
        elif choice == 3:
            old_data = input("Digite o valor a ser alterado: ")
            new_data = input("Digite o novo valor: ")
            if linked_list.search(old_data):
                linked_list.delete(old_data)
                linked_list.insert(new_data)
                print(f"{old_data} foi alterado para {new_data}.")
            else:
                print(f"{old_data} não está na lista para ser alterado.")
        elif choice == 4:
            data = input("Digite o valor a ser removido: ")
            if linked_list.search(data):
                linked_list.delete(data)
                print(f"{data} foi removido da lista.")
            else:
                print(f"{data} não está na lista para ser removido.")
        elif choice == 5:
            break
        else:
            print("Escolha uma opção válida.")
    
    linked_list.display()
