import csv

def check_len_csv(file_path_check):
    with open(file_path_check,'r') as file:
        read_file = file.read()
        return len(read_file)
    
    
def access_find_csv(file_path_access,domain_limitation_access,email_list_access):
    with open(file_path_access, newline='') as csvfile:
        reader_csv = csv.reader(csvfile)
        for elements in reader_csv:
            for email in elements:
                email = email.strip()
                if email.endswith(domain_limitation_access):
                    email_list_access.append(email)
 
def generate_csv(file_path_output,email_list_loop):
    with open(file_path_output, 'w', newline='', encoding='utf-8') as readfile:
        write_csv = csv.writer(readfile)
        write_csv.writerows([[email] for email in email_list_loop])

decision = True
while(decision):

    email_list = []

    domain_limitation= input("Please set the domain you want to appear in the final list: ")
    file_origin = input("Please write the file name with the extension that needs to be read:")
    file_path = 'domain-migration-analyzer/files/' + file_origin
    file_path_output = 'domain-migration-analyzer/files/output_' + file_origin

    if(check_len_csv(file_path) ==0):
        print("Empty CSV")
        break;
    
    access_find_csv(file_path,domain_limitation,email_list)
    generate_csv(file_path_output,email_list)

    cloop = input("Do you want to use another file? Y/N")
    cloop.lower()

    if cloop =='y':
        decision = True
    else:
        decision = False


