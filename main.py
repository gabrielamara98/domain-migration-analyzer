import csv


domain_limitation= str(input("Please set the domain you want to appear in the final list: "))
file_origin = str(input("Please write the file name with the extension that needs to be read:"))

email_list = []
email_list_correct = []
email_list_denied = []


with open('domain-migration-analyzer/files/'+file_origin, newline='') as csvfile:
    reader_csv = csv.reader(csvfile)

    for elements in reader_csv:
        for email in elements:
            if email in domain_limitation:
                email_list_correct.append(email)
            else:
                email_list_denied.append(email)
      
print(email_list_correct)
print(email_list_denied)
