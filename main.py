# input section started 
N = 5
measurments = []
print("Введите 5 измерений, отправляя каждое с помощью ENTER: ")
for i in range(N):
    measurments.append(float(input()))
print("Введите цену деления на приборе: ")
partition= float(input())
# коэфициенты для 5 измерений
coefT = 2.8 
coefBeta = 0.51
coefU = 0.64
coefV = 1.67
# input section ended
measurments = sorted(measurments)
N = len(measurments)
scope = abs(measurments[4] - measurments[0]) # найдем размах
# проверка на промахи
if (abs(measurments[0] - measurments[1]) >= coefU*scope) or (abs(measurments[4] - measurments[3]) >= coefU*scope):
    print("Ошибка на этапе проверки на промахи")
median = sum(measurments) / N # найдем среднее
# найдем СКО
numerator = 0
for i in range(N):
    numerator += (measurments[i] - median)**2
sqDevitation = (numerator/(N - 1))**0.5

averageSqDevitation = sqDevitation / N**0.5 # найдем ско среднего

# найдем случайную погрешность
randomAccuracyScope = coefBeta*scope  # по размаху
randomAccuracyAverageSqDevitation = coefT*averageSqDevitation # по ско
randomAccuracy = max(randomAccuracyAverageSqDevitation, randomAccuracyScope) # выберем наибольшую случайную погрешность
instrumentAccuracy = partition/2 # найдем приборную погрешность
fullAccuracy = (randomAccuracy**2 + instrumentAccuracy**2)**0.5 # найдем полную погрешность
relativeAccuracy = (fullAccuracy/median) * 100 # найдем относительную погрешность
print("Относительная погрешность = ", relativeAccuracy, "%")
print("Ответ: ", median, '±', fullAccuracy)
print("Ответ округлите по правилам округления.")
