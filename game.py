import answer

print('당신에게는 사채가 1억 있었다.')
print('하지만 당신은 사채를 갚을 능력이 없었고 운이 좋게도 채권자가 달콤한 제안을 건넸다.')
print('문제 5개를 맞추면 빚을 모두 없애겠다는 제안을 당신은 거절할 수 없었다.')
print('문제를 피한다면 다가오는 것은 죽음 뿐')

print('진행하시겠습니까?')
print('1.진행한다.','2.포기한다.')
A = int(input())
if A == 1:
    print('정답은 숫자 혹은 영어 소문자만 사용해서 적으시면 됩니다.')
    answer.answer1()
    a1 = input()
    if a1 == 'm':
        print('정답입니다. 4문제 남았습니다.')
        answer.answer2()
    else:
        print('사망하셨습니다.')
        exit()
    a2 = input()
    if a2 == 'sky':
        print('정답입니다. 3문제 남았습니다.')
        answer.answer3()
    else:
        print('사망하셨습니다.')
        exit()    
    a3 = input()
    if a3 == '0':
        print('정답입니다. 2문제 남았습니다.')
        answer.answer4()
    else:
        print('사망하셨습니다.')
        exit()
    a4 = input()
    if a4 == 'pluto':
        print('정답입니다. 마지막 문제만 남았습니다.')
        answer.answer5()
    else:
        print('사망하셨습니다.')
        exit()
    a5 = input()
    if a5 == '21':
        print('당신은 모든 문제를 맞히고 살아 남으셨습니다.')
        print('다음에는 뵙는 일이 없기를')
    else:
        print('사망하셨습니다.')
        exit()
else:
    print('사망하셨습니다.')
    exit()