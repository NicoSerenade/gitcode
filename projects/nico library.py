library_name = 'Nico\'s library'
available_books = ['python basics', 'life and death', 'deepwork', 'the art of war', 'the power of now', 'pepito', 'juanito']
borrowed_books = {}
max_borrow = 5
password = 123
banned_users = set()
#1
def show_available_books():
    print('Available books in Nico\'s library:')
    if available_books:
        for book in available_books:
            print(f'- {book}')
    else:
        print('No available books right now!')


#2
def borrow_a_book(user, book):
    if not user in banned_users:
        if book in available_books:
            if user in borrowed_books:
                if len(borrowed_books[user]) < max_borrow:
                    borrowed_books[user].append(book)
                    available_books.remove(book)
                    print(f'{user} has borrowed {book}')
                    if len(borrowed_books[user]) < max_borrow:
                        choice = input('Would you like to borrow another book? Enter (y): ').lower()
                        if choice == 'y':
                            book = input('Enter the book you\'d like to borrow: ').lower()
                            borrow_a_book(user, book)
                        
                else:
                    print(f'You already have borrowed {max_borrow} books, returnt at least one of them to borrow another.')
                
            else: 
                borrowed_books[user] = [book]
                available_books.remove(book)
                print(f'{user} has borrowed {book}')
                choice = input('Would you like to borrow another book? Enter (y): ').lower()
                if choice == 'y':
                    book = input('Enter the book you\'d like to borrow: ').lower()
                    borrow_a_book(user, book)
            
        else:
            print('Book not found in system')
    else:
        print(f'{user}, you are banned!')

3#
def return_a_book(user, book):
    if user in borrowed_books and book in borrowed_books[user]:
       borrowed_books[user].remove(book)
       available_books.append(book)
       print(f'{user} removed {book} successfully')

    elif user in borrowed_books:
        print(f'{user} have not borrowed {book} before.')

    else:
        print(f'{user} is not in the system')

#4
def show_borrowed_books(user):
    if user in borrowed_books:
        print(f'{user} borrowed history:')

        for book in borrowed_books[user]:
            print(f'-{book}')


1#
def add_book(book):
        available_books.append(book)
        print(f'{book} added successfully!')

#2
def delete_book(book):
    for x in available_books:
        if x == book:
            available_books.remove(book)
            print(f'{book} removed successfully!')
    
#3 
def show_all_data():
    if borrowed_books:
        for user in borrowed_books: 
            print(f'{user} borrowed history:')
            for book in borrowed_books[user]:
                print(f'-{book}')
    else:
        print('No books have been borrowed yet')
#4 
def ban_users(user):
    if user in borrowed_books:
        banned_users.add(user)
        available_books.extend(borrowed_books[user])
        del borrowed_books[user]  
        print(f'{user} have been banned successfully!')     
    else:
        print(f'{user} is not in the system.')

#5
def unban_users(user):
    if user in banned_users:
        banned_users.remove(user)
        print(f'{user} have been unbanned successfully!') 
    else:
        print(f'{user} is not currently banned.')

# main menu

def main():
    
    print(f"Welcome to {library_name}!")

    while True:
        print("\nChoose an action:")
        print("1. Show available books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Show my borrowed books")
        print("5. Exit")
        print('Password. for admin options')

        choice = (input("Enter the number of your choice: "))
        if choice.isdigit():
            choice = int(choice)

            if choice == 1:
                show_available_books()
            
            elif choice == 2:
                user = input('Enter your name: ').title()
                book = input('Enter the book you\'d like to borrow: ').lower()
                borrow_a_book(user, book)

            elif choice == 3:
                user = input('Enter your name: ').title()
                book = input('Enter the book you\'d like to return: ').lower()
                return_a_book(user, book)

            elif choice == 4:
                user = input('Enter your name: ').title()
                show_borrowed_books(user)
            
            elif choice == 5:
                print('Thank you for choosing us, have a great day!')
                break

            elif choice == password:
                while True:
                    print('Admin menu')
                    print("\nChoose an action:")
                    print('1. Add a new book')
                    print('2. Delete a descontinued book')
                    print('3. Show all borrowed books and user data')
                    print('4. Ban users')
                    print('5. Unban users')
                    print('6. Main menu')

                    
                    choice = (input("Enter the number of your choice: "))
                    if choice.isdigit():
                        choice = int(choice)

                        if choice == 1:
                            book = input('Enter the book\'s name: ')
                            add_book(book)

                        elif choice == 2:
                            book = input('Enter the book\'s name: ').lower()
                            delete_book(book)
                        
                        elif choice == 3:
                            show_all_data()

                        elif choice == 4:
                            user = input('Enter user\'s name: ').title()
                            ban_users(user)
                        
                        elif choice == 5:
                            user = input('Enter user\'s name: ').title()
                            unban_users(user)

                        elif choice == 6:
                            print('Exiting the admin menu')
                            break
                        else:
                            print('Invalid number')
                    else:
                        print('It must be a number')
            else:
                print('Invalid number')
        else:
            print('It must be a number')

if __name__ == '__main__':
    main()