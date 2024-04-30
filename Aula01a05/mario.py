def main(size): 
    for i in range(size):
         print_column(i)
            
def print_row(row):
    print("@" * row)

def print_column(number):    

    for i in range(number):
        print_row(number)
        print("@")
        

main(10)