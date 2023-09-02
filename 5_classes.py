import json
import time
from collections import defaultdict, namedtuple
from dataclasses import dataclass
from datetime import datetime, timedelta
from pprint import pprint
from weakref import WeakKeyDictionary


class SimpleGradebook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)


book = SimpleGradebook()
book.add_student("Isaac Newton")
book.report_grade("Isaac Newton", 90)
book.report_grade("Isaac Newton", 95)
book.report_grade("Isaac Newton", 85)

print(book.average_grade("Isaac Newton"))


class BySubjectGradebook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = defaultdict(list)

    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0

        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)

        return total / count


book = BySubjectGradebook()
book.add_student("Albert Einstein")
book.report_grade("Albert Einstein", "Math", 75)
book.report_grade("Albert Einstein", "Math", 65)
book.report_grade("Albert Einstein", "Gym", 90)
book.report_grade("Albert Einstein", "Gym", 95)
print(book.average_grade("Albert Einstein"))


class WeightedGradebook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = defaultdict(list)

    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append((score, weight))

    def average_grade(self, name):
        by_subject = self._grades[name]

        score_sum, score_count = 0, 0

        for subject, scores in by_subject.items():
            subject_avg, total_weight = 0, 0

            for score, weight in scores:
                subject_avg += score * weight
                total_weight += weight

            score_sum += subject_avg / total_weight
            score_count += 1

        return score_sum / score_count


book = WeightedGradebook()
book.add_student("Albert Einstein")
book.report_grade("Albert Einstein", "Math", 75, 0.05)
book.report_grade("Albert Einstein", "Math", 65, 0.15)
book.report_grade("Albert Einstein", "Math", 70, 0.80)
book.report_grade("Albert Einstein", "Gym", 100, 0.40)
book.report_grade("Albert Einstein", "Gym", 85, 0.60)

print(book.average_grade("Albert Einstein"))


class Subject:
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append((score, weight))

    def average_grade(self):
        total, total_weight = 0, 0

        for score, weight in self._grades:
            total += score * weight
            total_weight += weight

        return total / total_weight


class Student:
    def __init__(self):
        self._subjects = defaultdict(Subject)

    def get_subject(self, name):
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0

        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1

        return total / count


class Gradebook:
    def __init__(self):
        self._students = defaultdict(Student)

    def get_student(self, name):
        return self._students[name]


book = Gradebook()
albert = book.get_student("Albert Einstein")
math = albert.get_subject("Math")
math.report_grade(75, 0.05)
math.report_grade(65, 0.15)
math.report_grade(70, 0.80)
gym = albert.get_subject("Gym")
gym.report_grade(100, 0.40)
gym.report_grade(85, 0.60)
print(albert.average_grade())


current = {"green": 12, "blue": 3}
increments = [
    ("red", 5),
    ("blue", 17),
    ("orange", 9),
]


def log_missing():
    print("Key added")
    return 0


result = defaultdict(log_missing, current)
print("Before:", dict(result))

for key, amount in increments:
    result[key] += amount
print("After:", dict(result))


def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count
        added_count += 1
        return 0

    result = defaultdict(missing, current)

    for key, amount in increments:
        result[key] += amount

    return result, added_count


class CountMissing:
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0


counter = CountMissing()
result = defaultdict(counter.missing, current)
for key, amount in increments:
    result[key] += amount

assert counter.added == 2


class BetterCountMissing:
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0


counter = BetterCountMissing()
assert callable(counter)

counter()
counter()
counter()

print(counter.added)

counter = BetterCountMissing()
result = defaultdict(counter, current)
for key, amount in increments:
    result[key] += amount
assert counter.added == 2


class InputData:
    def read(self):
        raise NotImplementedError


