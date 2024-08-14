import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'BUULGYEONG01_LEEWONJAE'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909


# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')


while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
    #   - order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) balls[0][0]: 흰 공의 X좌표
    #         balls[0][1]: 흰 공의 Y좌표
    #         balls[1][0]: 1번 공의 X좌표
    #         balls[4][0]: 4번 공의 X좌표
    #         balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.


    r = 5.73 / 2
    BallIn = [False] * NUMBER_OF_BALLS
    for b in range(NUMBER_OF_BALLS):
        if balls[b][0] == -1 and balls[b][1] == -1: BallIn[b] = True

    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    if order ==1:
        myB, enB = [1,3], [2,4]
    else:
        myB, enB = [2,4], [1,3]
    
    # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
    if order == 1:
        if BallIn[1] and BallIn[3]:
            myB.append(5)
    elif order == 2:
        if BallIn[2] and BallIn[4]:
            myB.append(5)
    
    list(set(myB))
    for b in myB:
        if not BallIn[b]:
            targetBall_x = balls[b][0]
            targetBall_y = balls[b][1]
            break

    # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
    # targetBall_x = balls[1][0]
    # targetBall_y = balls[1][1]
    # for num in range(1, 6):             # 목적구의 좌표를 나타내기 위한 반복문
    #     targetBall_x = balls[num][0]        # 목적구의 x좌표
    #     targetBall_y = balls[num][1]        # 목적구의 y좌표
    #     if targetBall_x >= 0 and targetBall_y >= 0: # 만약 목적구의 좌표가 0크면(당구대에 존재하면)
    #         break                           # break를 걸어 그 공을 목적구로 지정

    # width, height: 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
    width = abs(targetBall_x - whiteBall_x)
    height = abs(targetBall_y - whiteBall_y)   

    # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
    #   - 1radian = 180 / PI (도)
    #   - 1도 = PI / 180 (radian)
    # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
    # radian = math.atan(width / height) if height > 0 else 0
    # angle = 180 / math.pi * radian
    
    # 목적구가 흰 공과 상하좌우로 일직선상에 위치했을 때 각도 입력
    if whiteBall_x == targetBall_x:
        if whiteBall_y < targetBall_y:
            angle = 0
        else:
            angle = 180
    elif whiteBall_y == targetBall_y:
        if whiteBall_x < targetBall_x:
            angle = 90.0005
        else:
            angle = 270
    distance = math.sqrt(width**2 + height**2)

    # 강의 내용에 포함된 삼각함수 내용에서 영감을 얻었습니다.
    # 삼각함수를 이용하여 빗겨 쳐서 넣을 수 있는 각도를 구했습니다...
    # 흰 공과 목적구의 위치를 비교하여
    # 목적구가 흰 공을 중심으로 1사분면에 위치했을 때 각도를 재계산
    if whiteBall_x < targetBall_x and whiteBall_y < targetBall_y:
        aa = (HOLES[5][0] - whiteBall_x)**2 + (HOLES[5][1] - whiteBall_y)**2        # 흰 공과 HOLES[5] 사이의 거리
        bb = (HOLES[5][0] - targetBall_x)**2 + (HOLES[5][1] - targetBall_y)**2      # 목적구와 HOLES[5] 사이의 거리
        cc = (targetBall_x - whiteBall_x)**2 + (targetBall_y - whiteBall_y)**2      # 흰 공과 목적구 사이의 거리
        a = math.sqrt(aa)
        b = math.sqrt(bb)
        c = math.sqrt(cc)
        degree_1_radian = math.atan((HOLES[5][0] - whiteBall_x) / (HOLES[5][1] - whiteBall_y))  # 흰 공과 HOLES[5]가 이루는 각도
        degree_1 = math.degrees(degree_1_radian)        # 라디안을 degree로 변경
        cos_degree_2 = (aa + bb - cc) / (2 * a * b)     # 
        dd = aa + (b + 2*r)**2 - 2 * a * (b + 2*r)*cos_degree_2
        degree_3_radian = math.acos((aa + dd - (b + 2*r)**2) / (2 * a * math.sqrt(dd)))
        degree_3 = math.degrees(degree_3_radian)
        if  ((targetBall_y - whiteBall_y) / (targetBall_x - whiteBall_x)) > ((HOLES[5][1] - whiteBall_y) / (HOLES[5][0] - whiteBall_x)):
            angle = (degree_1 - (degree_3 * 1.00000005))
        else:
            angle = (degree_1 + (degree_3 * 0.99999995))
        distance = max(b, c)


    # 목적구가 흰 공을 중심으로 2사분면에 위치했을 때 각도를 재계산
    elif whiteBall_x > targetBall_x and whiteBall_y < targetBall_y:
        aa = (HOLES[3][0] - whiteBall_x)**2 + (HOLES[3][1] - whiteBall_y)**2
        bb = (HOLES[3][0] - targetBall_x)**2 + (HOLES[3][1] - targetBall_y)**2
        cc = (targetBall_x - whiteBall_x)**2 + (targetBall_y - whiteBall_y)**2
        a = math.sqrt(aa)
        b = math.sqrt(bb)
        c = math.sqrt(cc)
        degree_1_radian = math.atan((HOLES[3][1] - whiteBall_y) / whiteBall_x)
        degree_1 = math.degrees(degree_1_radian)
        cos_degree_2 = (aa + bb - cc) / (2 * a * b)
        dd = aa + (b + 2*r)**2 - 2 * a * (b + 2*r)*cos_degree_2
        degree_3_radian = math.acos((aa + dd - (b + 2*r)**2) / (2 * a * math.sqrt(dd)))
        degree_3 = math.degrees(degree_3_radian)
        if  abs((targetBall_y - whiteBall_y) / (targetBall_x - whiteBall_x)) > abs((HOLES[3][1] - whiteBall_y) / (HOLES[3][0] - whiteBall_x)):
            angle = (degree_1 + (degree_3 * 1.00000005)) + 270
        else:
            angle = (degree_1 - (degree_3 * 0.99999995)) + 270
        distance = max(b, c)


    # 목적구가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
    elif whiteBall_x > targetBall_x and whiteBall_y > targetBall_y:
        aa = (HOLES[0][0] - whiteBall_x)**2 + (HOLES[0][1] - whiteBall_y)**2
        bb = (HOLES[0][0] - targetBall_x)**2 + (HOLES[0][1] - targetBall_y)**2
        cc = (targetBall_x - whiteBall_x)**2 + (targetBall_y - whiteBall_y)**2
        a = math.sqrt(aa)
        b = math.sqrt(bb)
        c = math.sqrt(cc)
        degree_1_radian = math.atan(whiteBall_x / whiteBall_y)
        degree_1 = math.degrees(degree_1_radian)
        cos_degree_2 = (aa + bb - cc) / (2 * a * b)
        dd = aa + (b + 2*r)**2 - 2 * a * (b + 2*r)*cos_degree_2
        degree_3_radian = math.acos((aa + dd - (b + 2*r)**2) / (2 * a * math.sqrt(dd)))
        degree_3 = math.degrees(degree_3_radian)
        if  abs((targetBall_y - whiteBall_y) / (targetBall_x - whiteBall_x)) < abs((HOLES[0][1] - whiteBall_y) / (HOLES[0][0] - whiteBall_x)):
            angle = (degree_1 + (degree_3 * 1.00000005)) + 180
        else:
            angle = (degree_1 - (degree_3 * 0.99999995)) + 180
        distance = max(b, c)


    # 목적구가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
    elif whiteBall_x < targetBall_x and whiteBall_y > targetBall_y:
        aa = (HOLES[2][0] - whiteBall_x)**2 + (HOLES[2][1] - whiteBall_y)**2
        bb = (HOLES[2][0] - targetBall_x)**2 + (HOLES[2][1] - targetBall_y)**2
        cc = (targetBall_x - whiteBall_x)**2 + (targetBall_y - whiteBall_y)**2
        a = math.sqrt(aa)
        b = math.sqrt(bb)
        c = math.sqrt(cc)
        degree_1_radian = math.atan(whiteBall_y / (HOLES[2][0] - whiteBall_x))
        degree_1 = math.degrees(degree_1_radian)
        cos_degree_2 = (aa + bb - cc) / (2 * a * b)
        dd = aa + (b + 2*r)**2 - 2 * a * (b + 2*r)*cos_degree_2
        degree_3_radian = math.acos((aa + dd - (b + 2*r)**2) / (2 * a * math.sqrt(dd)))
        degree_3 = math.degrees(degree_3_radian)
        if  abs((targetBall_y - whiteBall_y) / (targetBall_x - whiteBall_x)) < abs((HOLES[2][1] - whiteBall_y) / (HOLES[2][0] - whiteBall_x)):
            angle = (degree_1 - (degree_3 * 1.00000005)) + 90
        else:
            angle = (degree_1 + (degree_3 * 0.99999995)) + 90
        distance = max(b, c)
    


        

    power = distance * 0.6
    # 주어진 sample code에는 목적구가 1, 3, 4사분면에 위치했을 때 각도를 구하는 식이 완성되어 있어서 stage3까지 손 대지 않고도 clear 했습니다.
    # 하지만 stage4에서 2사분면에 존재하는 목적구를 맞추기 위해 각도를 구하는 code가 없어 식을 구해야 했고,
    # 각도를 구했지만 흰 공과 목적구와의 각도를 구했지만 Hole까지의 각도는 신경쓰지 못하여 한 번에 넣기 어려웠습니다.
    # 주어진 sample code의 힘의 세기를 그대로 사용하니 stage clear가 어려워 힘을 강하게 주지 않아서 Hole로 영점을 맞춰가는 전략을 짰습니다...
    # 하지만 목적구를 빗겨 치지 않아서 stage가 올라갈수록 힘을 잃어가는 전략이 되었습니다...




    # 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
    # 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
    #   - angle: 흰 공을 때려서 보낼 방향(각도)
    #   - power: 흰 공을 때릴 힘의 세기
    # 
    # 이 때 주의할 점은 power는 100을 초과할 수 없으며,
    # power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
    #
    # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')