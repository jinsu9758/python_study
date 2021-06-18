# 마린 : 공격 유닛, 군인, 총을쓸 수 있음.
# name = "마린"
# hp = 40 # 유닛의 이름
# damage = 5 #유닛의 공격력

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# tank2_name = "탱크2"
# tank2_hp = 150
# tank2_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))


# def attack(name, location, damage):
#     print("{} : {} 방향으로 적군을 공격합니다. [공격력 : {}]".format(name, location, damage))
    
# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

# 이런 식으로 코딩을하게 되면 유닛이 많을 때 힘들어짐 -> 클래스 사용

#일반 유닛  #부모 클래스
class Unit:
    def __init__(self, name, hp, speed):    #필요한 값들을 정의를 해준다.
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self, location):
        print("지상유닛 이동")
        print("{} : {} 방향으로 이동합니다  속도 : {}".format(self.name, location, self.speed))

# marine1 = Unit("마린", 40, 5)    #Unit 클래스의 인스턴스
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# #레이스 : 공중 유닛, 비행기 클로킹 ( 상대방에게 보이지 않음 )
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {}, 공격력 : {}".format(wraith1.name, wraith1.damage)) #.(dot) 으로 멤버 변수에 접근 가능


# # 마인드 컨트롤 : 상대방 유닛을 내것으로 만드는 것 ( 빼앗음 )
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True  #클로킹이라는 변수는 클래스에 없는데, 외부에서 추가로 변수를 만들어서 써주었음.

# if wraith2.clocking == True:
#     print("{} 는 현재 클로킹 상태입니다.".format(wraith2.name))


#공격 유닛
class AttackUnit(Unit):  #상속받는 거임. #자식 클래스
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        #self.name = name
        #self.hp = hp
        self.damage = damage
    
    def attack(self, location):  #공격
        print("{} : {} 방향으로 적군을 공격합니다. 공격력 : {}".format(self.name, location, self.damage))
        
    def damaged(self, damage): #공격받은 거
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp<0:
            print("{} : 파괴되었습니다.".format(self.name))

#메딕 : 의무병
# 상속 이해하기 Unit 클래스 부분과 AttackUnit 부분에서 __init__ 에 겹치는 부분이 있음.
# 상속을 하게 되면 Unit의 멤버 변수부분들을 AttackUnit에서 사용할 수 있게 된다.


# 파이어뱃 : 공격 유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

# 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 x

#날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print("{} : {} 뱡향으로 날아갑니다. 속도 : {}".format(name, location, self.flying_speed))
              
              

             
#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) #지상스피드는 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):  #move 재 정의
        print("공중유닛 이동")
        self.fly(self.name, location)


#발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
#valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
#valkyrie.fly(valkyrie.name, "3시")
        

# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

#배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)


#벌쳐는 이동하려면 move 함수를 써야한고 battlecruiser는 fly 함수를 써야함.
#매번 지상유닛인지 공중유닛인지 확인을 해야함.
vulture.move("11시")
#battlecruiser.fly("battlecruiser.name", "9시")
battlecruiser.move("9시") #오버로딩

              
#건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #pass # 그냥 아무것도 안하고 넘어간다는 의미 ( 완성 취급 )
        #Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self,location = location

# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

              
