import csv

creation_file = open('user-creation-commands.txt', 'a')
deletion_file = open('user-deletion-commands.txt', 'a')
with open('tudengid.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            username = row[0] + row[1]
            group = 'Tudengid'
            arn = 'arn:aws:iam::311962906195:policy/Tudengite-oigused'

            create_user = (f'aws iam create-user --user-name {username}\n')
            create_user_pw = (f"aws iam create-login-profile --user-name {username} --password '{username}1!' --password-reset-required\n")
            add_user_to_group = (f'aws iam add-user-to-group --user-name {username} --group-name  {group}\n')

            creation_file.write(create_user)
            creation_file.write(create_user_pw)
            creation_file.write(add_user_to_group)

            remove_user_from_group = f'aws iam remove-user-from-group --user-name {username} --group-name {group}\n'
            delete_user_login_profile = f'aws iam delete-login-profile --user-name {username}\n'
            delete_user = f'aws iam delete-user --user-name {username}\n'

            deletion_file.write(remove_user_from_group)
            deletion_file.write(delete_user_login_profile)
            deletion_file.write(delete_user)

            line_count += 1
    print(f'Loodi {line_count - 1} kasutajat.')
creation_file.close()
deletion_file.close()
