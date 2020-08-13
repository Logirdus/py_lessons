"""
Вам дано описание наследования классов в следующем формате.
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

Или эквивалентно записи:

class Class1(Class2, Class3 ... ClassK):
    pass

Класс A является прямым предком класса B, если B отнаследован от A:

class B(A):
    pass

Класс A является предком класса B, если

    A = B;
    A - прямой предок B
    существует такой класс C, что C - прямой предок B и A - предок C

Например:
class B(A):
    pass

class C(B):
    pass

# A -- предок С

Вам необходимо отвечать на запросы, является ли один класс предком другого класса

Важное примечание:
Создавать классы не требуется.
Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
Формат входных данных

В первой строке входных данных содержится целое число n - число классов.

В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й
класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от
себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число q - количество запросов.

В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.
Формат выходных данных

Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No", если не
является.

Sample Input:

4
A
B : A
C : A
D : B C
4
A B
B D
C D
D A


3
A
B : A
C : B
3
A B
B C
A C

Sample Output:

Yes
Yes
Yes
No
"""



def found_parent(class_search, class_search_parent):
    # алгоритм поиска в глубину https://foxford.ru/wiki/informatika/algoritm-poiska-v-glubinu
    # ищем все пути из класса class_search до корня (класса без предков)
    # посещенные классы отмечаем в списке visited, чтобы не посещать их дважды
    visited.append(class_search)
    for p in classes[class_search]:
        if p not in visited:
            found_parent(p, class_search_parent)
    # ищем предка в списке par
    if class_search_parent in visited:
        return True
    else:
        return False


classes = {}
# заполняем словарь classes
n = int(input())
for i in range(n):
    class_description = input().split()
    class_name = class_description[0]
    class_parents = class_description[2:]
    classes[class_name] = class_parents

q = int(input())
for i in range(q):
    class_search_description = input().split()
    class_search_parent = class_search_description[0]
    class_search = class_search_description[1]
    visited = []
    if found_parent(class_search, class_search_parent) or class_search_parent == class_search:
        print('Yes')
    else:
        print('No')