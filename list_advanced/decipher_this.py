secret_message = input().split(' ')
message_list = []

for word in secret_message:
    ch_sum = 0
    s_part = []
    for i in range(len(word)):
        ch = word[i]
        if ch.isdigit():
            ch_sum = ch_sum * 10 + int(ch)
        else:
            s_part.append(ch)

    s_part[0], s_part[-1] = s_part[-1], s_part[0]
    message = chr(ch_sum) + ''.join(s_part)
    message_list.append(message)

print(' '.join(message_list))

