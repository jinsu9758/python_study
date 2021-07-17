# 상속: 다른 클래스의 멤버 변수와 메소드를 물려받아 사용
# 부모와 자식 관계가 존재
# 자식 클래스 : 부모 클래스를 상속받은 클래스

class Unit: # 유닛
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(self.name,"이 공격을 수행합니다.\n전투력:", self.power)

#몬스터 클래스 -> 유닛이 가지고 있는 이름과 파워 변수를 다 가져야 함.
#Unit -> 부모 클래스
class Monster(Unit):
    def __init__(self, name, power, type):
        #self.name = name
        #self.power = power
        Unit.__init__(self, name, power)
        self.type = type


unit = Unit("홍길동", 375)
unit.attack()

monster = Monster("슬라임",10,"초급")
monster.attack()
