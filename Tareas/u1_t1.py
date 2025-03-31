class BookCatalog:
    """
    Clase para representar un catálogo de libros.

    Atributos:
        catalog (dict): Un diccionario para almacenar la información de los libros.
    """

    def __init__(self):
        """
        Inicializa el catálogo de libros con un diccionario vacío.
        """
        self.catalog = {}

    def add_book(self, title, author, isbn, genre):
        """
        Agrega un libro al catálogo.

        Argumentos:
            title (str): El título del libro.
            author (str): El autor del libro.
            isbn (str): El ISBN del libro.
            genre (str): El género del libro.
        """
        self.catalog[isbn] = {"title": title, "author": author, "genre": genre}

    def search_book(self, query):
        """
        Busca libros en el catálogo.

        Argumentos:
            query (str): Título, autor o ISBN.

        Retorna:
            list: Una lista de diccionarios que contienen la información de los libros.
        """
        results = []
        for isbn, book_data in self.catalog.items():
            if (
                query in book_data["title"]
                or query in book_data["author"]
                or query == isbn
            ):
                results.append(book_data)
        return results

    def display_catalog(self):
        """
        Muestra todos los libros del catálogo.
        """
        for isbn, book_data in self.catalog.items():
            print(
                f"ISBN: {isbn}, Título: {book_data['title']}, Autor: {book_data['author']}, Género: {book_data['genre']}"
            )


class BankAccount:
    def __init__(self):
        self.transactions = []

    def deposit(self, amount):
        """Agrega una transacción de depósito."""
        if amount > 0:
            self.transactions.append({"type": "deposit", "amount": amount})
            print(f"Depósito de {amount}")
        else:
            print("El monto debe ser positivo.")

    def withdraw(self, amount):
        """Agrega una transacción de retiro si el saldo es suficiente."""
        if amount > 0:
            current_balance = self.check_balance()
            if current_balance >= amount:
                self.transactions.append({"type": "withdrawal", "amount": amount})
                print(f"Retiro de {amount}")
            else:
                print("Fondos insuficientes para el retiro.")
        else:
            print("El monto debe ser positivo.")

    def view_history(self):
        """Muestra todas las transacciones en orden cronológico."""
        if self.transactions:
            print("\nHistorial de transacciones:")
            for transaction in self.transactions:
                print(f"{transaction['type'].capitalize()} de {transaction['amount']}")
        else:
            print("Aún no hay transacciones.")

    def check_balance(self):
        """Calcula y devuelve el saldo actual basado en todas las transacciones."""
        balance = 0
        for transaction in self.transactions:
            if transaction["type"] == "deposit":
                balance += transaction["amount"]
            elif transaction["type"] == "withdrawal":
                balance -= transaction["amount"]
        return balance


class TodoList:
    def __init__(self, filename="todo.txt"):
        self.filename = filename
        self.tasks = self.load_todo_list()

    def load_todo_list(self):
        tasks = []
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    tasks.append(line.strip())
        except FileNotFoundError:
            pass  # Ignorar si el archivo no existe
        return tasks

    def save_todo_list(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def add_task(self, task):
        self.tasks.append(task)

    def mark_complete(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index] = self.tasks[task_index] + " [Complete]"

    def view_todo_list(self):
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")


# Función main para gestionar todos los casos
def main():
    # Gestionar una cuenta bancaria
    account = BankAccount()
    account.deposit(1000)
    account.withdraw(200)
    account.deposit(500)
    account.view_history()
    print(f"\nSaldo actual: {account.check_balance()}")

    # Gestionar un catálogo de libros
    catalog = BookCatalog()
    catalog.add_book(
        "The Lord of the Rings", "J.R.R. Tolkien", "9780547928227", "Fantasy"
    )
    catalog.add_book(
        "The Hitchhiker's Guide to the Galaxy",
        "Douglas Adams",
        "9780345391803",
        "Science Fiction",
    )

    search_results = catalog.search_book("Tolkien")
    print("\nResultados de búsqueda de 'Tolkien':", search_results)

    catalog.display_catalog()

    # Gestionar una lista de tareas (To-Do list)
    todo_list = TodoList()
    todo_list.add_task("Buy groceries")
    todo_list.add_task("Finish homework")

    print("\nLista de tareas:")
    todo_list.view_todo_list()

    todo_list.mark_complete(0)  # Marca como completada la primera tarea

    print("\nLista de tareas después de marcar la primera como completa:")
    todo_list.view_todo_list()

    todo_list.save_todo_list()


if __name__ == "__main__":
    main()
