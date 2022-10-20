# ssh_user

Сreates a user, generates an ssh key for him and sends it to the hosts of the group

## Requirements

You will probably need to perform a pre-configuration

## Role Variables

- ssh_user_create_user: (string) create a user and a home directory for him. If the value is empty, the user will not be created
- ssh_user_sudo: (bool) add sudo for user
- ssh_user_create_home_path: (string) set a specific path to the directory
- ssh_user_create_ssh_key: (bool) create public and private ssh-keys
- ssh_user_put_ssh_key_for_group_name: (string) group name

## Dependencies

## Example Playbook

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - role: ssh_user

## License

Apache-2.0

## Author Information

- [habr](https://habr.com/ru/users/mmblsp/)
- mmblspace@yandex.ru
