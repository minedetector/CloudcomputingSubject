import csv

with open('tudengid.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count > 0:
            username = row[0] + row[1]
            arn = 'arn:aws:iam::311962906195:policy/Tudengite-oigused'
            print(f'aws iam create-user --user-name {username}')
            print(f"aws iam create-login-profile --user-name {username} --password '{username}'1! --password-reset-required")
            print(f'aws iam attach-user-policy --policy-arn {arn} --user-name {username}')
            line_count += 1
    print(f'Processed {line_count} lines.')