class PathInputData(InputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        with open(self.path) as f:
            return f.read()


class Worker:
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError


class LineCountWorker(Worker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count("\n")

    def reduce(self, other):
        self.result += other.result


class MyBaseClass:
    def __init__(self, value):
        self.value = value


class MyChildClass(MyBaseClass):
    def __init__(self):
        MyBaseClass.__init__(self, 5)


class TimesTwo:
    def __init__(self):
        self.value *= 2


class PlusFive:
    def __init__(self):
        self.value += 5


class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


foo = OneWay(5)
print("First ordering is (5 * 2) + 5 =", foo.value)


class AnotherWay(MyBaseClass, PlusFive, TimesTwo):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


bar = AnotherWay(5)
print("Second ordering still is", bar.value)


class TimesSeven(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 7


class PlusNine(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 9


class ThisWay(TimesSeven, PlusNine):
    def __init__(self, value):
        TimesSeven.__init__(self, value)
        PlusNine.__init__(self, value)


foo = ThisWay(5)
print("Should be (5 * 7) + 9 =", foo.value)


class TimesSevenCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value *= 7


class PlusNineCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value += 9


class GoodWay(TimesSevenCorrect, PlusNineCorrect):
    def __init__(self, value):
        super().__init__(value)


foo = GoodWay(5)
print("Should be 7 * (5 + 9) =", foo.value)


Grade = namedtuple("Grade", ("score", "weight"))
g1 = Grade(score=81, weight=0.30)
defaultdict(list)


class ToDictMixin:
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        output = {}

        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)

        return output

    def _traverse(self, key, value):
        if isinstance(value, ToDictMixin):
            return value.to_dict()

        elif isinstance(value, dict):
            return self._traverse_dict(value)

        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]

        elif hasattr(value, "__dict__"):
            return self._traverse_dict(value.__dict__)

        else:
            return value


class BinaryTree(ToDictMixin):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


tree = BinaryTree(
    10,
    left=BinaryTree(7, right=BinaryTree(9)),
    right=BinaryTree(13, left=BinaryTree(11)),
)

pprint(tree.to_dict())

tree2 = BinaryTree(12)
print(tree2.to_dict())


class BinaryTreeWithParent(BinaryTree):
    def __init__(self, value, left=None, right=None, parent=None):
        super().__init__(value, left=left, right=right)
        self.parent = parent

    def _traverse(self, key, value):
        if isinstance(value, BinaryTreeWithParent) and key == "parent":
            return value.value
        else:
            return super()._traverse(key, value)


root = BinaryTreeWithParent(10)
root.left = BinaryTreeWithParent(7, parent=root)
root.left.right = BinaryTreeWithParent(9, parent=root.left)
print(root.to_dict())


class JsonMixin:
    @classmethod
    def from_json(cls, data):
        kwargs = json.loads(data)
        return cls(**kwargs)

    def to_json(self):
        return json.dumps(self.to_dict())


class Switch(ToDictMixin, JsonMixin):
    def __init__(self, ports, speed):
        self.ports = ports
        self.speed = speed


class Machine(ToDictMixin, JsonMixin):
    def __init__(self, cores, ram, switch=None):
        self.cores = cores
        self.ram = ram
        self.switch = switch


class DatacenterRack(ToDictMixin, JsonMixin):
    def __init__(self, switch=None, machines=None):
        self.switch = switch
        self.machines = [Machine(**kwargs) for kwargs in machines]


serialized = """{
    "switch": {"ports": 5, "speed": 1e9},
    "machines": [
        {"cores": 8, "ram": 32e9},
        {"cores": 4, "ram": 16e9},
        {"cores": 2, "ram": 4e9}
    ]
}"""

deserialized = DatacenterRack.from_json(serialized)
print(deserialized.switch)


class MyObject:
    def __init__(self):
        self.public_field = 5
        self.__private_field = 10

    def get_private_field(self):
        return self.__private_field


foo = MyObject()
assert foo.public_field == 5
assert foo.get_private_field() == 10

# assert foo.__private_field == 10


class MyOtherObject:
    def __init__(self):
        self.__private_field = 71

    @classmethod
    def get_private_field_of_instance(cls, instance):
        return instance.__private_field


class MyParentObject:
    def __init__(self):
        self.__private_field = 71


class MyChildObject(MyParentObject):
    def get_private_field(self):
        return self.__private_field


baz = MyChildObject()
# baz.get_private_field()

assert baz._MyParentObject__private_field == 71


class TestClass:
    def __init__(self):
        self.__value = 123


a = TestClass()
print(a.__dict__)


class FrequncyList(list):
    def __init__(self, numbers):
        super().__init__(numbers)

    def frequency(self):
        counts = {}
        for item in self:
            counts.setdefault(item, 0)
            counts[item] += 1

        return counts


foo = FrequncyList(["a", "b", "a", "c", "b", "a", "d"])
print("Length is", len(foo))

foo.pop()
print("After pop:", repr(foo))
print("Frequency:", foo.frequency())


class Bucket:
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.quota = 0

    def __repr__(self):
        return f"Bucket(quota={self.quota})"


def fill(bucket, amount):
    now = datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = now

    bucket.quota += amount


def deduct(bucket, amount):
    now = datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        return False

    if bucket.quota - amount < 0:
        return False

    bucket.quota -= amount
    return True


bucket = Bucket(1)
fill(bucket, 100)
print(bucket)

if deduct(bucket, 99):
    print("Had 99 quota")
else:
    print("Not enough for 99 quota")

if deduct(bucket, 3):
    print("Had 3 quota")
else:
    print("Not enough for 3 quota")

print(bucket)


class NewBucket:
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.max_quota = 0
        self.quota_consumed = 0

    def __repr__(self):
        return (
            f"NewBucket(max_quota={self.max_quota}, "
            f"quota_consumed={self.quota_consumed})"
        )

    @property
    def quota(self):
        return self.max_quota - self.quota_consumed

    @quota.setter
    def quota(self, amount):
        delta = self.max_quota - amount

        if amount == 0:
            self.quota_consumed = 0
            self.max_quota = 0

        elif delta < 0:
            assert self.quota_consumed == 0
            self.max_quota = amount

        else:
            assert self.max_quota >= self.quota_consumed
            self.quota_consumed += delta


bucket = NewBucket(60)
print("Initial", bucket)

fill(bucket, 100)
print("Filled", bucket)

if deduct(bucket, 99):
    print("Had 99 quota")
else:
    print("Not enough for 99 quota")

print("Now", bucket)

if deduct(bucket, 3):
    print("Had 3 quota")
else:
    print("Not enough for 3 quota")

print("Still", bucket)


# better way 46) 재사용 가능한 @property 메서드에는 디스크립터를 사용하자
class Homework:
    def __init__(self):
        self._grade = 0

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Grade must be between 0 and 100")
        self._grade = value


galileo = Homework()
galileo.grade = 95


class Exam:
    def __init__(self):
        self._writing_grade = 0
        self._math_grade = 0

    @staticmethod
    def _check_grade(value):
        if not (0 <= value <= 100):
            raise ValueError("Grade must be between 0 and 100")

    @property
    def writing_grade(self):
        return self._writing_grade

    @writing_grade.setter
    def writing_grade(self, value):
        self._check_grade(value)
        self._writing_grade = value

    @property
    def math_grade(self):
        return self._math_grade

    @math_grade.setter
    def math_grade(self, value):
        self._check_grade(value)
        self._math_grade = value


class Grade:
    def __get__(self, instance, instance_type):
        return self.value

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Grade must be between 0 and 100")

        self.value = value


class Exam:
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


first_exam = Exam()
first_exam.writing_grade = 82
first_exam.science_grade = 99
print(f"Writing: {first_exam.writing_grade}")
print(f"Science: {first_exam.science_grade}")

second_exam = Exam()
second_exam.writing_grade = 75
print(f"Second Writing {second_exam.writing_grade}")  # 75
# writing_grade 클래스 애트리뷰트로 한 Grade 인스턴스를 공유하기 때문에 같은값이 나온다,
print(f"First Writing {first_exam.writing_grade}")  # 75


class Grade:
    def __init__(self):
        self._values = (
            {}
        )  # 모든 Exam 인스턴스에 대한 참조를 저장하고 있어서 절대로 참조 카운터가 0이 되지 않는다. (memory leak)

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Grade must be between 0 and 100")

        self._values[instance] = value


class Grade:
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Grade must be between 0 and 100")

        self._values[instance] = value


class Exam:
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


first_exam = Exam()
first_exam.writing_grade = 82
second_exam = Exam()
second_exam.writing_grade = 75
print(f"First Writing {first_exam.writing_grade}")  # 82
print(f"Second Writing {second_exam.writing_grade}")  # 75


# better way 47) 지연 계산 애트리뷰트가 필요하면 __getattr__, __getattribute__, __setattr__을 사용하자
class LazyRecord:
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = f"Value for {name}"
        setattr(self, name, value)
        return value


data = LazyRecord()
print("Before:", data.__dict__)
print("foo:", data.foo)  # 객체 딕셔너리안에 data.foo 는 없으므로 __getattr__ 호출
print("After:", data.__dict__)


class LoggingLazyRecord(LazyRecord):
    def __getattr__(self, name):
        print(f"* Called __getattr__({name!r}), " f"populating instance dictionary")
        result = super().__getattr__(name)
        print(f"* Returning {result!r}")
        return result


data = LoggingLazyRecord()
print("exists:", data.exists)  # __getattr__ 호출 안함
print("First foo:", data.foo)  # __getattr__ 호출
print("Second foo:", data.foo)  # __getattr__ 호출 안함


class ValidatingRecord:
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        print(f"* Called __getattribute__({name!r})")
        try:
            value = super().__getattribute__(name)
            print(f"* Found {name!r}, returning {value!r}")
            return value

        except AttributeError:
            value = f"Value for {name}"
            print(f"* Setting {name!r} to {value!r}")
            setattr(self, name, value)
            return value


class MissingPropertyRecord:
    def __getattr__(self, name):
        if name == "bad_name":
            raise AttributeError(f"{name} is missing")
        value = f"Value for {name}"
        setattr(self, name, value)
        return value


data = MissingPropertyRecord()
#data.bad_name  # AttributeError: bad_name is missing


# better way 48) __init_subclass__를 사용해 서브클래스를 검증하자

# meta class 에 대한 이해
class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print(f"* 실행: {name}의 메타 {meta}.__new__")
        print(f" 기반 클래스들: {bases}")
        print(class_dict)

        return type.__new__(meta, name, bases, class_dict)

class MyClass(metaclass=Meta):
    stuff = 123

    def foo(self):
        pass

class MySubclass(MyClass):
    other = 567

    def bar(self):
        pass


class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        if bases:
            if class_dict["sides"] < 3:
                raise ValueError("Polygons need 3+ sides")

        return type.__new__(meta, name, bases, class_dict)

class Polygon(metaclass=ValidatePolygon):
    sides = None

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180

class Triangle(Polygon):
    sides = 3


class Rectangle(Polygon):
    sides = 4


# class Nonagon(Polygon):
#     sides = 9
#
#
# assert Triangle.interior_angles() == 180
# assert Rectangle.interior_angles() == 360
# assert Nonagon.interior_angles() == 1260
#
# # print("Before class")
# #
# # class Line(Polygon):
# #     print("Before sides")
# #     sides = 1
# #     print("After sides")
# #
# # print("After class")
#
#
# class BetterPolygon:
#     sides = None
#
#     def __init_subclass__(cls):
#         super().__init_subclass__()
#         if cls.sides < 3:
#             raise ValueError("Polygons need 3+ sides")
#
#     @classmethod
#     def interior_angles(cls):
#         return (cls.sides - 2) * 180
#
# class Hexagon(BetterPolygon):
#     sides = 6
#
# print("Before class")
#
# class Point(BetterPolygon):
#     sides = 1
#
# print("After class")
#
#
# @dataclass
# class Exam:
#     math: int
#     writing: int
#
#     def __post_init__(self):
#         for field, value in self.__dict__.items():
#             if not (0 <= value <= 100):
#                 raise ValueError(f"{field}의 점수 {value}는 유효하지 않습니다. 0부터 100 사이의 값을 입력해주세요.")
#
#
def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class TheOne:
    @staticmethod
    def static_method():
        print("static_method123")


# o = TheOne()
# o.static_method()
#
# o2 = TheOne()

TheOne.static_method()
