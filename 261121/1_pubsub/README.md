PWM : Pulse Width Modulation 통신채널


IMU : 관성측정, 가속도, 자이로스콥, 나침반


임베디드통신 프로토콜 ( communication protocol)
 - mcu와 센서, 액추에이터, 외부 제어 장치 사이에서 데이터를 교환하기 위한 토인 규칙
 - 데이터의 전송 순서, 신호 타이밍, 전송 형식 및 장치 식별 방법 등을 정의
 - 임베디드 시스템에서는 주로 직렬 통신
 
 
 동기 방식 : 통신하느 대상과 주기를 일치시키기 
 비동기 방식: 주기와 상관없이 데이터를 주는 방식, 전송 속도가 정해져 있음
 
 uart (비동기)
 
 - tx(트랜스미터)->rx(리시버)
 - 클럭 신호선 없이baud 레이트에 따라 통신
 
 
 I^2C(inter-integgrated circuit)
 
 - 적은 수의 신호로 연결하기 위한 동기식 직렬 통신
 - sda, scl 두개의 신호선 연결
 
 - 마스터(muc)가 클럭을 생성하고 통신할 slave(센서들)장치 선택
 - 선택된 슬레이브는 ack을 보내서 송신 확인
 
 
 
 도메인 id
 - 도메인 단위로 로스 노드들을 그룹화
 - 같은 도메인 아이뎅이 속하면 같은  DDS에 연결
 - 서로의 토픽을 자동으로 발견
 
 노드 한개 = 프로세스 1개 = 터미널 1개
 
 포즈 = 포지션 + 오리엔테이션
 
 
 QoS(Quality of Service) : 노드끼리 데이터를 주고 받을 때 적용하는 '통신 규칙'
- Reliability : reliable, best effort
- Durability : transient local, volatile


colcon workspace
- src/ : 개발자가 작성한 로스 패키지의 소스 코드
- build/ : 컴파일 및 빌드 과정에서 생성되는 중간 파일
- install/ : 빌드 및 설치된 실행 파일, 라이브러리, 설정 파일 등
- log/ : 빌드 및 테스트 과정의 로그
