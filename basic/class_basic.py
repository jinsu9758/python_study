'''
클래스 : 반복되는 불필요한 소스코드를 최소화 하면서 컴퓨터 프로그래밍 상에서
쉽게 표현할 수 있도록 해주는 프로그래밍 기술

인스턴스 : 클래스로 정의된 객체를 프로그램 상에서 이용할 수 있게 만든 변수

클래스의 멤버 : 클래스 내부에 포함되는 변수

클래스의 함수 : 클래스 내부에 포함되는 함수. 메소드라고 부름

'''
class Car:
    #클래스의 생성자
    def __init__(self, name, color):
        self.name = name #클래스의 멤버
        self.color = color #클래스의 멤버
    #클래스 소멸자
    def __del__(self):
        print("인스턴스를 소멸시킵니다.")
    #클래스의 메소드
    def show_info(self):
        print("이름:", self.name,"\n","색상:", self.color)
    # Setter 메소드 (값을 바꿔주는 메서드로 자주 활용)
    def set_name(self, name):
        self.name = name

car1 = Car("소나타", "빨간색")
car1.show_info()
#접근
print(car1.name)
car1.set_name("아반떼")
car1.show_info()
del car1
#car1.show_info()

print()

car2 = Car("아반떼", "검은색")
car2.show_info()
