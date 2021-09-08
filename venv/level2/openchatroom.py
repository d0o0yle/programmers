def solution(record):
    answer = []

    users = dict()
    commands = []

    for aRecord in record:
        contents = aRecord.split()
        command = contents[0]

        if command == 'Enter':
            users[contents[1]] = contents[2]
            commands.append((command, contents[1]))
        elif command == 'Change':
            users[contents[1]] = contents[2]
        elif command == 'Leave':
            commands.append((command, contents[1]))

    for command in commands:
        if command[0] == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(users[command[1]]))
        elif command[0] == 'Leave':
            answer.append('{}님이 나갔습니다.'.format(users[command[1]]))


    return answer

if __name__ == "__main__":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    result = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
    print('->', solution(record), result)